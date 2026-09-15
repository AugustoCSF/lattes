import json
import os
import sys

import JCR2024 as jcr
import baremas
import relatorioQualis as rq


DEFAULT_YEARS = [str(year) for year in range(2021, 2026)]


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def section(data, *path):
    current = data
    for key in path:
        if not isinstance(current, dict):
            return {}
        current = current.get(key)
    return current if isinstance(current, dict) else {}


def container(data, *path):
    current = data
    for key in path:
        if not isinstance(current, dict):
            return {}
        current = current.get(key)
    if isinstance(current, list) and len(current) == 1 and isinstance(current[0], dict):
        return current[0]
    return current if isinstance(current, dict) else {}


def records(data, *path):
    current = data
    for key in path:
        if not isinstance(current, dict):
            return as_list(current)
        current = current.get(key)
    if isinstance(current, list):
        return current
    if not isinstance(current, dict) or not current:
        return []
    for value in current.values():
        if isinstance(value, list):
            return value
        if isinstance(value, dict):
            return as_list(value)
    return []


def value(record, key, default=""):
    if not isinstance(record, dict):
        return default
    result = record.get(key, default)
    return default if result is None else result


def normalize_issn(issn):
    issn = str(issn or "").strip().upper()
    if len(issn) == 8 and "-" not in issn:
        return issn[:4] + "-" + issn[4:]
    return issn


def create_researcher(assessment, years):
    classes = {
        "A": baremas.PesquisadorA,
        "E": baremas.PesquisadorE,
        "H": baremas.PesquisadorH,
    }
    try:
        return classes[assessment.upper()]("", years)
    except KeyError as error:
        raise ValueError("assessment must be A, E or H") from error


def classify_article(researcher, year, issn):
    if year not in researcher.avaliacao:
        return ""

    if issn in jcr.jcr:
        researcher.avaliacao[year].addJCR()
        return f"JCR:{jcr.jcr[issn][0]}"
    if issn in jcr.eissn:
        researcher.avaliacao[year].addJCR()
        return f"JCR:{jcr.eissn[issn][0]}"
    if issn in rq.estratoQualis:
        qualis = rq.estratoQualis[issn][1]
        methods = {
            "A1": "addA1",
            "A2": "addA2",
            "A3": "addA3",
            "A4": "addA4",
            "B1": "addB1B2",
            "B2": "addB1B2",
            "B3": "addB3B4",
            "B4": "addB3B4",
        }
        method = methods.get(qualis)
        if method:
            getattr(researcher.avaliacao[year], method)()
        return qualis
    return ""


