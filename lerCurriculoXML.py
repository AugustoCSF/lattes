import os
import csv
import unicodedata
import baremas
from xml.dom.minidom import parse
from datetime import datetime
import relatorioQualis as rq
import JCR2024 as jcr

revistas = {
    '?': '-',
    '?GORA': 'AGORA',
    'ADMINISTRA??O': 'ADMINISTRACAO',
    'AGR?RIAS': 'AGRARIAS',
    'ANT?TESIS': 'ANTITESIS',
    'APLICA??O': 'APLICACAO',
    'ARAC?': 'ARACE',
    'ARET?': 'ARETE',
    'BEITR?GE': 'BEITRAGE',
    'BIOL?GICA': 'BIOLOGICA',
    'BIOMATEM?TICA': 'BIOMATEMATICA',
    'CENT?RIAS': 'CENTURIAS',
    'CI?NCIA': 'CIENCIA',
    'CI?NCIAS': 'CIENCIAS',
    'COLE??O': 'COLECAO',
    'COM?RCIO': 'COMERCIO',
    'CONSTRU?DO': 'CONSTRUIDO',
    'CIUDADAN?AS': 'CIUDADANIAS',
    'COMUNICA??O': 'COMUNICACAO',
    'COINSPIRA??O': 'COINSPIRACAO',
    'DI?LOGOS': 'DIALOGOS',
    'DOC?NCIA': 'DOCENCIA',
    'EDI??O': 'EDICAO',
    'ENFERMER?A': 'ENFERMERIA',
    'EDUCA??O': 'EDUCACAO',
    'EDUCA??O:': 'EDUCACAO:',
    'EDUCAC?ON': 'EDUCACION',
    'ELETR?NICA': 'ELETRONICA',
    'ESPA?OLAS': 'ESPANHOLAS',
    'EXTENS?O': 'EXTENSAO',
    'FILOS?FICA': 'FILOSOFICA',
    'F?SICA': 'FISICA',
    'F?SICO': 'FISICO',
    'F?SICOS': 'FISICOS',
    'GEOCI?NCIAS': 'GEOCIENCIAS',
    'GRADUA??O': 'GRADUACAO',
    'HIST?RIA': 'HISTORIA',
    'HUMAN?STICA': 'HUMANISTICA',
    'IND?STRIA': 'INDUSTRIA',
    'INFORMA??O': 'INFORMACAO',
    'INFORM?TICA': 'INFORMATICA',
    'INGL?S': 'INGLES',
    'INGL?S)': 'INGLES)',
    'INVESTIGACI?N': 'INVESTIGACION',
    'L?NEA': 'LINEA',
    'L?NEA)': 'LINEA)',
    'MATEM?TICA': 'MATEMATICA',
    'METR?POLE': 'METROPOLE',
    'PEDAG?GICO': 'PEDAGOGICO',
    'POL?TICAS': 'POLITICAS',
    'P?S': 'POS',
    'PROSPEC??O': 'PROSPECCAO',
    'PSIQUIATR?A': 'PSIQUIATRIA',
    'P?BLICA': 'PUBLICA',
    'RA?DO': 'RAIDO',
    'S?O':  'SAO',
    '(S?O':  '(SAO',
    'SA?DE': 'SAUDE',
    'TERRIT?RIO': 'TERRITORIO',
    'VETERIN?RIA': 'VETERINARIA',
    'ZOOL?GICA': 'ZOOLGICA'
}

