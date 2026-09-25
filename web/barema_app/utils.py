"""
utils.py — Ponte entre a app Django e os módulos existentes do projeto Lattes.

Funções para:
- Converter XML Lattes → JSON (via xsdata)
- Carregar o barema.toml padrão
- Executar o cálculo do barema em memória
- Constantes (rótulos, listas de itens) usadas pelas views e templates
"""
from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuração de paths — garante que os módulos raiz são importáveis
# ---------------------------------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parents[2]          # lattes/
_DEFINITIONS_DIR = ROOT_DIR / "definitions" / "curriculo_lattes"

for _p in (str(ROOT_DIR), str(_DEFINITIONS_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import baremas_config as bc   # noqa: E402
import json_barema as jb      # noqa: E402


# ---------------------------------------------------------------------------
# Listas de itens de produção (Grupo 1 e Grupo 2)
# ---------------------------------------------------------------------------
ITENS_G1 = [
    "artigo_jcr", "qualis_a1", "qualis_a2", "qualis_a3", "qualis_a4",
    "qualis_b1_b2", "qualis_b3_b4", "livro_tecnico", "organizacao_edicao_livro",
    "capitulo_livro", "trabalhos_internacional", "trabalhos_nacional",
    "bolsista_pq", "editor_internacional", "editor_nacional",
    "organizacao_eventos", "traducao_livro", "traducao_artigo",
    "curadoria", "organizacao_festival", "producao_visual",
    "producao_musical", "artes_cenicas", "programa_computador",
    "patente_depositada", "patente_concedida", "patente_licenciada",
    "material_didatico",
]

ITENS_G2 = [
    "tese_doutorado", "dissertacao_mestrado", "tcc_especializacao",
    "iniciacao_cientifica", "tcc_graduacao", "supervisao_pos_doc",
]


# ---------------------------------------------------------------------------
# Rótulos legíveis para cada item
# ---------------------------------------------------------------------------
ROTULOS: dict[str, str] = {
    "artigo_jcr":               "Artigo indexado com JCR",
    "qualis_a1":                "Periódico Qualis A1",
    "qualis_a2":                "Periódico Qualis A2",
    "qualis_a3":                "Periódico Qualis A3",
    "qualis_a4":                "Periódico Qualis A4",
    "qualis_b1_b2":             "Periódico Qualis B1 / B2",
    "qualis_b3_b4":             "Periódico Qualis B3 / B4",
    "livro_tecnico":            "Publicação de Livro Técnico-Científico (autor)",
    "organizacao_edicao_livro": "Organização / Edição de livro com ISBN",
    "capitulo_livro":           "Capítulo de Livro (máx. 1 por livro)",
    "trabalhos_internacional":  "Trabalhos em anais — Internacional",
    "trabalhos_nacional":       "Trabalhos em anais — Nacional",
    "bolsista_pq":              "Bolsista PQ/DT CNPq (por ano)",
    "editor_internacional":     "Editor de periódico internacional",
    "editor_nacional":          "Editor de periódico nacional",
    "organizacao_eventos":      "Organização de eventos técnico-científicos",
    "traducao_livro":           "Tradução integral de livro com ISBN",
    "traducao_artigo":          "Tradução de artigo científico",
    "curadoria":                "Curadoria (festival, concerto, exposição…)",
    "organizacao_festival":     "Organização de festival / concerto / exposição",
    "producao_visual":          "Produção Visual (filme, foto, vídeo…)",
    "producao_musical":         "Produção Musical (composição, arranjo…)",
    "artes_cenicas":            "Artes Cênicas (teatro, ópera, circo…)",
    "programa_computador":      "Programa de computador registrado",
    "patente_depositada":       "Patente depositada no INPI",
    "patente_concedida":        "Patente concedida no INPI",
    "patente_licenciada":       "Patente licenciada",
    "material_didatico":        "Material didático / instrucional",
    # Grupo 2
    "tese_doutorado":           "Tese de doutorado orientada e defendida",
    "dissertacao_mestrado":     "Dissertação de Mestrado orientada e defendida",
    "tcc_especializacao":       "TCC / Monografia de Especialização (lato sensu)",
    "iniciacao_cientifica":     "Orientação de Iniciação Científica concluída",
    "tcc_graduacao":            "TCC / Monografia de Graduação",
    "supervisao_pos_doc":       "Supervisão de pós-doutorado",
}


# ---------------------------------------------------------------------------
# Funções de conversão e cálculo
# ---------------------------------------------------------------------------

def converter_xml_para_json(xml_bytes: bytes) -> dict:
    """Converte XML do Lattes (bytes) para dict JSON usando xsdata."""
    from xsdata.formats.dataclass.parsers import XmlParser
    from xsdata.formats.dataclass.serializers import JsonSerializer
    from curriculo_model import CurriculoVitae

    parser = XmlParser()
    serializer = JsonSerializer()

    curriculo_obj = parser.from_bytes(xml_bytes, CurriculoVitae)
    json_str = serializer.render(curriculo_obj)
    return json.loads(json_str)


def carregar_config_padrao() -> dict:
    """Lê o barema.toml padrão e retorna como dict Python."""
    config_path = ROOT_DIR / "config" / "barema.toml"
    with open(config_path, "rb") as f:
        return tomllib.load(f)


def calcular_barema_em_memoria(
    json_data: dict,
    perfil: str,
    config_dict: dict,
    anos: list[str] | None = None,
) -> tuple[bc.PesquisadorConfig, str]:
    """
    Executa o cálculo do barema inteiramente em memória.

    Parâmetros
    ----------
    json_data   : dados do currículo Lattes (dict parsed do JSON)
    perfil      : código do perfil (ex: "A", "E", "H")
    config_dict : configuração do barema (mesmo formato do barema.toml parsed)
    anos        : lista de anos a avaliar (None = calcula do config)

    Retorna
    -------
    (pesquisador, html_string) — o PesquisadorConfig preenchido e o HTML do relatório.
    """
    # Injeta a configuração customizada no motor
    bc.recarregar_config_dict(config_dict)

    if anos is None:
        geral = config_dict.get("geral", {})
        ano_fim = geral.get("ano_fim", 2026)
        janela = geral.get("janela", 5)
        anos = [str(a) for a in range(ano_fim - janela, ano_fim)]

    # Cria o pesquisador e preenche com dados do currículo
    pesquisador = bc.criar_pesquisador(perfil, anos)
    jb.populate_researcher(json_data, pesquisador, anos)

    # Gera HTML
    html_lines = bc.geraHTML(pesquisador)
    html_string = "\n".join(html_lines)

    return pesquisador, html_string