def populate_researcher(data, researcher, years):
    general = section(data, "DADOS-GERAIS")
    researcher.nome = value(general, "NOME-COMPLETO").replace("Vin?cius", "Vinicius").replace("VIN?CIUS", "VINICIUS")
    formation = section(general, "FORMACAO-ACADEMICA-TITULACAO")
    researcher.doutorado = bool(as_list(formation.get("DOUTORADO")))
    researcher.mestrado = bool(as_list(formation.get("MESTRADO"))) and not researcher.doutorado
    researcher.bolsistaPQ = researcher.nome.upper() in baremas_bolsistas_pq()

    publications = []
    bibliography = section(data, "PRODUCAO-BIBLIOGRAFICA")

    for article in records(bibliography, "ARTIGOS-PUBLICADOS"):
        basic = section(article, "DADOS-BASICOS-DO-ARTIGO")
        detail = section(article, "DETALHAMENTO-DO-ARTIGO")
        year = value(basic, "ANO-DO-ARTIGO")
        if year not in years:
            continue
        issn = normalize_issn(value(detail, "ISSN"))
        qualis = classify_article(researcher, year, issn)
        if not qualis or qualis.upper().startswith("C"):
            continue
        publications.append([
            year,
            researcher.nome,
            "Doutorado" if researcher.doutorado else "Mestrado" if researcher.mestrado else "",
            value(basic, "DOI"),
            value(basic, "TITULO-DO-ARTIGO"),
            "Periodico",
            qualis,
            "",
            f"{issn};{value(detail, 'TITULO-DO-PERIODICO-OU-REVISTA')}",
        ])

    books = section(bibliography, "LIVROS-E-CAPITULOS")
    for book in records(books, "LIVROS-PUBLICADOS-OU-ORGANIZADOS"):
        basic = section(book, "DADOS-BASICOS-DO-LIVRO")
        detail = section(book, "DETALHAMENTO-DO-LIVRO")
        year = value(basic, "ANO")
        if year not in years:
            continue
        book_type = value(basic, "TIPO")
        if book_type == "LIVRO_PUBLICADO":
            researcher.avaliacao[year].addLivroTecnico()
            label = "Livro:Publicado"
        elif book_type == "LIVRO_ORGANIZADO_OU_EDICAO":
            researcher.avaliacao[year].addOrganizacaoLivro()
            label = "Livro:Organizado/Editado"
        else:
            continue
        publications.append([
            year, researcher.nome, "", value(basic, "DOI"),
            value(basic, "TITULO-DO-LIVRO"), label, value(detail, "ISBN"), "", "",
        ])

    seen_chapters = set()
    for chapter in records(books, "CAPITULOS-DE-LIVROS-PUBLICADOS"):
        basic = section(chapter, "DADOS-BASICOS-DO-CAPITULO")
        detail = section(chapter, "DETALHAMENTO-DO-CAPITULO")
        year = value(basic, "ANO")
        if year not in years:
            continue
        isbn = value(detail, "ISBN")
        title = value(detail, "TITULO-DO-LIVRO")
        identity = isbn or title
        if identity in seen_chapters or title[:6].upper() == "ANAIS ":
            continue
        seen_chapters.add(identity)
        researcher.avaliacao[year].addCapituloLivro()
        publications.append([
            year, researcher.nome, "", value(basic, "DOI"),
            value(basic, "TITULO-DO-CAPITULO-DO-LIVRO"), "Capitulo Livro",
            isbn, "", title,
        ])

    for work in records(bibliography, "TRABALHOS-EM-EVENTOS"):
        basic = section(work, "DADOS-BASICOS-DO-TRABALHO")
        detail = section(work, "DETALHAMENTO-DO-TRABALHO")
        year = value(basic, "ANO-DO-TRABALHO")
        if year not in years or value(basic, "NATUREZA") != "COMPLETO":
            continue
        classification = value(detail, "CLASSIFICACAO-DO-EVENTO")
        if classification == "INTERNACIONAL":
            researcher.avaliacao[year].addTrabalhoInternacional()
        elif classification == "NACIONAL":
            researcher.avaliacao[year].addTrabalhoNacional()
        else:
            continue
        publications.append([
            year, researcher.nome, "", value(basic, "DOI"),
            value(basic, "TITULO-DO-TRABALHO"), "Congresso:Completo",
            value(detail, "ISBN"), classification, value(detail, "NOME-DO-EVENTO"),
        ])

    technical = container(data, "PRODUCAO-TECNICA", "DEMAIS-TIPOS-DE-PRODUCAO-TECNICA")
    for event in records(technical, "ORGANIZACAO-DE-EVENTO"):
        basic = section(event, "DADOS-BASICOS-DA-ORGANIZACAO-DE-EVENTO")
        year = value(basic, "ANO")
        if year not in years:
            continue
        event_type = value(basic, "TIPO")
        nature = value(basic, "NATUREZA")
        if event_type == "CONGRESSO" and nature == "ORGANIZACAO":
            researcher.avaliacao[year].addOrganizacaoEventos()
        elif event_type in ("FESTIVAL", "CONCERTO", "EXPOSICAO", "CONCURSO"):
            if nature == "CURADORIA":
                researcher.avaliacao[year].addCuradoria()
            elif nature == "ORGANIZACAO":
                researcher.avaliacao[year].addOrganizacaoFestival()
        else:
            continue

    orientations = container(data, "OUTRA-PRODUCAO", "ORIENTACOES-CONCLUIDAS")
    orientation_categories = {
        "ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO": ("DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO", "addTeseDoutorado"),
        "ORIENTACOES-CONCLUIDAS-PARA-MESTRADO": ("DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO", "addDissertacaoMestrado"),
        "ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO": ("DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO", "addSupervisaoPosDoc"),
    }
    for category, (basic_key, method) in orientation_categories.items():
        for orientation in as_list(orientations.get(category)):
            basic = section(orientation, basic_key)
            detail_key = basic_key.replace("DADOS-BASICOS", "DETALHAMENTO")
            detail = section(orientation, detail_key)
            year = value(basic, "ANO")
            if year not in years or value(detail, "TIPO-DE-ORIENTACAO") == "CO_ORIENTADOR":
                continue
            getattr(researcher.avaliacao[year], method)()

    other_orientation_key = "DADOS-BASICOS-DE-OUTRAS-ORIENTACOES-CONCLUIDAS"
    other_detail_key = "DETALHAMENTO-DE-OUTRAS-ORIENTACOES-CONCLUIDAS"
    for orientation in as_list(orientations.get("OUTRAS-ORIENTACOES-CONCLUIDAS")):
        basic = section(orientation, other_orientation_key)
        detail = section(orientation, other_detail_key)
        year = value(basic, "ANO")
        nature = value(basic, "NATUREZA")
        if year not in years or value(detail, "TIPO-DE-ORIENTACAO-CONCLUIDA") == "CO_ORIENTADOR":
            continue
        if nature == "TRABALHO_DE_CONCLUSAO_DE_CURSO_GRADUACAO":
            researcher.avaliacao[year].addTCCGraduacao()
        elif nature == "INICIACAO_CIENTIFICA":
            researcher.avaliacao[year].addIniciacaoCientifica()
        elif nature == "MONOGRAFIA_DE_CONCLUSAO_DE_CURSO_APERFEICOAMENTO_E_ESPECIALIZACAO":
            researcher.avaliacao[year].addTCCEspecializacao()

    return publications


def baremas_bolsistas_pq():
    return {
        "VINICIUS CARVALHO PEREIRA",
    }


def generate_json_barema(json_path, output_path, assessment="H", years=None):
    years = years or DEFAULT_YEARS
    data = load_json(json_path)
    researcher = create_researcher(assessment, years)
    publications = populate_researcher(data, researcher, years)
    with open(output_path, "w", encoding="utf-8") as file:
        file.writelines(baremas.geraHTML(researcher))
    return researcher, publications


def main(argv=None):
    argv = argv or sys.argv[1:]
    if len(argv) not in (2, 3):
        print("Usage: python json_barema.py <curriculo.json> <saida.html> [A|E|H]")
        return 2
    assessment = argv[2] if len(argv) == 3 else "H"
    researcher, publications = generate_json_barema(argv[0], argv[1], assessment)
    print(f"Researcher: {researcher.nome}")
    print(f"Score: {researcher.pontuacao_total()}")
    print(f"Publications exported: {len(publications)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