nomes = {
    'Al?ssio': 'Alessio',
    'Aliss?ia': 'Alisseia',
    'A?lvaro': 'Alvaro',
    'A?lvares': 'Alvares',
    'Am?rico': 'Americo',
    'Am?lcar': 'Amilcar',
    'Andr?': 'Andre',
    'Andr?a': 'Andrea',
    'Andr?ia': 'Andreia',
    'Ant?nio': 'Antonio',
    'Ara?jo': 'Araujo',
    'B?rbara': 'Barbara',
    'Baldu?no': 'Balduino',
    'Brand?o': 'Brandao',
    'B?ttner': 'Buttner',
    'C?ndido': 'Candido',
    'C?ssia': 'Cassia',
    'Cl?udia': 'Claudia',
    'Concei??o': 'Conceicao',
    'C?rdova': 'Cordova',
    'Corr?a': 'Correa',
    'Crist?v?o': 'Cristovao',
    'D?lia': 'Dalia',
    'D?nis': 'Denis',
    'Edi?lida': 'Edialida',
    'Elo?': 'Eloa',
    'Eust?quio': 'Eustaquio',
    'F?bio': 'Fabio',
    'Fabr?cio': 'Fabricio',
    'F?lix': 'Felix',
    'Fl?res': 'Flores',
    'Fl?via': 'Flavia',
    'Fran?a': 'Franca',
    'Gl?ucia': 'Glaucia',
    'G?lvia': 'Gloria',
    'Guimar?es': 'Guimaraes',
    'Gon?alves': 'Goncalves',
    'Gouv?a': 'Gouvea',
    'H?lio': 'Helio',
    'Ja?anan': 'Jacanan',
    'J?ssica': 'Jessica',
    'J?sus': 'Jesus',
    'Jo?o': 'Joao',
    'Jord?o': 'Jordao',
    'Jos?': 'Jose',
    'J?lia': 'Julia',
    'J?lio': 'Julio',
    'J?nior': 'Junior',
    'La?s': 'Lais',
    'Le?o': 'Leao',
    'L?lica': 'Lilica',
    'Louren?o': 'Lourenco',
    'L?cia': 'Lucia',
    'L?cio': 'Lucio',
    'Lu?sa': 'Luisa',
    'Magalh?es': 'Magalhaes',
    'M?rcia': 'Marcia',
    'Mar?lia': 'Marilia',
    'Marin?z': 'Marinez',
    'M?rio': 'Mario',
    'Maur?cio': 'Mauricio',
    'Mendon?a': 'Mendonca',
    'Mois?s': 'Moises',
    'N?dia': 'Nadia',
    'Nic?cio': 'Nicacio',
    'Ol?via': 'Olivia',
    'On?': 'Ona',
    'Ort?z': 'Ortiz',
    'Pac?fica': 'Pacifica',
    'P?mela': 'Pamela',
    'Patr?cia': 'Patricia',
    'Prim?o': 'Primao',
    'Proc?pio': 'Procopio',
    'R?gia': 'Regia',
    'Rodr?guez': 'Rodriguez',
    'Rog?rio': 'Rogerio',
    'Rom?rio': 'Romario',
    'S?o': 'Sao',
    'Sebasti?o': 'Sebastiao',
    'S?rgio': 'Sergio',
    'Sim?es': 'Simoes',
    'Su?lem': 'Suelem',
    'Tha?s': 'Thais',
    'Val?ria': 'Valeria',
    'Vl?dia': 'Vladia',
    'Ven?ga': 'Venega',
    'Vin?cius': 'Vinicius',
    'Virg?nia': 'Virginia',
    'V?tor': 'Vitor'
}

bolsistaPQ = [
  "ADENILDA CRISTINA HONORIO FRANCA",
  "ADILSON PACHECO DE SOUZA",
  "ALESANDRO FERREIRA DOS SANTOS",
  "ALEX NEVES JUNIOR",
  "AMARILDO SALINA RUIZ",
  "AMILCAR SABINO DAMAZO",
  "ANDERSON CORASSA",
  "ANDRE SOARES DE OLIVEIRA",
  "ARLEANA DO BOM PARTO FERREIRA DE ALMEIDA",
  "BRUNA ANDRADE IRINEU",
  "CRISTIANO MACIEL",
  "DALTON HENRIQUE PEREIRA",
  "DOMINGOS DE JESUS RODRIGUES",
  "DOMINGOS TABAJARA DE OLIVEIRA MARTINS",
  "EDLLEY MAX PESSOA DA SILVA",
  "EDUARDO EUSTAQUIO DE SOUZA FIGUEIREDO",
  "EDUARDO GUIMARAES COUTO",
  "EDUARDO HENRIQUE BEVITORI KLING DE MORAES",
  "EDUARDO LUZIA FRANCA",
  "ERALCI MOREIRA TEREZIO",
  "FABIANO ANDRE PETTER",
  "FERNANDA REGINA CASAGRANDE GIACHINI VITORINO",
  "FERNANDO ZAGURY VAZ DE MELLO",
  "FILOMENA MARIA DE ARRUDA MONTEIRO",
  "FRANCISCO DE ALMEIDA LOBO",
  "GABRIEL LUIZ CRUZ DE SOUZA",
  "GUSTAVO TADEU VOLPATO",
  "IBRAIM FANTIN DA CRUZ",
  "JOANIS TILEMAHOS ZERVOUDAKIS",
  "JOSE EDUARDO DE AGUILAR SIQUEIRA DO NASCIMENTO",
  "LEANA OLIVEIRA FREITAS",
  "LEANDRO SCHLEMMER BRASIL",
  "LUCIANO DA SILVA CABRAL",
  "LUCIANO NAKAZATO",
  "MADILEINE FRANCELY AMERICO",
  "MARCELO LATTARULO CAMPOS",
  "MARCELO SACARDI BIUDES",
  "MARCIA QUEIROZ LATORRACA",
  "MARCOS ANTONIO SOARES",
  "MARIO SPEZZAPRIA",
  "MILTON FERREIRA DE MORAES",
  "NELSON LEITAO PAES",
  "NILCE VIEIRA CAMPOS FERREIRA",
  "RICHARD DE CAMPOS PACHECO",
  "ROBERTO LOPES DE SOUZA",
  "THIAGO JUNQUEIRA IZZO",
  "VALERIA DUTRA",
  "VALERIA REGIA FRANCO SOUSA",
  "VINICIUS CARVALHO PEREIRA"
]


