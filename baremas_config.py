"""
baremas_config.py — Motor de barema orientado a configuração.

Substitui as classes fixas AvaliacaoA/E/H e PesquisadorA/E/H de baremas.py
por versões genéricas que lêem pesos, limites e bônus de titulação
diretamente do arquivo config/barema.toml.

O arquivo config/barema.toml é carregado uma única vez na importação
deste módulo. Para usar um caminho diferente, chame
``recarregar_config(caminho)`` antes de criar qualquer objeto.

Compatibilidade: os objetos Pesquisador produzidos aqui expõem a mesma
interface que os de baremas.py (atributos de contagem, pontuacao_total(),
avaliacao[ano], etc.), de modo que a função geraHTML() de baremas.py
continua funcionando com eles se necessário.

Uso básico
----------
    import baremas_config as bc

    pesq = bc.criar_pesquisador("H", anos_validos)
    pesq.nome       = "Fulano de Tal"
    pesq.doutorado  = True
    pesq.bolsistaPQ = False

    pesq.avaliacao["2024"].addA1()
    pesq.avaliacao["2024"].addTeseDoutorado()

    print(pesq.pontuacao_total())
    html_linhas = bc.geraHTML(pesq)
"""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Dict, List, Optional


# ---------------------------------------------------------------------------
# Localização do config file
# ---------------------------------------------------------------------------
_CONFIG_PATH = Path(__file__).parent / "config" / "barema.toml"
_cfg: dict = {}


def recarregar_config(caminho: Optional[str | Path] = None) -> dict:
    """Lê (ou re-lê) o arquivo TOML e retorna o dicionário de configuração."""
    global _cfg, _CONFIG_PATH
    if caminho is not None:
        _CONFIG_PATH = Path(caminho)
    with open(_CONFIG_PATH, "rb") as f:
        _cfg = tomllib.load(f)
    return _cfg


def recarregar_config_dict(config_dict: dict) -> dict:
    """Carrega configuração a partir de um dicionário Python (sem ler arquivo).

    Útil para injetar configurações em memória (ex: vindas de formulário web)
    sem precisar escrever um arquivo TOML temporário.

    Nota: altera o estado global do módulo — não é thread-safe.
    Para uso em servidor multi-thread, considere refatorar para injeção
    de dependência no construtor de PesquisadorConfig.
    """
    global _cfg
    _cfg = config_dict
    return _cfg


def _get_cfg() -> dict:
    """Garante que o config já foi carregado."""
    if not _cfg:
        recarregar_config()
    return _cfg