periodicos = []
erros_xml  = []
resumo = [0, 0, 0, 0]

pq = 0

def corrigir_nome(nome, dicionario):
    if nome:
        res = []
        lstNomes = nome.split(' ')
        for pal in lstNomes:
            if pal in dicionario.keys():
                #print(f'    {pal} corrigido para {dicionario[pal]}')
                pal = dicionario[pal]
            res.append(pal)
        return ' '.join(res)
    else:
        return nome

def normalizar(texto):
    if texto:
        return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode().strip()
    return ''

def formata_isbn(isbn):
    if (len(isbn) == 13):
        isbn = f'{isbn[:3]}-{isbn[3]}-{isbn[4:6]}-{isbn[6:12]}-{isbn[12]}'
    elif (len(isbn) == 10):
        isbn = f'{isbn[:2]}-{isbn[2:5]}-{isbn[5:9]}-{isbn[9]}'
    
    return isbn

def obter_nivel_formacao(collection):
    formacoes = collection.getElementsByTagName("FORMACAO-ACADEMICA-TITULACAO")
    if not formacoes:
        return ""

    possui_doutorado = formacoes[0].getElementsByTagName("DOUTORADO")
    possui_mestrado = formacoes[0].getElementsByTagName("MESTRADO")
    possui_graduacao = formacoes[0].getElementsByTagName("GRADUACAO")

    if possui_doutorado:
        return "Doutorado"
    elif possui_mestrado:
        return "Mestrado"
    elif possui_graduacao:
        return "Graduacao"
    else:
        return "Nao informado"