# ---------------------------------------------------------------------------
# AvaliacaoConfig — equivalente a AvaliacaoA / AvaliacaoE / AvaliacaoH
# ---------------------------------------------------------------------------
_TODOS_OS_ITENS_G1 = [
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

_TODOS_OS_ITENS_G2 = [
    "tese_doutorado", "dissertacao_mestrado", "tcc_especializacao",
    "iniciacao_cientifica", "tcc_graduacao", "supervisao_pos_doc",
]


class AvaliacaoConfig:
    """
    Armazena contagens de produção para UM ano e calcula pontuação
    usando os pesos e limites vindos do barema.toml.
    """

    def __init__(self, pesos: Dict[str, int], limites: Dict[str, int]):
        self._pesos = pesos
        self._limites = limites  # {item: limite_máximo_global}, 0 = sem limite

        # Contadores — Grupo 1
        self.artigo_jcr: int = 0
        self.qualis_a1: int = 0
        self.qualis_a2: int = 0
        self.qualis_a3: int = 0
        self.qualis_a4: int = 0
        self.qualis_b1_b2: int = 0
        self.qualis_b3_b4: int = 0
        self.livro_tecnico: int = 0
        self.organizacao_edicao_livro: int = 0
        self.capitulo_livro: int = 0
        self.trabalhos_internacional: int = 0
        self.trabalhos_nacional: int = 0
        self.bolsista_pq: int = 0
        self.editor_internacional: int = 0
        self.editor_nacional: int = 0
        self.organizacao_eventos: int = 0
        self.traducao_livro: int = 0
        self.traducao_artigo: int = 0
        self.curadoria: int = 0
        self.organizacao_festival: int = 0
        self.producao_visual: int = 0
        self.producao_musical: int = 0
        self.artes_cenicas: int = 0
        self.programa_computador: int = 0
        self.patente_depositada: int = 0
        self.patente_concedida: int = 0
        self.patente_licenciada: int = 0
        self.material_didatico: int = 0

        # Contadores — Grupo 2
        self.tese_doutorado: int = 0
        self.dissertacao_mestrado: int = 0
        self.tcc_especializacao: int = 0
        self.iniciacao_cientifica: int = 0
        self.tcc_graduacao: int = 0
        self.supervisao_pos_doc: int = 0

    # ---- métodos add (mesma assinatura de baremas.py) ----------------------

    def addJCR(self, quantidade: int = 1):               self.artigo_jcr += quantidade
    def addA1(self, quantidade: int = 1):                self.qualis_a1 += quantidade
    def addA2(self, quantidade: int = 1):                self.qualis_a2 += quantidade
    def addA3(self, quantidade: int = 1):                self.qualis_a3 += quantidade
    def addA4(self, quantidade: int = 1):                self.qualis_a4 += quantidade
    def addB1B2(self, quantidade: int = 1):              self.qualis_b1_b2 += quantidade
    def addB3B4(self, quantidade: int = 1):              self.qualis_b3_b4 += quantidade
    def addLivroTecnico(self, quantidade: int = 1):      self.livro_tecnico += quantidade
    def addOrganizacaoLivro(self, quantidade: int = 1):  self.organizacao_edicao_livro += quantidade
    def addCapituloLivro(self, quantidade: int = 1):     self.capitulo_livro += quantidade
    def addTrabalhoInternacional(self, quantidade: int = 1): self.trabalhos_internacional += quantidade
    def addTrabalhoNacional(self, quantidade: int = 1):  self.trabalhos_nacional += quantidade
    def addBolsistaPQ(self, quantidade: int = 1):        self.bolsista_pq += quantidade
    def addEditorInternacional(self, quantidade: int = 1): self.editor_internacional += quantidade
    def addEditorNacional(self, quantidade: int = 1):    self.editor_nacional += quantidade
    def addOrganizacaoEventos(self, quantidade: int = 1): self.organizacao_eventos += quantidade
    def addTraducaoLivro(self, quantidade: int = 1):     self.traducao_livro += quantidade
    def addTraducaoArtigo(self, quantidade: int = 1):    self.traducao_artigo += quantidade
    def addCuradoria(self, quantidade: int = 1):         self.curadoria += quantidade
    def addOrganizacaoFestival(self, quantidade: int = 1): self.organizacao_festival += quantidade
    def addProducaoVisual(self, quantidade: int = 1):    self.producao_visual += quantidade
    def addProducaoMusical(self, quantidade: int = 1):   self.producao_musical += quantidade
    def addArtesCenicas(self, quantidade: int = 1):      self.artes_cenicas += quantidade
    def addProgramaComputador(self, quantidade: int = 1): self.programa_computador += quantidade
    def addPatenteDepositada(self, quantidade: int = 1): self.patente_depositada += quantidade
    def addPatenteConcedida(self, quantidade: int = 1):  self.patente_concedida += quantidade
    def addPatenteLicenciada(self, quantidade: int = 1): self.patente_licenciada += quantidade
    def addMaterialDidatico(self, quantidade: int = 1):  self.material_didatico += quantidade
    def addTeseDoutorado(self, quantidade: int = 1):     self.tese_doutorado += quantidade
    def addDissertacaoMestrado(self, quantidade: int = 1): self.dissertacao_mestrado += quantidade
    def addTCCEspecializacao(self, quantidade: int = 1): self.tcc_especializacao += quantidade
    def addIniciacaoCientifica(self, quantidade: int = 1): self.iniciacao_cientifica += quantidade
    def addTCCGraduacao(self, quantidade: int = 1):      self.tcc_graduacao += quantidade
    def addSupervisaoPosDoc(self, quantidade: int = 1):  self.supervisao_pos_doc += quantidade

    # ---- cálculo de pontuação ----------------------------------------------

    def calcular_pontuacao_item(self, item: str, quantidade: int) -> int:
        """Pontuação de um item: quantidade × peso, respeitando o limite global."""
        peso = self._pesos.get(item, 0)
        pontuacao = quantidade * peso
        limite = self._limites.get(item, 0)
        if limite > 0:
            pontuacao = min(pontuacao, limite)
        return pontuacao

    def calcular_grupo_1(self) -> int:
        return sum(
            self.calcular_pontuacao_item(item, getattr(self, item))
            for item in _TODOS_OS_ITENS_G1
        )

    def calcular_grupo_2(self) -> int:
        return sum(
            self.calcular_pontuacao_item(item, getattr(self, item))
            for item in _TODOS_OS_ITENS_G2
        )

    def calcular_pontuacao_total(self) -> int:
        return self.calcular_grupo_1() + self.calcular_grupo_2()


# ---------------------------------------------------------------------------
# PesquisadorConfig — equivalente a PesquisadorA / PesquisadorE / PesquisadorH
# ---------------------------------------------------------------------------

class PesquisadorConfig:
    """
    Representa um pesquisador avaliado com base num perfil do barema.toml.

    Atributos públicos
    ------------------
    nome        : str
    doutorado   : bool
    mestrado    : bool
    bolsistaPQ  : bool
    anos        : list[str]
    perfil      : str   — código do perfil (ex: "A", "E", "H")
    avaliacao   : dict[str, AvaliacaoConfig]  — um objeto por ano
    """

    def __init__(self, nome: str, anos: List[str], perfil: str):
        cfg = _get_cfg()

        if perfil not in cfg.get("perfis", {}):
            perfis_disponiveis = list(cfg.get("perfis", {}).keys())
            raise ValueError(
                f"Perfil '{perfil}' não encontrado em barema.toml. "
                f"Disponíveis: {perfis_disponiveis}"
            )

        self.nome: str = nome
        self.anos: List[str] = anos
        self.perfil: str = perfil
        self.doutorado: bool = False
        self.mestrado: bool = False
        self.bolsistaPQ: bool = False

        pesos = cfg["perfis"][perfil]["pesos"]
        limites = cfg.get("limites", {})

        self.avaliacao: Dict[str, AvaliacaoConfig] = {
            ano: AvaliacaoConfig(pesos, limites) for ano in anos
        }

    # ---- pontuação total ---------------------------------------------------

    def pontuacao_total(self) -> int:
        cfg = _get_cfg()
        pts_tit = cfg.get("titulacao", {})

        if self.doutorado:
            total = pts_tit.get("doutorado", 50)
        elif self.mestrado:
            total = pts_tit.get("mestrado", 30)
        else:
            total = 0

        if self.bolsistaPQ:
            total += pts_tit.get("bolsista_pq", 20)

        for ano in self.anos:
            total += self.avaliacao[ano].calcular_pontuacao_total()

        return total

    def pontuacao_por_ano(self) -> List[int]:
        return [self.avaliacao[ano].calcular_pontuacao_total() for ano in self.anos]


# ---------------------------------------------------------------------------
# Funções auxiliares (mesma interface de baremas.py)
# ---------------------------------------------------------------------------

def criar_pesquisador(perfil: str, anos: List[str], nome: str = "") -> PesquisadorConfig:
    """
    Cria um PesquisadorConfig para o perfil e anos informados.

    Parâmetros
    ----------
    perfil : código do perfil definido em barema.toml (ex: "A", "E", "H")
    anos   : lista de strings de anos (ex: ["2021", "2022", "2023"])
    nome   : nome do pesquisador (pode ser definido depois)
    """
    return PesquisadorConfig(nome, anos, perfil)


def anos_validos_do_config() -> List[str]:
    """Retorna a lista de anos avaliados conforme [geral] do barema.toml."""
    cfg = _get_cfg()
    geral = cfg.get("geral", {})
    ano_fim = geral.get("ano_fim", 2026)
    janela = geral.get("janela", 5)
    return [str(a) for a in range(ano_fim - janela, ano_fim)]


def perfis_disponiveis() -> List[str]:
    """Retorna os códigos de perfil definidos no barema.toml."""
    return list(_get_cfg().get("perfis", {}).keys())


def nome_perfil(perfil: str) -> str:
    """Retorna o nome descritivo do perfil (campo 'nome' no TOML)."""
    cfg = _get_cfg()
    return cfg.get("perfis", {}).get(perfil, {}).get("nome", perfil)


# ---------------------------------------------------------------------------
# Funções de suporte ao HTML (mesma assinatura de baremas.py)
# ---------------------------------------------------------------------------

def _ponto_item(pesq: PesquisadorConfig, idx_ano: int, item: str) -> int:
    """Pontuação de um item em um ano específico (por índice)."""
    ava = pesq.avaliacao[pesq.anos[idx_ano]]
    return ava.calcular_pontuacao_item(item, getattr(ava, item))


def _pontos_g1_ano(pesq: PesquisadorConfig, idx_ano: int) -> int:
    return pesq.avaliacao[pesq.anos[idx_ano]].calcular_grupo_1()


def _pontos_g2_ano(pesq: PesquisadorConfig, idx_ano: int) -> int:
    return pesq.avaliacao[pesq.anos[idx_ano]].calcular_grupo_2()


def _peso_do_item(pesq: PesquisadorConfig, item: str) -> int:
    """Retorna o peso configurado de um item para o perfil do pesquisador."""
    cfg = _get_cfg()
    return cfg["perfis"][pesq.perfil]["pesos"].get(item, 0)


# ---------------------------------------------------------------------------
# Geração do HTML
# ---------------------------------------------------------------------------

def geraHTML(p: PesquisadorConfig) -> List[str]:
    """
    Gera o relatório HTML de barema para o pesquisador.

    Retorna uma lista de strings (igual à interface de baremas.geraHTML).
    As linhas da tabela são geradas dinamicamente: apenas itens com peso > 0
    no perfil do pesquisador aparecem no relatório.
    """
    cfg = _get_cfg()
    pts_tit = cfg.get("titulacao", {})

    # Titulação
    if p.doutorado:
        tit = pts_tit.get("doutorado", 50)
    elif p.mestrado:
        tit = pts_tit.get("mestrado", 30)
    else:
        tit = 0

    n = len(p.anos)

    # Rótulos legíveis para cada item de produção
    rotulos: Dict[str, str] = {
        "artigo_jcr":               "Artigo indexado com JCR",
        "qualis_a1":                "Periódico Qualis A1",
        "qualis_a2":                "Periódico Qualis A2",
        "qualis_a3":                "Periódico Qualis A3",
        "qualis_a4":                "Periódico Qualis A4",
        "qualis_b1_b2":             "Periódico Qualis B1 e B2",
        "qualis_b3_b4":             "Periódico Qualis B3 e B4",
        "livro_tecnico":            "Publicação de Livro Técnico-Científico (como autor)",
        "organizacao_edicao_livro": "Organização ou Edição de livro com ISBN (exceto anais)",
        "capitulo_livro":           "Capítulo de Livro (máximo 1 por livro)",
        "trabalhos_internacional":  "Trabalhos completos em anais com ISSN — Internacional (máx. 4/ano)",
        "trabalhos_nacional":       "Trabalhos completos em anais com ISSN — Nacional (máx. 4/ano)",
        "bolsista_pq":              "Atuação como Bolsista de Produtividade CNPq (PQ/DT)",
        "editor_internacional":     "Editor/a de periódico científico com ISSN internacional",
        "editor_nacional":          "Editor/a de periódico científico com ISSN nacional",
        "organizacao_eventos":      "Organização de eventos técnico-científicos",
        "traducao_livro":           "Tradução integral de livro técnico-científico com ISBN",
        "traducao_artigo":          "Tradução de artigo científico",
        "curadoria":                "Curadoria de festival, concerto, exposição ou concurso",
        "organizacao_festival":     "Organização de festival, concerto, exposição ou concurso",
        "producao_visual":          "Produção Visual (filme, fotografia, vídeo, instalação, pintura...)",
        "producao_musical":         "Produção Musical (composição, arranjo, partitura, interpretação...)",
        "artes_cenicas":            "Artes Cênicas (teatral, operística, coreográfica, circense...)",
        "programa_computador":      "Programa de computador registrado",
        "patente_depositada":       "Patente depositada no INPI",
        "patente_concedida":        "Patente concedida no INPI",
        "patente_licenciada":       "Patente licenciada",
        "material_didatico":        "Produção de material didático/instrucional",
        # Grupo 2
        "tese_doutorado":           "Tese de doutorado orientada e defendida",
        "dissertacao_mestrado":     "Dissertação de Mestrado orientada e defendida",
        "tcc_especializacao":       "TCC/Monografia de especialização lato sensu (máx. 3/ano)",
        "iniciacao_cientifica":     "Orientação de Iniciação Científica concluída",
        "tcc_graduacao":            "TCC/Monografia de graduação orientada e defendida (máx. 5/ano)",
        "supervisao_pos_doc":       "Supervisão de pós-doutorado",
    }

    def _linha_item(item: str) -> List[str]:
        """Gera as tags <tr>...</tr> de um item, por ano + subtotal."""
        peso = _peso_do_item(p, item)
        lst = [_ponto_item(p, i, item) for i in range(n)]
        linhas = [
            "                <tr>",
            f"                    <td>{rotulos.get(item, item)}</td>",
            f'                    <td class="points-column">{peso}</td>',
        ]
        for v in lst:
            linhas.append(f'                    <td class="year-column">{v}</td>')
        linhas.append(f'                    <td class="points-column">{sum(lst)}</td>')
        linhas.append("                </tr>")
        return linhas

    def _linha_subtotal(label: str, fn_pts) -> List[str]:
        lst = [fn_pts(p, i) for i in range(n)]
        linhas = [
            '                <tr class="subtotal-row">',
            f"                    <td><strong>{label}</strong></td>",
            '                    <td class="points-column"></td>',
        ]
        for v in lst:
            linhas.append(f'                    <td class="year-column">{v}</td>')
        linhas.append(f'                    <td class="points-column">{sum(lst)}</td>')
        linhas.append("                </tr>")
        return linhas

    def _cabecalho_tabela(titulo: str) -> List[str]:
        cols_ano = "".join(
            f'\n                    <th class="year-column">{ano}</th>'
            for ano in p.anos
        )
        return [
            "        <table>",
            "            <thead>",
            "                <tr>",
            f"                    <th>{titulo}</th>",
            '                    <th class="points-column">Pontuação</th>',
            cols_ano,
            '                    <th class="points-column">Subtotal</th>',
            "                </tr>",
            "            </thead>",
            "            <tbody>",
        ]

    # ---------- montagem do HTML ----------
    s: List[str] = []

    # cabeçalho HTML
    s += [
        "<!DOCTYPE html>",
        '<html lang="pt-BR">',
        "<head>",
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        f"    <title>Avaliação de {p.nome}</title>",
        "    <style>",
        "        body { font-family: Arial, sans-serif; margin: 20px; line-height: 1.1; font-size: 10px; }",
        "        .container { max-width: 1200px; margin: 0 auto; }",
        "        h3 { color: #333; text-align: center; margin-bottom: 10px; }",
        "        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,.1); }",
        "        th, td { border: 1px solid #ddd; padding: 6px; text-align: left; }",
        "        th { background-color: #f8f9fa; font-weight: bold; }",
        "        .points-column { text-align: center; width: 58px; padding: 3px; }",
        "        .points-double-column { text-align: center; width: 135px; padding: 3px; }",
        "        .year-column { text-align: center; width: 40px; padding: 3px; }",
        "        .subtotal-row { background-color: #f8f9fa; font-weight: bold; }",
        "        .footer-note { font-style: italic; margin-top: 20px; text-align: center; color: #666; }",
        "        .perfil-badge { background:#e9ecef; border-radius:4px; padding:2px 8px; font-size:9px; }",
        "    </style>",
        "</head>",
        "<body>",
        '    <div class="container">',
        f'        <h3>Avaliação de {p.nome} <span class="perfil-badge">Perfil {p.perfil} — {nome_perfil(p.perfil)}</span></h3>',
    ]

    # --- Tabela 1: Formação Acadêmica ---
    s += [
        "",
        "        <!-- Formação Acadêmica -->",
        "        <table>",
        "            <thead><tr>",
        "                <th>Formação Acadêmica</th>",
        '                <th class="points-column">Pontuação</th>',
        '                <th class="points-double-column">Pontuação Indicada</th>',
        '                <th class="points-column">Subtotal</th>',
        "            </tr></thead>",
        "            <tbody>",
        "                <tr>",
        f"                    <td>Titulação Máxima (mestrado = {pts_tit.get('mestrado',30)}; doutorado = {pts_tit.get('doutorado',50)})</td>",
        f'                    <td class="points-column">{pts_tit.get("mestrado",30)} ou {pts_tit.get("doutorado",50)}</td>',
        f'                    <td class="points-double-column">{tit}</td>',
        f'                    <td class="points-column">{tit}</td>',
        "                </tr>",
        "            </tbody>",
        "        </table>",
    ]

    # --- Tabela 2: Produção Técnica, Científica e de Inovação ---
    s += ["", "        <!-- Produção Técnica, Científica e de Inovação -->"]
    s += _cabecalho_tabela("Produção Técnica, Científica e de Inovação")

    for item in _TODOS_OS_ITENS_G1:
        if _peso_do_item(p, item) > 0:
            s += _linha_item(item)

    s += _linha_subtotal("Subtotal da Produção Técnica, Científica e de Inovação", _pontos_g1_ano)
    s += ["            </tbody>", "        </table>"]

    # --- Tabela 3: Formação de Recursos Humanos ---
    s += ["", "        <!-- Formação de Recursos Humanos em Pesquisa -->"]
    s += _cabecalho_tabela("Formação de Recursos Humanos em Pesquisa")

    for item in _TODOS_OS_ITENS_G2:
        if _peso_do_item(p, item) > 0:
            s += _linha_item(item)

    s += _linha_subtotal("Subtotal da Formação de Recursos Humanos em Pesquisa", _pontos_g2_ano)
    s += ["            </tbody>", "        </table>"]

    # --- Tabela 4: Resumo Final ---
    cols_ano_total = "".join(
        f'\n                    <th class="year-column">{ano}</th>'
        for ano in p.anos
    )
    s += [
        "",
        "        <!-- Resumo Final -->",
        "        <table>",
        "            <thead><tr>",
        "                <th>Planilha atualizada pela PROPESQ</th>",
        '                <th class="points-column">Titulação</th>',
        cols_ano_total,
        '                <th class="points-column">Total</th>',
        "            </tr></thead>",
        "            <tbody><tr>",
        "                <td></td>",
        f'                <td class="points-column">{tit}</td>',
    ]
    for i in range(n):
        s.append(f'                <td class="year-column">{_pontos_g1_ano(p,i)+_pontos_g2_ano(p,i)}</td>')
    s += [
        f'                <td class="points-column">{p.pontuacao_total()}</td>',
        "            </tr></tbody>",
        "        </table>",
        "",
        '        <div class="footer-note"><em>Gerado por baremas_config.py — configuração em barema.toml</em></div>',
        "    </div>",
        "</body>",
        "</html>",
    ]

    return s