def extrair_publicacoes(xml_path, anos_validos, file_name, pesquisador):
    global erros_xml
    global resumo
    global pq
    
    publicacoes = []
    try:
        try:
            DOMTree = parse(xml_path)
        except Exception as e:
            #print(f"Erro: XML Não reconhecido: {xml_path}")
            erros_xml.append(f'{file_name};XML Não reconhecido')
            resumo[3] = resumo[3] + 1
            return publicacoes
        
        collection = DOMTree.documentElement

        try:
            dados_gerais = collection.getElementsByTagName("DADOS-GERAIS")[0]
        except Exception as e:
            #print(f"Erro: Formato de curriculo não reconhecido: {xml_path}")
            erros_xml.append(f'{file_name};Formato de curriculo não reconhecido')
            resumo[3] = resumo[3] + 1
            return publicacoes

        nome = corrigir_nome(normalizar(dados_gerais.getAttribute("NOME-COMPLETO")), nomes)
        pesquisador.nome = nome
        
        titulacao = obter_nivel_formacao(collection)
        # Determinar categoria para resumo
        if titulacao == "Doutorado":
            resumo[2] = resumo[2] + 1
            pesquisador.doutorado = True
        elif titulacao == "Mestrado":
            resumo[1] = resumo[1] + 1
            pesquisador.mestrado = True
        else:
            resumo[0] = resumo[0] + 1

        # Bolsista PQ
        if (nome.upper() in bolsistaPQ):
            pesquisador.bolsistaPQ = True
            titulacao = titulacao + " (PQ)"
            pq += 1

        print("%s (%s)" % (nome, titulacao))

        # Artigos publicados
        for artigo in collection.getElementsByTagName("ARTIGO-PUBLICADO"):
            dados = artigo.getElementsByTagName('DADOS-BASICOS-DO-ARTIGO')[0]
            detalhe = artigo.getElementsByTagName('DETALHAMENTO-DO-ARTIGO')[0]
            ano = dados.getAttribute("ANO-DO-ARTIGO")
            if ano in anos_validos:
                issn = detalhe.getAttribute('ISSN')
                if (len(issn)==8):
                    issn = issn[:4] + '-' + issn[4:]

                per = normalizar(detalhe.getAttribute("TITULO-DO-PERIODICO-OU-REVISTA").upper())
                per = issn + ';' + corrigir_nome(per.replace('.', ' ').strip(), revistas)

                if (issn in jcr.jcr.keys()):
                    qualis = f'JCR:{jcr.jcr[issn][0]}'
                    pesquisador.avaliacao[ano].addJCR(1)
                elif (issn in jcr.eissn.keys()):
                    qualis = f'JCR:{jcr.eissn[issn][0]}'
                    pesquisador.avaliacao[ano].addJCR(1)
                elif (issn in rq.estratoQualis.keys()):
                    qualis = rq.estratoQualis[issn][1]
                    if (qualis == 'A1'):
                        pesquisador.avaliacao[ano].addA1(1)
                    elif (qualis == 'A2'):
                        pesquisador.avaliacao[ano].addA2(1)
                    elif (qualis == 'A3'):
                        pesquisador.avaliacao[ano].addA3(1)
                    elif (qualis == 'A4'):
                        pesquisador.avaliacao[ano].addA4(1)
                    elif (qualis == 'B1' or qualis == 'B2'):
                        pesquisador.avaliacao[ano].addB1B2(1)
                    elif (qualis == 'B3' or qualis == 'B4'):
                        pesquisador.avaliacao[ano].addB3B4(1)
                else:
                    qualis = ''
                    continue

                if ((len(qualis) > 0) and (qualis.upper()[0]=='C')):
                    continue
                linha = [
                    ano,
                    nome, titulacao,
                    dados.getAttribute("DOI"),
                    normalizar(dados.getAttribute("TITULO-DO-ARTIGO")),
                    'Periodico', qualis, '', 
                    per
                ]
                publicacoes.append(linha)

                if not (per in periodicos):
                    periodicos.append(per)

        # Livros publicados / organizados
        for livro in collection.getElementsByTagName("LIVRO-PUBLICADO-OU-ORGANIZADO"):
            dados = livro.getElementsByTagName('DADOS-BASICOS-DO-LIVRO')[0]
            detalhe = livro.getElementsByTagName('DETALHAMENTO-DO-LIVRO')[0]
            ano = dados.getAttribute("ANO")
            if ano in anos_validos:
                sTipo = dados.getAttribute("TIPO")
                if (sTipo == "LIVRO_PUBLICADO"):
                    tipo = "Publicado"
                    pesquisador.avaliacao[ano].addLivroTecnico(1)
                elif (sTipo == "LIVRO_ORGANIZADO_OU_EDICAO"):
                    tipo = "Organizado/Editado"
                    pesquisador.avaliacao[ano].addOrganizacaoLivro(1)
                else:
                    tipo = "Pub. N/Informada"
                    continue

                linha = [
                    ano,
                    nome, titulacao,
                    dados.getAttribute("DOI"),
                    normalizar(dados.getAttribute("TITULO-DO-LIVRO")),
                    f'Livro:{tipo}', formata_isbn(detalhe.getAttribute("ISBN")), '', ''
                ]
                publicacoes.append(linha)

        # Capítulos de livro
        livros = []
        for cap in collection.getElementsByTagName("CAPITULO-DE-LIVRO-PUBLICADO"):
            dados = cap.getElementsByTagName('DADOS-BASICOS-DO-CAPITULO')[0]
            detalhe = cap.getElementsByTagName('DETALHAMENTO-DO-CAPITULO')[0]
            ano = dados.getAttribute("ANO")
            isbn = formata_isbn(detalhe.getAttribute("ISBN"))
            livro = normalizar(detalhe.getAttribute("TITULO-DO-LIVRO"))
            if (len(isbn.strip())==0):
                if livro in livros:
                    continue
                livros.append(livro)
            else:
                if isbn in livros:
                    continue
                livros.append(isbn)
            if (livro[:6].upper() == "ANAIS "):
                continue

            if ano in anos_validos:
                pesquisador.avaliacao[ano].addCapituloLivro(1)
                
                linha = [
                    ano,
                    nome, titulacao,
                    dados.getAttribute("DOI"),
                    normalizar(dados.getAttribute("TITULO-DO-CAPITULO-DO-LIVRO")),
                    'Capitulo Livro', isbn, '',
                    livro
                ]
                publicacoes.append(linha)

        # Trabalhos em eventos
        for trabalho in collection.getElementsByTagName("TRABALHO-EM-EVENTOS"):
            dados = trabalho.getElementsByTagName('DADOS-BASICOS-DO-TRABALHO')[0]
            detalhe = trabalho.getElementsByTagName('DETALHAMENTO-DO-TRABALHO')[0]
            ano = dados.getAttribute("ANO-DO-TRABALHO")
            classificacao = normalizar(detalhe.getAttribute("CLASSIFICACAO-DO-EVENTO"))

            if ano in anos_validos:
                natureza = dados.getAttribute("NATUREZA")
                if (natureza == "COMPLETO"):
                    tipo = "Completo"
                else:
                    continue
                """
                elif (natureza  == "RESUMO"):
                    tipo = "Resumo"
                elif (natureza == "RESUMO_EXPANDIDO"):
                    tipo = "Resumo Expandido"
                else:
                    tipo = "N/Informado"
                """
                if (classificacao == "INTERNACIONAL"):
                    pesquisador.avaliacao[ano].addTrabalhoInternacional(1)
                elif (classificacao == "NACIONAL"):
                    pesquisador.avaliacao[ano].addTrabalhoNacional(1)
                else:
                    continue
                
                
                linha = [
                    ano,
                    nome, titulacao,
                    dados.getAttribute("DOI"),
                    normalizar(dados.getAttribute("TITULO-DO-TRABALHO")),
                    f"Congresso:{tipo}", formata_isbn(detalhe.getAttribute("ISBN")), 
                    classificacao, 
                    normalizar(detalhe.getAttribute("NOME-DO-EVENTO"))
                ]
                publicacoes.append(linha)

        # Organização de eventos / Curadoria
        for eve in collection.getElementsByTagName("ORGANIZACAO-DE-EVENTO"):
            dados = eve.getElementsByTagName('DADOS-BASICOS-DA-ORGANIZACAO-DE-EVENTO')[0]
            detalhe = eve.getElementsByTagName('DETALHAMENTO-DA-ORGANIZACAO-DE-EVENTO')[0]
            ano = dados.getAttribute("ANO")
            if ano in anos_validos:
                sTipo = dados.getAttribute("TIPO")
                natureza = dados.getAttribute("NATUREZA")
                if ((sTipo in ["FESTIVAL","CONCERTO","EXPOSICAO","CONCURSO"])):
                    if (natureza == "CURADORIA"):
                        pesquisador.avaliacao[ano].addCuradoria(1)
                    elif (natureza == "ORGANIZACAO"):
                        pesquisador.avaliacao[ano].addOrganizacaoFestival(1)
                    tipo = f"{sTipo}:{natureza.lower()}"
                elif ((sTipo == "CONGRESSO") and (natureza == "ORGANIZACAO")):
                    tipo = f"{sTipo}:{natureza.lower()}"
                    pesquisador.avaliacao[ano].addOrganizacaoEventos(1)
                else:
                    continue

                linha = [
                    ano,
                    nome, titulacao,
                    dados.getAttribute("DOI"),
                    normalizar(dados.getAttribute("TITULO")),
                    tipo, '', '', 
                    normalizar(dados.getAttribute("TITULO"))
                ]
                publicacoes.append(linha)

        # Traduções
        for prod in collection.getElementsByTagName("TRADUCAO"):
            dados = prod.getElementsByTagName('DADOS-BASICOS-DA-TRADUCAO')[0]
            detalhe = prod.getElementsByTagName('DETALHAMENTO-DA-TRADUCAO')[0]
            ano = dados.getAttribute("ANO")            
            if ano in anos_validos:
                natureza = dados.getAttribute("NATUREZA")
                if natureza == 'ARTIGO':
                    tipo = 'Artigo'
                    pesquisador.avaliacao[ano].addTraducaoArtigo(1)
                elif natureza == 'LIVRO':
                    pesquisador.avaliacao[ano].addTraducaoLivro(1)
                    tipo = 'Livro'
                else:
                    continue
                """
                elif natureza == 'OUTRO':
                    sTipo = 'Outro'
                else:
                    tipo = 'N/Informado'
                """

                linha = [
                    ano,
                    nome, titulacao,
                    detalhe.getAttribute("ISSN-ISBN"),
                    normalizar(dados.getAttribute("TITULO")),
                    f'Traducao:{tipo}', '', '', 
                    normalizar(detalhe.getAttribute("TITULO-DA-OBRA-ORIGINAL"))
                ]
                publicacoes.append(linha)
        
        # Producao Visual
        for prod in collection.getElementsByTagName("OBRA-DE-ARTES-VISUAIS"):
            dados = prod.getElementsByTagName('DADOS-BASICOS-DA-OBRA-DE-ARTES-VISUAIS')[0]
            detalhe = prod.getElementsByTagName('DETALHAMENTO-DA-OBRA-DE-ARTES-VISUAIS')[0]
            ano = dados.getAttribute("ANO")            
            if ano in anos_validos:
                natureza = dados.getAttribute("NATUREZA")
                if (natureza in ["CINEMA","FOTOGRAFIA","VIDEO","INSTALACAO","DESENHO","PINTURA","GRAVURA"]):
                    sTipo = dados.getAttribute("")

                pesquisador.avaliacao[ano].addProducaoVisual(1)

                linha = [
                    ano,
                    nome, titulacao, '',
                    normalizar(dados.getAttribute("TITULO")),
                    f'ProducaoVisual:{natureza}', '', '', 
                    normalizar(detalhe.getAttribute("LOCAL-DO-EVENTO"))
                ]
                publicacoes.append(linha)

        for prod in collection.getElementsByTagName("ARTES-VISUAIS"):
            dados = prod.getElementsByTagName('DADOS-BASICOS-DE-ARTES-VISUAIS')[0]
            detalhe = prod.getElementsByTagName('DETALHAMENTO-DE-ARTES-VISUAIS')[0]
            ano = dados.getAttribute("ANO")            
            if ano in anos_validos:
                natureza = dados.getAttribute("NATUREZA")
                if (natureza in ["CINEMA","FOTOGRAFIA","VIDEO","INSTALACAO","DESENHO","PINTURA","GRAVURA"]):
                    sTipo = dados.getAttribute("")
                
                pesquisador.avaliacao[ano].addProducaoVisual(1)

                linha = [
                    ano,
                    nome, titulacao, '',
                    normalizar(dados.getAttribute("TITULO")),
                    f'ProducaoVisual:{natureza}', '', '', 
                    normalizar(detalhe.getAttribute("LOCAL-DO-EVENTO"))
                ]
                publicacoes.append(linha)

        # Producao Musical
        for prod in collection.getElementsByTagName("MUSICA"):
            dados = prod.getElementsByTagName('DADOS-BASICOS-DA-MUSICA')[0]
            detalhe = prod.getElementsByTagName('DETALHAMENTO-DA-MUSICA')[0]
            ano = dados.getAttribute("ANO")            
            if ano in anos_validos:
                natureza = dados.getAttribute("NATUREZA")
                if (natureza in ["APRESENTACAO_DE_OBRA","COMPOSICAO","TRILHA_SONORA","INTERPRETACAO","PUBLICACAO_DE_PARTITURA","ARRANJO"]):
                    sTipo = dados.getAttribute("")

                pesquisador.avaliacao[ano].addProducaoMusical(1)

                linha = [
                    ano,
                    nome, titulacao, '',
                    normalizar(dados.getAttribute("TITULO")),
                    f'ProducaoMusical:{natureza}', '', '', 
                    normalizar(detalhe.getAttribute("TIPO-DE-EVENTO"))
                ]
                publicacoes.append(linha)

        # Producao Artes Cenicas
        for prod in collection.getElementsByTagName("ARTES-CENICAS"):
            dados = prod.getElementsByTagName('DADOS-BASICOS-DE-ARTES-CENICAS')[0]
            detalhe = prod.getElementsByTagName('DETALHAMENTO-DE-ARTES-CENICAS')[0]
            ano = dados.getAttribute("ANO")
            if ano in anos_validos:
                natureza = dados.getAttribute("NATUREZA")
                if (natureza in ["AUDIOVISUAL","PERFORMATICA","OPERISTICA","COREOGRAFICA","CIRCENSE","TEATRAL"]):
                    sTipo = dados.getAttribute("")

                pesquisador.avaliacao[ano].addArtesCenicas(1)

                linha = [
                    ano,
                    nome, titulacao, '',
                    normalizar(dados.getAttribute("TITULO")),
                    f'ProducaoMusical:{natureza}', '', '', 
                    normalizar(detalhe.getAttribute("TIPO-DE-EVENTO"))
                ]
                publicacoes.append(linha)

        # Registro ou Patente
        for reg in collection.getElementsByTagName("PRODUCAO-TECNICA"):
            # --- Software
            for sof in reg.getElementsByTagName("SOFTWARE"):
                dados = sof.getElementsByTagName("DADOS-BASICOS-DO-SOFTWARE")[0]
                detalhe = sof.getElementsByTagName("DETALHAMENTO-DO-SOFTWARE")[0]
                ano = dados.getAttribute("ANO")
                if ano in anos_validos:

                    pesquisador.avaliacao[ano].addProgramaComputador(1)

                    linha = [
                        ano,
                        nome, titulacao, '',
                        normalizar(dados.getAttribute("TITULO-DO-SOFTWARE")),
                        f'Software:{dados.getAttribute("NATUREZA")}', '', '', 
                        normalizar(dados.getAttribute("TITULO-DO-SOFTWARE"))
                    ]
                    publicacoes.append(linha)

            # --- Patente
            for pat in reg.getElementsByTagName("PATENTE"):
                dados = pat.getElementsByTagName("DADOS-BASICOS-DA-PATENTE")[0]
                detalhe = pat.getElementsByTagName("DETALHAMENTO-DA-PATENTE")[0]
                ano = dados.getAttribute("ANO-DESENVOLVIMENTO")
                if ano in anos_validos:

                    pesquisador.avaliacao[ano].addPatenteDepositada(1)

                    linha = [
                        ano,
                        nome, titulacao, '',
                        normalizar(dados.getAttribute("TITULO")),
                        'Patente', '', '', 
                        normalizar(dados.getAttribute("TITULO"))
                    ]
                    publicacoes.append(linha)

        # Material Didatico
        for material in collection.getElementsByTagName("DESENVOLVIMENTO-DE-MATERIAL-DIDATICO-OU-INSTRUCIONAL"):
            dados = material.getElementsByTagName('DADOS-BASICOS-DO-MATERIAL-DIDATICO-OU-INSTRUCIONAL')[0]
            detalhe = material.getElementsByTagName('DETALHAMENTO-DO-MATERIAL-DIDATICO-OU-INSTRUCIONAL')[0]
            ano = dados.getAttribute("ANO")
            if ano in anos_validos:
                pesquisador.avaliacao[ano].addMaterialDidatico(1)

                linha = [
                    ano,
                    nome, titulacao, '',
                    normalizar(dados.getAttribute("TITULO")),
                    'Material Didatico/Institucional', '', 
                    normalizar(dados.getAttribute("MEIO-DE-DIVULGACAO")), 
                    normalizar(detalhe.getAttribute("FINALIDADE"))
                ]
                publicacoes.append(linha)

        # Orientacoes concluidas Pós-Doutorado
        for orientacoes in collection.getElementsByTagName("ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO"):
            dados = orientacoes.getElementsByTagName('DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO')[0]
            detalhe = orientacoes.getElementsByTagName('DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO')[0]
            ano = dados.getAttribute("ANO")
            if ano in anos_validos:
                if (detalhe.getAttribute("TIPO-DE-ORIENTACAO") == "CO_ORIENTADOR"):
                    continue

                pesquisador.avaliacao[ano].addSupervisaoPosDoc(1)

                linha = [
                    ano,
                    nome, titulacao,
                    dados.getAttribute("DOI"),
                    normalizar(dados.getAttribute("TITULO")),
                    f'Pós-Doutorado:{detalhe.getAttribute("TIPO-DE-ORIENTACAO")}', '', '', 
                    normalizar(detalhe.getAttribute("NOME-DO-ORIENTADO"))
                ]
                publicacoes.append(linha)

        # Orientacoes concluidas Doutorado
        for orientacoes in collection.getElementsByTagName("ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO"):
            dados = orientacoes.getElementsByTagName('DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO')[0]
            detalhe = orientacoes.getElementsByTagName('DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO')[0]
            ano = dados.getAttribute("ANO")
            if ano in anos_validos:
                if (detalhe.getAttribute("TIPO-DE-ORIENTACAO") == "CO_ORIENTADOR"):
                    continue

                pesquisador.avaliacao[ano].addTeseDoutorado(1)
                linha = [
                    ano,
                    nome, titulacao,
                    dados.getAttribute("DOI"),
                    normalizar(dados.getAttribute("TITULO")),
                    f'Doutorado:{detalhe.getAttribute("TIPO-DE-ORIENTACAO")}', '', '', 
                    normalizar(detalhe.getAttribute("NOME-DO-ORIENTADO"))
                ]
                publicacoes.append(linha)

        # Orientacoes concluidas Mestrado
        for orientacoes in collection.getElementsByTagName("ORIENTACOES-CONCLUIDAS-PARA-MESTRADO"):
            dados = orientacoes.getElementsByTagName('DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO')[0]
            detalhe = orientacoes.getElementsByTagName('DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO')[0]
            ano = dados.getAttribute("ANO")
            if ano in anos_validos:
                if (detalhe.getAttribute("TIPO-DE-ORIENTACAO") == "CO_ORIENTADOR"):
                    continue

                pesquisador.avaliacao[ano].addDissertacaoMestrado(1)
                linha = [
                    ano,
                    nome, titulacao,
                    dados.getAttribute("DOI"),
                    normalizar(dados.getAttribute("TITULO")),
                    f'Mestrado:{detalhe.getAttribute("TIPO-DE-ORIENTACAO")}', '', '', 
                    normalizar(detalhe.getAttribute("NOME-DO-ORIENTADO"))
                ]
                publicacoes.append(linha)

        # Orientacoes concluidas Especializacao / TCC / Iniciacao Científica / Extensão
        for orientacoes in collection.getElementsByTagName("OUTRAS-ORIENTACOES-CONCLUIDAS"):
            dados = orientacoes.getElementsByTagName('DADOS-BASICOS-DE-OUTRAS-ORIENTACOES-CONCLUIDAS')[0]
            detalhe = orientacoes.getElementsByTagName('DETALHAMENTO-DE-OUTRAS-ORIENTACOES-CONCLUIDAS')[0]
            ano = dados.getAttribute("ANO")            
            if ano in anos_validos:
                natureza = dados.getAttribute("NATUREZA")
                if natureza == 'TRABALHO_DE_CONCLUSAO_DE_CURSO_GRADUACAO':
                    tipo = 'TCC'
                    pesquisador.avaliacao[ano].addTCCGraduacao(1)
                elif natureza == 'INICIACAO_CIENTIFICA':
                    tipo = 'IC'
                    pesquisador.avaliacao[ano].addIniciacaoCientifica(1)
                elif natureza == 'MONOGRAFIA_DE_CONCLUSAO_DE_CURSO_APERFEICOAMENTO_E_ESPECIALIZACAO':
                    tipo = 'Especializacao'
                    pesquisador.avaliacao[ano].addTCCEspecializacao(1)
                else:
                    continue
                """
                elif natureza == 'ORIENTACAO-DE-OUTRA-NATUREZA':
                    sTipo = dados.getAttribute("TIPO").upper()
                    if (sTipo[:7] == 'ORIENTA' and sTipo.find("PROJETO DE EXTENS") >= 0):
                        tipo = 'Extensão'
                        continue
                    else:
                        tipo = 'N/Informado'
                        continue
                else:
                    tipo = 'N/Informado'
                    continue
                """

                linha = [
                    ano,
                    nome, titulacao,
                    dados.getAttribute("DOI"),
                    normalizar(dados.getAttribute("TITULO")),
                    f'Orientacao:{tipo}', '', '', 
                    normalizar(detalhe.getAttribute("NOME-DO-ORIENTADO"))
                ]
                publicacoes.append(linha)


    except Exception as e:
        print(f"Erro: {e}")
        exit(-1)

    return publicacoes


def escreve_arquivo_area(pasta, publicacoes):
    with open(f'publicacoes-{pasta}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Ano', 'Nome', 'Titulacao', 'DOI', 'Titulo', 'Tipo', 'Qualis', 'Abrangencia', 'Nome Evento'])
        for pub in publicacoes:
            writer.writerow(pub)
    return

def escreve_sumario_area(pasta, lista):
    if (pasta != ""):
        print('=================================================')
        print(f'Resumo de "{pasta}"')
    else:
        print('\n\n=================================================')
        print("Resumo Geral")
    print(f'  Doutores: {lista[2]} curriculos')
    print(f'  Mestres.: {lista[1]} curriculos')
    print(f'  Outros..: {lista[0]} curriculos')
    print(f'  Erros...: {lista[3]} curriculos')

def escreve_erros_area(pasta, erros):
    if (len(erros)>0):
        with open(f'erros-{pasta}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(['Arquivo', 'Erro'])
            print('  Erros encontrados:')
            for erro in erros:
                lin = erro.split(';')
                writer.writerow([erro])
                print(f'    {lin[0]}: {lin[1]}')
    return

def escreve_arquivo_pontuacao(pasta, pontuacoes):
    with open(f'pontuacoes-{pasta}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['Nome', 'Pontos'])
        for pon in pontuacoes:
            writer.writerow(pon)
    return

def escreve_barema(arquivo, pesquisador):
    arquivo = f'{arquivo[:-4]}-barema.html'
    with open(arquivo, 'w', encoding='utf-8') as arq:
        arq.writelines(baremas.geraHTML(pesquisador))
        arq.close()
    return

# Seleciona arquivos XML de pastas e retorna uma lista de pastas e os respectivos arquivos XMLs para análise
def seleciona_XMLs_pastas(pasta_curriculos):
    lstPastas = []
    
    for root, folders, files in os.walk(pasta_curriculos):
        lstF = []
        for f in files:
            if f.lower().endswith('.xml'):
                lstF.append(f)
        
        if len(lstF)>0:
            lstPastas.append([root, lstF])
    return lstPastas

def main():
    global erros_xml
    global resumo
    global pq

    pasta_curriculos = 'curriculos'
    ano_fim = 2026
    ano_inicio = ano_fim - 5 # 3 anos anteriores
    anos_validos = [str(a) for a in range(ano_inicio, ano_fim)]

    resumo_total = resumo.copy()
    lstPastas = seleciona_XMLs_pastas(pasta_curriculos)
    for caminho, XMLs in lstPastas:
        pastas = caminho.split(os.sep)
        if len(pastas) > 1:
            pasta = pastas[-1]
        else:
            pasta = caminho
        print(f"\nLendo arquivo na pasta: {pasta} ({len(XMLs)} arquivos)")
        avaliacao = []
        todas_publicacoes = []

        for arqXML in XMLs:
            if (pasta.lower() == "letras linguistica"):
                pesquisador = baremas.PesquisadorA("", anos_validos)
            elif (pasta.lower() in ["humanas", "sociais aplicadas"]):
                pesquisador = baremas.PesquisadorH("", anos_validos)
            else:
                pesquisador = baremas.PesquisadorE("", anos_validos)

            caminho_xml = os.path.join(caminho, arqXML)
            publicacoes = extrair_publicacoes(caminho_xml, anos_validos, arqXML, pesquisador)
            todas_publicacoes.extend(publicacoes)
            avaliacao.append([pesquisador.nome, pesquisador.pontuacao_total()])
            escreve_barema(caminho_xml, pesquisador)
                                   
        escreve_arquivo_area(pasta, todas_publicacoes)
        escreve_sumario_area(pasta, resumo)
        escreve_erros_area(pasta, erros_xml)
        escreve_arquivo_pontuacao(pastas[0], avaliacao)
        erros_xml.clear()
        for r in range(len(resumo)):
            resumo_total[r] += resumo[r]
        resumo = [0, 0, 0, 0]

    escreve_sumario_area("", resumo_total)

    with open('periodicos.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(['ISSN', 'Periodico/Revista'])
        periodicos.sort()
        for per in periodicos:
            lin = per.split(';')
            writer.writerow(lin)

    print('\nTotal de PQs:', pq)


if __name__ == '__main__':
    main()
    print('')
