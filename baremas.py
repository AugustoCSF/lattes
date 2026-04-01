from abc import ABC, abstractmethod
from typing import Dict, Any

class AvaliacaoAcademica(ABC):
    """Classe base para avaliação acadêmica"""
    
    def __init__(self):
        # Grupo 1 - Produção Científica
        self.artigo_jcr = 0
        self.qualis_a1 = 0
        self.qualis_a2 = 0
        self.qualis_a3 = 0
        self.qualis_a4 = 0
        self.qualis_b1_b2 = 0
        self.qualis_b3_b4 = 0
        self.livro_tecnico = 0
        self.organizacao_edicao_livro = 0
        self.capitulo_livro = 0
        self.trabalhos_internacional = 0
        self.trabalhos_nacional = 0
        self.bolsista_pq = 0
        self.editor_internacional = 0
        self.editor_nacional = 0
        self.organizacao_eventos = 0
        self.traducao_livro = 0
        self.traducao_artigo = 0
        self.curadoria = 0
        self.organizacao_festival = 0
        self.producao_visual = 0
        self.producao_musical = 0
        self.artes_cenicas = 0
        self.programa_computador = 0
        self.patente_depositada = 0
        self.patente_concedida = 0
        self.patente_licenciada = 0
        self.material_didatico = 0
        
        # Grupo 2 - Orientações
        self.tese_doutorado = 0
        self.dissertacao_mestrado = 0
        self.tcc_especializacao = 0
        self.iniciacao_cientifica = 0
        self.tcc_graduacao = 0
        self.supervisao_pos_doc = 0

    # Métodos para adicionar +1 em cada atributo - Grupo 1
    def addJCR(self, quantidade=1):
        """Adiciona artigos indexados com JCR"""
        self.artigo_jcr += quantidade
    
    def addA1(self, quantidade=1):
        """Adiciona periódicos Qualis A1"""
        self.qualis_a1 += quantidade
    
    def addA2(self, quantidade=1):
        """Adiciona periódicos Qualis A2"""
        self.qualis_a2 += quantidade
    
    def addA3(self, quantidade=1):
        """Adiciona periódicos Qualis A3"""
        self.qualis_a3 += quantidade
    
    def addA4(self, quantidade=1):
        """Adiciona periódicos Qualis A4"""
        self.qualis_a4 += quantidade
    
    def addB1B2(self, quantidade=1):
        """Adiciona periódicos Qualis B1 e B2"""
        self.qualis_b1_b2 += quantidade
    
    def addB3B4(self, quantidade=1):
        """Adiciona periódicos Qualis B3 e B4"""
        self.qualis_b3_b4 += quantidade
    
    def addLivroTecnico(self, quantidade=1):
        """Adiciona publicação de livro técnico-científico"""
        self.livro_tecnico += quantidade
    
    def addOrganizacaoLivro(self, quantidade=1):
        """Adiciona organização ou edição de livro com ISBN"""
        self.organizacao_edicao_livro += quantidade
    
    def addCapituloLivro(self, quantidade=1):
        """Adiciona capítulo de livro"""
        self.capitulo_livro += quantidade
    
    def addTrabalhoInternacional(self, quantidade=1):
        """Adiciona trabalho completo internacional"""
        self.trabalhos_internacional += quantidade
    
    def addTrabalhoNacional(self, quantidade=1):
        """Adiciona trabalho completo nacional"""
        self.trabalhos_nacional += quantidade
    
    def addBolsistaPQ(self, quantidade=1):
        """Adiciona atuação como bolsista PQ"""
        self.bolsista_pq += quantidade
    
    def addEditorInternacional(self, quantidade=1):
        """Adiciona atuação como editor internacional"""
        self.editor_internacional += quantidade
    
    def addEditorNacional(self, quantidade=1):
        """Adiciona atuação como editor nacional"""
        self.editor_nacional += quantidade
    
    def addOrganizacaoEventos(self, quantidade=1):
        """Adiciona organização de eventos"""
        self.organizacao_eventos += quantidade
    
    def addTraducaoLivro(self, quantidade=1):
        """Adiciona tradução de livro"""
        self.traducao_livro += quantidade
    
    def addTraducaoArtigo(self, quantidade=1):
        """Adiciona tradução de artigo"""
        self.traducao_artigo += quantidade
    
    def addCuradoria(self, quantidade=1):
        """Adiciona curadoria"""
        self.curadoria += quantidade
    
    def addOrganizacaoFestival(self, quantidade=1):
        """Adiciona organização de festival"""
        self.organizacao_festival += quantidade
    
    def addProducaoVisual(self, quantidade=1):
        """Adiciona produção visual"""
        self.producao_visual += quantidade
    
    def addProducaoMusical(self, quantidade=1):
        """Adiciona produção musical"""
        self.producao_musical += quantidade
    
    def addArtesCenicas(self, quantidade=1):
        """Adiciona artes cênicas"""
        self.artes_cenicas += quantidade
    
    def addProgramaComputador(self, quantidade=1):
        """Adiciona programa computador"""
        self.programa_computador += quantidade

    def addPatenteDepositada(self, quantidade=1):
        """Adiciona patente depositada"""
        self.patente_depositada += quantidade

    def addPatenteConcedida(self, quantidade=1):
        """Adiciona patende concedida"""
        self.patente_concedida += quantidade

    def addPatenteLicenciada(self, quantidade=1):
        """Adiciona patente licenciada"""
        self.patente_licenciada += quantidade

    def addMaterialDidatico(self, quantidade=1):
        """Adiciona material didatico"""
        self.material_didatico += quantidade

    # Métodos para Grupo 2 (Orientações) - apenas adiciona 1
    def addTeseDoutorado(self, quantidade=1):
        """Adiciona 1 tese de doutorado ao ano especificado"""
        self.tese_doutorado += quantidade
    
    def addDissertacaoMestrado(self, quantidade=1):
        """Adiciona 1 dissertação de mestrado ao ano especificado"""
        self.dissertacao_mestrado += quantidade
    
    def addTCCEspecializacao(self, quantidade=1):
        """Adiciona 1 TCC de especialização ao ano especificado"""
        self.tcc_especializacao += quantidade
    
    def addIniciacaoCientifica(self, quantidade=1):
        """Adiciona 1 orientação de iniciação científica ao ano especificado"""
        self.iniciacao_cientifica += quantidade
    
    def addTCCGraduacao(self, quantidade=1):
        """Adiciona 1 TCC de graduação ao ano especificado"""
        self.tcc_graduacao += quantidade
    
    def addSupervisaoPosDoc(self, quantidade=1):
        """Adiciona 1 supervisão de pós-doutorado ao ano especificado"""
        self.supervisao_pos_doc += quantidade
    

    @abstractmethod
    def get_pesos(self) -> Dict[str, int]:
        """Retorna o dicionário com pesos para cada atributo"""
        pass
    
    def get_pontuacao_maxima(self) -> Dict[str, int]:
        """Retorna o dicionário com pontuação máxima apenas para os 4 atributos que têm limite"""
        return {
            'trabalhos_internacional': 16,  # máximo 4 por ano × 4 pontos
            'trabalhos_nacional': 8,        # máximo 4 por ano × 2 pontos
            'tcc_especializacao': 6,        # máximo 3 por ano × 2 pontos
            'tcc_graduacao': 5              # máximo 5 por ano × 1 ponto
        }
    
    def calcular_pontuacao_item(self, item: str, quantidade: int) -> int:
        """Calcula a pontuação de um item específico"""
        pesos = self.get_pesos()
        
        if item not in pesos:
            return 0
        
        pontuacao_calculada = quantidade * pesos[item]
        
        # Aplica limite máximo apenas para os 4 atributos que possuem
        pontuacao_maxima = self.get_pontuacao_maxima()
        if item in pontuacao_maxima:
            return min(pontuacao_calculada, pontuacao_maxima[item])
        
        return pontuacao_calculada
    
    def calcular_grupo_1(self) -> int:
        """Calcula pontuação total do Grupo 1"""
        itens_grupo_1 = [
            'artigo_jcr', 'qualis_a1', 'qualis_a2', 'qualis_a3', 'qualis_a4',
            'qualis_b1_b2', 'qualis_b3_b4', 'livro_tecnico', 'organizacao_edicao_livro',
            'capitulo_livro', 'trabalhos_internacional', 'trabalhos_nacional',
            'bolsista_pq', 'editor_internacional', 'editor_nacional',
            'organizacao_eventos', 'traducao_livro', 'traducao_artigo',
            'curadoria', 'organizacao_festival', 'producao_visual',
            'producao_musical', 'artes_cenicas', 'programa_computador',
            'patente_depositada', 'patente_concedida', 'patente_licenciada',
            'material_didatico'
        ]
        
        total = 0
        for item in itens_grupo_1:
            quantidade = getattr(self, item)
            total += self.calcular_pontuacao_item(item, quantidade)
        
        return total
    
    def calcular_grupo_2(self) -> int:
        """Calcula pontuação total do Grupo 2"""
        itens_grupo_2 = [
            'tese_doutorado', 'dissertacao_mestrado', 'tcc_especializacao',
            'iniciacao_cientifica', 'tcc_graduacao', 'supervisao_pos_doc'
        ]
        
        total = 0
        for item in itens_grupo_2:
            quantidade = getattr(self, item)
            total += self.calcular_pontuacao_item(item, quantidade)
        
        return total
    
    def calcular_pontuacao_total(self) -> int:
        """Calcula pontuação total (Grupo 1 + Grupo 2)"""
        return self.calcular_grupo_1() + self.calcular_grupo_2()
    

class AvaliacaoA(AvaliacaoAcademica):
    """Especialização para avaliação tipo A"""
    
    def get_pesos(self) -> Dict[str, int]:
        return {
            'artigo_jcr': 10,
            'qualis_a1': 10,
            'qualis_a2': 8,
            'qualis_a3': 6,
            'qualis_a4': 4,
            'qualis_b1_b2': 2,
            'qualis_b3_b4': 1,
            'livro_tecnico': 10,
            'organizacao_edicao_livro': 5,
            'capitulo_livro': 5,
            'trabalhos_internacional': 4,
            'trabalhos_nacional': 2,
            'bolsista_pq': 20,
            'editor_internacional': 5,
            'editor_nacional': 3,
            'organizacao_eventos': 3,
            'traducao_livro': 0,
            'traducao_artigo': 0,
            'curadoria': 0,
            'organizacao_festival': 0,
            'producao_visual': 0,
            'producao_musical': 0,
            'artes_cenicas': 0,
            'programa_computador': 0,
            'patente_depositada': 0,
            'patente_concedida': 0,
            'patente_licenciada': 0,
            'material_didatico': 3,
            'tese_doutorado': 15,
            'dissertacao_mestrado': 10,
            'tcc_especializacao': 2,
            'iniciacao_cientifica': 5,
            'tcc_graduacao': 1,
            'supervisao_pos_doc': 10
        }


class AvaliacaoE(AvaliacaoAcademica):
    """Especialização para avaliação tipo E"""
    
    def get_pesos(self) -> Dict[str, int]:
        return {
            'artigo_jcr': 10,
            'qualis_a1': 10,
            'qualis_a2': 8,
            'qualis_a3': 6,
            'qualis_a4': 4,
            'qualis_b1_b2': 2,
            'qualis_b3_b4': 1,
            'livro_tecnico': 10,
            'organizacao_edicao_livro': 5,
            'capitulo_livro': 5,
            'trabalhos_internacional': 4,
            'trabalhos_nacional': 2,
            'bolsista_pq': 20,
            'editor_internacional': 5,
            'editor_nacional': 3,
            'organizacao_eventos': 0,
            'traducao_livro': 0,
            'traducao_artigo': 0,
            'curadoria': 0,
            'organizacao_festival': 0,
            'producao_visual': 0,
            'producao_musical': 0,
            'artes_cenicas': 0,
            'programa_computador': 10,
            'patente_depositada': 10,
            'patente_concedida': 20,
            'patente_licenciada': 30,
            'material_didatico': 0,
            'tese_doutorado': 15,
            'dissertacao_mestrado': 10,
            'tcc_especializacao': 2,
            'iniciacao_cientifica': 5,
            'tcc_graduacao': 1,
            'supervisao_pos_doc': 10
        }


class AvaliacaoH(AvaliacaoAcademica):
    """Especialização para avaliação tipo H"""
    
    def get_pesos(self) -> Dict[str, int]:
        return {
            'artigo_jcr': 10,
            'qualis_a1': 10,
            'qualis_a2': 8,
            'qualis_a3': 6,
            'qualis_a4': 4,
            'qualis_b1_b2': 2,
            'qualis_b3_b4': 1,
            'livro_tecnico': 10,
            'organizacao_edicao_livro': 5,
            'capitulo_livro': 5,
            'trabalhos_internacional': 4,
            'trabalhos_nacional': 2,
            'bolsista_pq': 20,
            'editor_internacional': 5,
            'editor_nacional': 3,
            'organizacao_eventos': 3,
            'traducao_livro': 0,
            'traducao_artigo': 0,
            'curadoria': 0,
            'organizacao_festival': 0,
            'producao_visual': 0,
            'producao_musical': 0,
            'artes_cenicas': 0,
            'programa_computador': 0,
            'patente_depositada': 0,
            'patente_concedida': 0,
            'patente_licenciada': 0,
            'material_didatico': 3,
            'tese_doutorado': 15,
            'dissertacao_mestrado': 10,
            'tcc_especializacao': 2,
            'iniciacao_cientifica': 5,
            'tcc_graduacao': 1,
            'supervisao_pos_doc': 10
        }


class Pesquisador(ABC):
    """Classe base para avaliação do pesquisador"""
    def __init__(self, nome, anos):
        self.nome = nome
        self.doutorado = False
        self.mestrado = False
        self.bolsistaPQ = False
        self.anos = anos

    # Metodo para calculo total
    def pontuacao_por_ano(self):
        pts_anos = []
        for ano in self.anos:
            pts_anos.append(self.avaliacao[ano].calcular_pontuacao_total())
        return pts_anos
            

    def pontuacao_total(self):
        if self.doutorado:
            total = 50
        elif self.mestrado:
            total = 30
        else:
            total = 0

        if self.bolsistaPQ:
            total += 20
        
        for ano in self.anos:
            total += self.avaliacao[ano].calcular_pontuacao_total()

        return total  
        

class PesquisadorA(Pesquisador):
    def __init__(self, nome, anos):
        super().__init__(nome, anos)

        # Criando uma instância de AvaliacaoA para cada ano        
        self.avaliacao = {}
        for ano in self.anos:
            self.avaliacao[ano] = AvaliacaoA()
        

class PesquisadorE(Pesquisador):
    def __init__(self, nome, anos):
        super().__init__(nome, anos)

        # Criando uma instância de AvaliacaoE para cada ano
        self.avaliacao = {}
        for ano in self.anos:
            self.avaliacao[ano] = AvaliacaoE()


class PesquisadorH(Pesquisador):
    def __init__(self, nome, anos):
        super().__init__(nome, anos)

        # Criando uma instância de AvaliacaoH para cada ano
        self.avaliacao = {}
        for ano in self.anos:
            self.avaliacao[ano] = AvaliacaoH()

def pontoItem(pesq, ava, item):
    avaliacao = pesq.avaliacao[pesq.anos[ava]]
    return avaliacao.calcular_pontuacao_item(item, getattr(avaliacao, item))

def pontosG1Ava(pesq, ava):
    avaliacao = pesq.avaliacao[pesq.anos[ava]]
    return avaliacao.calcular_grupo_1()

def pontosG2Ava(pesq, ava):
    avaliacao = pesq.avaliacao[pesq.anos[ava]]
    return avaliacao.calcular_grupo_2()

def pontosAva(pesq, ava):
    avaliacao = pesq.avaliacao[pesq.anos[ava]]
    return avaliacao.calcular_pontuacao_total()


def geraHTML2025(p):
    tit = 0
    sRes = []
    sRes.append('<!DOCTYPE html>')
    sRes.append('<html lang="pt-BR">')
    sRes.append('<head>')
    sRes.append('    <meta charset="UTF-8">')
    sRes.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    sRes.append(f'    <title>Avaliação de {p.nome}</title>')
    sRes.append('    <style>')
    sRes.append('        body {')
    sRes.append('            font-family: Arial, sans-serif;')
    sRes.append('            margin: 20px;')
    sRes.append('            line-height: 1.1;')
    sRes.append('            font-size: 10px;')
    sRes.append('        }')
    sRes.append('        .container {')
    sRes.append('            max-width: 1200px;')
    sRes.append('            margin: 0 auto;')
    sRes.append('        }')
    sRes.append('        h3 {')
    sRes.append('            color: #333;')
    sRes.append('            text-align: center;')
    sRes.append('            margin-bottom: 10px;')
    sRes.append('        }')
    sRes.append('        table {')
    sRes.append('            width: 100%;')
    sRes.append('            border-collapse: collapse;')
    sRes.append('            margin-bottom: 20px;')
    sRes.append('            box-shadow: 0 2px 5px rgba(0,0,0,0.1);')
    sRes.append('        }')
    sRes.append('        th, td {')
    sRes.append('            border: 1px solid #ddd;')
    sRes.append('            padding: 6px;')
    sRes.append('            text-align: left;')
    sRes.append('        }')
    sRes.append('        th {')
    sRes.append('            background-color: #f8f9fa;')
    sRes.append('            font-weight: bold;')
    sRes.append('        }')
    sRes.append('        .section-header {')
    sRes.append('            background-color: #e9ecef;')
    sRes.append('            font-weight: bold;')
    sRes.append('            text-align: center;')
    sRes.append('        }')
    sRes.append('        .points-column {')
    sRes.append('            text-align: center;')
    sRes.append('            width: 58px;')
    sRes.append('            padding: 3px;')
    sRes.append('        }')
    sRes.append('        .points-double-column {')
    sRes.append('            text-align: center;')
    sRes.append('            width: 135px;')
    sRes.append('            padding: 3px;')
    sRes.append('        }')
    sRes.append('        .year-column {')
    sRes.append('            text-align: center;')
    sRes.append('            width: 40px;')
    sRes.append('            padding: 3px;')
    sRes.append('        }')
    sRes.append('        .subtotal-row {')
    sRes.append('            background-color: #f8f9fa;')
    sRes.append('            font-weight: bold;')
    sRes.append('        }')
    sRes.append('        .footer-note {')
    sRes.append('            font-style: italic;')
    sRes.append('            margin-top: 20px;')
    sRes.append('            text-align: center;')
    sRes.append('            color: #666;')
    sRes.append('        }')
    sRes.append('    </style>')
    sRes.append('</head>')
    sRes.append('<body>')
    sRes.append('    <div class="container">')
    sRes.append(f'        <h3>Avaliação de {p.nome}</h3>')
    sRes.append('        ')
    sRes.append('        <!-- Formação Acadêmica -->')
    sRes.append('        <table>')
    sRes.append('            <thead>')
    sRes.append('                <tr>')
    sRes.append('                    <th>Formação Acadêmica</th>')
    sRes.append('                    <th class="points-column">Pontuação</th>')
    sRes.append('                    <th class="points-double-column">Pontuação Indicada</th>')
    sRes.append('                    <th class="points-column">Subtotal</th>')
    sRes.append('                </tr>')
    sRes.append('            </thead>')
    sRes.append('            <tbody>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Titulação Máxima (mestrado = 30; doutorado = 50)</td>')
    sRes.append('                    <td class="points-column">30 ou 50</td>')
    if p.doutorado:
        sRes.append('                    <td class="points-double-column">50</td>')
        sRes.append('                    <td class="points-column">50</td>')
        tit = 50
    elif p.mestrado:
        sRes.append('                    <td class="points-double-column">30</td>')
        sRes.append('                    <td class="points-column">30</td>')
        tit = 30
    else:
        sRes.append('                    <td class="points-double-column">0</td>')
        sRes.append('                    <td class="points-column">0</td>')
        tit = 0
    sRes.append('                </tr>')
    sRes.append('            </tbody>')
    sRes.append('        </table>')
    sRes.append('')
    sRes.append('        <!-- Produção Técnica, Científica e de Inovação -->')
    sRes.append('        <table>')
    sRes.append('            <thead>')
    sRes.append('                <tr>')
    sRes.append('                    <th>Produção Técnica, Científica e de Inovação</th>')
    sRes.append('                    <th class="points-column">Pontuação</th>')
    sRes.append('                    <th class="year-column">2022</th>')
    sRes.append('                    <th class="year-column">2023</th>')
    sRes.append('                    <th class="year-column">2024</th>')
    sRes.append('                    <th class="points-column">Subtotal</th>')
    sRes.append('                </tr>')
    sRes.append('            </thead>')
    sRes.append('            <tbody>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Artigo indexado com JCR</td>')
    sRes.append('                    <td class="points-column">10</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "artigo_jcr")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "artigo_jcr")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "artigo_jcr")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "artigo_jcr")+pontoItem(p, 1, "artigo_jcr")+pontoItem(p, 2, "artigo_jcr")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis A1</td>')
    sRes.append('                    <td class="points-column">10</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "qualis_a1")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "qualis_a1")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "qualis_a1")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "qualis_a1")+pontoItem(p, 1, "qualis_a1")+pontoItem(p, 2, "qualis_a1")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis A2</td>')
    sRes.append('                    <td class="points-column">8</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "qualis_a2")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "qualis_a2")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "qualis_a2")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "qualis_a2")+pontoItem(p, 1, "qualis_a2")+pontoItem(p, 2, "qualis_a2")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis A3</td>')
    sRes.append('                    <td class="points-column">6</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "qualis_a3")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "qualis_a3")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "qualis_a3")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "qualis_a3")+pontoItem(p, 1, "qualis_a3")+pontoItem(p, 2, "qualis_a3")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis A4</td>')
    sRes.append('                    <td class="points-column">4</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "qualis_a4")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "qualis_a4")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "qualis_a4")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "qualis_a4")+pontoItem(p, 1, "qualis_a4")+pontoItem(p, 2, "qualis_a4")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis B1 e B2</td>')
    sRes.append('                    <td class="points-column">2</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "qualis_b1_b2")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "qualis_b1_b2")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "qualis_b1_b2")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "qualis_b1_b2")+pontoItem(p, 1, "qualis_b1_b2")+pontoItem(p, 2, "qualis_b1_b2")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis B3 e B4</td>')
    sRes.append('                    <td class="points-column">1</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "qualis_b3_b4")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "qualis_b3_b4")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "qualis_b3_b4")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "qualis_b3_b4")+pontoItem(p, 1, "qualis_b3_b4")+pontoItem(p, 2, "qualis_b3_b4")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Publicação de Livro Técnico-Científico (como autor)</td>')
    sRes.append('                    <td class="points-column">10</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "livro_tecnico")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "livro_tecnico")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "livro_tecnico")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "livro_tecnico")+pontoItem(p, 1, "livro_tecnico")+pontoItem(p, 2, "livro_tecnico")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Organização ou Edição de livro com ISBN (exceto livros de anais de evento)</td>')
    sRes.append('                    <td class="points-column">5</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "organizacao_edicao_livro")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "organizacao_edicao_livro")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "organizacao_edicao_livro")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "organizacao_edicao_livro")+pontoItem(p, 1, "organizacao_edicao_livro")+pontoItem(p, 2, "organizacao_edicao_livro")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Capítulo de Livro (máximo 1 por livro)</td>')
    sRes.append('                    <td class="points-column">5</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "capitulo_livro")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "capitulo_livro")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "capitulo_livro")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "capitulo_livro")+pontoItem(p, 1, "capitulo_livro")+pontoItem(p, 2, "capitulo_livro")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Trabalhos completos publicados em anais com ISSN - Internacional (máximo 4 por ano)</td>')
    sRes.append('                    <td class="points-column">4</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "trabalhos_internacional")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "trabalhos_internacional")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "trabalhos_internacional")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "trabalhos_internacional")+pontoItem(p, 1, "trabalhos_internacional")+pontoItem(p, 2, "trabalhos_internacional")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Trabalhos completos publicados em anais com ISSN - Nacional (máximo 4 por ano)</td>')
    sRes.append('                    <td class="points-column">2</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "trabalhos_nacional")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "trabalhos_nacional")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "trabalhos_nacional")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "trabalhos_nacional")+pontoItem(p, 1, "trabalhos_nacional")+pontoItem(p, 2, "trabalhos_nacional")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Atuação como Bolsista de Produtividade ou Produtividade em Desenvolvimento Tecnológico e Extensão Inovadora pelo CNPq</td>')
    sRes.append('                    <td class="points-column">20</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "bolsista_pq")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "bolsista_pq")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "bolsista_pq")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "bolsista_pq")+pontoItem(p, 1, "bolsista_pq")+pontoItem(p, 2, "bolsista_pq")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Atuação como editor/a chefe ou associado/a de periódico científico com ISSN internacional</td>')
    sRes.append('                    <td class="points-column">5</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "editor_internacional")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "editor_internacional")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "editor_internacional")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "editor_internacional")+pontoItem(p, 1, "editor_internacional")+pontoItem(p, 2, "editor_internacional")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Atuação como editor/a chefe ou associado/a de periódico científico com ISSN nacional</td>')
    sRes.append('                    <td class="points-column">3</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "editor_nacional")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "editor_nacional")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "editor_nacional")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "editor_nacional")+pontoItem(p, 1, "editor_nacional")+pontoItem(p, 2, "editor_nacional")}</td>')
    sRes.append('                </tr>')
    if (isinstance(p, (PesquisadorA, PesquisadorH))):
        sRes.append('                <tr>')
        sRes.append('                    <td>Organização de eventos técnico-científicos (internacional, nacional e regional)</td>')
        sRes.append('                    <td class="points-column">3</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "organizacao_eventos")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "organizacao_eventos")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "organizacao_eventos")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "organizacao_eventos")+pontoItem(p, 1, "organizacao_eventos")+pontoItem(p, 2, "organizacao_eventos")}</td>')
        sRes.append('                </tr>')
    if (isinstance(p, PesquisadorA)):
        sRes.append('                <tr>')
        sRes.append('                    <td>Tradução integral de livro técnico-científico da área com ISBN</td>')
        sRes.append('                    <td class="points-column">5</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "traducao_livro")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "traducao_livro")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "traducao_livro")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "traducao_livro")+pontoItem(p, 1, "traducao_livro")+pontoItem(p, 2, "traducao_livro")}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Tradução de artigo científico</td>')
        sRes.append('                    <td class="points-column">3</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "traducao_artigo")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "traducao_artigo")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "traducao_artigo")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "traducao_artigo")+pontoItem(p, 1, "traducao_artigo")+pontoItem(p, 2, "traducao_artigo")}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Curadoria de festival, concerto, exposição, concurso</td>')
        sRes.append('                    <td class="points-column">5</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "curadoria")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "curadoria")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "curadoria")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "curadoria")+pontoItem(p, 1, "curadoria")+pontoItem(p, 2, "curadoria")}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Organização de festival, concerto, exposição, concurso</td>')
        sRes.append('                    <td class="points-column">5</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "organizacao_festival")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "organizacao_festival")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "organizacao_festival")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "organizacao_festival")+pontoItem(p, 1, "organizacao_festival")+pontoItem(p, 2, "organizacao_festival")}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Produção Visual (filme, fotografia, vídeo, instalação, performance, animação, desenho, pintura, gravura)</td>')
        sRes.append('                    <td class="points-column">5</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "producao_visual")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "producao_visual")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "producao_visual")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "producao_visual")+pontoItem(p, 1, "producao_visual")+pontoItem(p, 2, "producao_visual")}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Produção musical (apresentação de obra, composição, trilha sonora, interpretação, publicação de partitura, arranjo)</td>')
        sRes.append('                    <td class="points-column">5</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "producao_musical")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "producao_musical")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "producao_musical")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "producao_musical")+pontoItem(p, 1, "producao_musical")+pontoItem(p, 2, "producao_musical")}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Artes cênicas (audiovisual, performática, operística, coreográfica, circense, teatral)</td>')
        sRes.append('                    <td class="points-column">5</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "artes_cenicas")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "artes_cenicas")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "artes_cenicas")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "artes_cenicas")+pontoItem(p, 1, "artes_cenicas")+pontoItem(p, 2, "artes_cenicas")}</td>')
        sRes.append('                </tr>')
    elif (isinstance(p, PesquisadorH)):
        sRes.append('                <tr>')
        sRes.append('                    <td>Produção de material didático</td>')
        sRes.append('                    <td class="points-column">3</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "material_didatico")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "material_didatico")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "material_didatico")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "material_didatico")+pontoItem(p, 1, "material_didatico")+pontoItem(p, 2, "material_didatico")}</td>')
        sRes.append('                </tr>')
    else:
        sRes.append('                <tr>')
        sRes.append('                    <td>Programa de computador registrado</td>')
        sRes.append('                    <td class="points-column">10</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "programa_computador")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "programa_computador")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "programa_computador")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "programa_computador")+pontoItem(p, 1, "programa_computador")+pontoItem(p, 2, "programa_computador")}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Patente Depositada no INPI</td>')
        sRes.append('                    <td class="points-column">10</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "patente_depositada")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "patente_depositada")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "patente_depositada")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "patente_depositada")+pontoItem(p, 1, "patente_depositada")+pontoItem(p, 2, "patente_depositada")}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Patente Concedida no INPI</td>')
        sRes.append('                    <td class="points-column">20</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "patente_concedida")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "patente_concedida")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "patente_concedida")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "patente_concedida")+pontoItem(p, 1, "patente_concedida")+pontoItem(p, 2, "patente_concedida")}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Patente Licenciada</td>')
        sRes.append('                    <td class="points-column">20</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "patente_licenciada")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "patente_licenciada")}</td>')
        sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "patente_licenciada")}</td>')
        sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "patente_licenciada")+pontoItem(p, 1, "patente_licenciada")+pontoItem(p, 2, "patente_licenciada")}</td>')
        sRes.append('                </tr>')

    sRes.append('                <tr class="subtotal-row">')
    sRes.append('                    <td><strong>Subtotal da Produção Técnica, Científica e de Inovação</strong></td>')
    sRes.append('                    <td class="points-column"></td>')
    sRes.append(f'                    <td class="year-column">{pontosG1Ava(p, 0)}</td>')
    sRes.append(f'                    <td class="year-column">{pontosG1Ava(p, 1)}</td>')
    sRes.append(f'                    <td class="year-column">{pontosG1Ava(p, 2)}</td>')
    sRes.append(f'                    <td class="points-column">{pontosG1Ava(p, 0)+pontosG1Ava(p, 1)+pontosG1Ava(p, 2)}</td>')
    sRes.append('                </tr>')
    sRes.append('            </tbody>')
    sRes.append('        </table>')
    sRes.append('')
    sRes.append('        <!-- Formação de Recursos Humanos em Pesquisa -->')
    sRes.append('        <table>')
    sRes.append('            <thead>')
    sRes.append('                <tr>')
    sRes.append('                    <th>Formação de Recursos Humanos em Pesquisa</th>')
    sRes.append('                    <th class="points-column">Pontuação</th>')
    sRes.append('                    <th class="year-column">2022</th>')
    sRes.append('                    <th class="year-column">2023</th>')
    sRes.append('                    <th class="year-column">2024</th>')
    sRes.append('                    <th class="points-column">Subtotal</th>')
    sRes.append('                </tr>')
    sRes.append('            </thead>')
    sRes.append('            <tbody>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Tese de doutorado orientada e defendida</td>')
    sRes.append('                    <td class="points-column">15</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "tese_doutorado")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "tese_doutorado")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "tese_doutorado")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "tese_doutorado")+pontoItem(p, 1, "tese_doutorado")+pontoItem(p, 2, "tese_doutorado")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Dissertação de Mestrado Orientada e Defendida</td>')
    sRes.append('                    <td class="points-column">10</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "dissertacao_mestrado")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "dissertacao_mestrado")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "dissertacao_mestrado")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "dissertacao_mestrado")+pontoItem(p, 1, "dissertacao_mestrado")+pontoItem(p, 2, "dissertacao_mestrado")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>TCC/Monografia de especialização lato sensu orientada e defendida (máximo 3 ano)</td>')
    sRes.append('                    <td class="points-column">2</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "tcc_especializacao")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "tcc_especializacao")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "tcc_especializacao")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "tcc_especializacao")+pontoItem(p, 1, "tcc_especializacao")+pontoItem(p, 2, "tcc_especializacao")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Orientação de Iniciação Científica concluída</td>')
    sRes.append('                    <td class="points-column">5</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "iniciacao_cientifica")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "iniciacao_cientifica")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "iniciacao_cientifica")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "iniciacao_cientifica")+pontoItem(p, 1, "iniciacao_cientifica")+pontoItem(p, 2, "iniciacao_cientifica")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>TCC/Monografia de graduação orientada e defendida (máximo 5/ano)</td>')
    sRes.append('                    <td class="points-column">1</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "tcc_graduacao")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "tcc_graduacao")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "tcc_graduacao")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "tcc_graduacao")+pontoItem(p, 1, "tcc_graduacao")+pontoItem(p, 2, "tcc_graduacao")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Supervisão de pós-doutorado</td>')
    sRes.append('                    <td class="points-column">10</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 0, "supervisao_pos_doc")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 1, "supervisao_pos_doc")}</td>')
    sRes.append(f'                    <td class="year-column">{pontoItem(p, 2, "supervisao_pos_doc")}</td>')
    sRes.append(f'                    <td class="points-column">{pontoItem(p, 0, "supervisao_pos_doc")+pontoItem(p, 1, "supervisao_pos_doc")+pontoItem(p, 2, "supervisao_pos_doc")}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr class="subtotal-row">')
    sRes.append('                    <td><strong>Subtotal da Formação de Recursos Humanos em Pesquisa</strong></td>')
    sRes.append('                    <td class="points-column"></td>')
    sRes.append(f'                    <td class="year-column">{pontosG2Ava(p, 0)}</td>')
    sRes.append(f'                    <td class="year-column">{pontosG2Ava(p, 1)}</td>')
    sRes.append(f'                    <td class="year-column">{pontosG2Ava(p, 2)}</td>')
    sRes.append(f'                    <td class="points-column">{pontosG2Ava(p, 0)+pontosG2Ava(p, 1)+pontosG2Ava(p, 2)}</td>')
    sRes.append('                </tr>')
    sRes.append('            </tbody>')
    sRes.append('        </table>')
    sRes.append('')
    sRes.append('        <!-- Resumo Final -->')
    sRes.append('        <table>')
    sRes.append('            <thead>')
    sRes.append('                <tr>')
    sRes.append('                    <th>Planilha atualizada pela PROPESQ em março de 2025</th>')
    sRes.append('                    <th class="points-column">Titulação</th>')
    sRes.append('                    <th class="year-column">2022</th>')
    sRes.append('                    <th class="year-column">2023</th>')
    sRes.append('                    <th class="year-column">2024</th>')
    sRes.append('                    <th class="points-column">Total</th>')
    sRes.append('                </tr>')
    sRes.append('            </thead>')
    sRes.append('            <tbody>')
    sRes.append('                <tr>')
    sRes.append('                    <td></td>')
    sRes.append(f'                    <td class="points-column">{tit}</td>')
    sRes.append(f'                    <td class="year-column">{pontosAva(p, 0)}</td>')
    sRes.append(f'                    <td class="year-column">{pontosAva(p, 1)}</td>')
    sRes.append(f'                    <td class="year-column">{pontosAva(p, 2)}</td>')
    sRes.append(f'                    <td class="points-column">{p.pontuacao_total()}</td>')
    sRes.append('                </tr>')
    sRes.append('            </tbody>')
    sRes.append('        </table>')
    sRes.append('')
    sRes.append('        <div class="footer-note">')
    sRes.append('            <em>Planilha atualizada pela PROPESQ em março de 2025</em>')
    sRes.append('        </div>')
    sRes.append('    </div>')
    sRes.append('</body>')
    sRes.append('</html>')
    return sRes

#================================================================================================================
# 2026
#================================================================================================================
def printColunas(s, lst):
    res = []
    for l in lst:
        res.append(s % str(l) + '\n');
    return ''.join(res)

def geraHTML(p):
    tit = 0
    sRes = []
    sRes.append('<!DOCTYPE html>')
    sRes.append('<html lang="pt-BR">')
    sRes.append('<head>')
    sRes.append('    <meta charset="UTF-8">')
    sRes.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    sRes.append(f'    <title>Avaliação de {p.nome}</title>')
    sRes.append('    <style>')
    sRes.append('        body {')
    sRes.append('            font-family: Arial, sans-serif;')
    sRes.append('            margin: 20px;')
    sRes.append('            line-height: 1.1;')
    sRes.append('            font-size: 10px;')
    sRes.append('        }')
    sRes.append('        .container {')
    sRes.append('            max-width: 1200px;')
    sRes.append('            margin: 0 auto;')
    sRes.append('        }')
    sRes.append('        h3 {')
    sRes.append('            color: #333;')
    sRes.append('            text-align: center;')
    sRes.append('            margin-bottom: 10px;')
    sRes.append('        }')
    sRes.append('        table {')
    sRes.append('            width: 100%;')
    sRes.append('            border-collapse: collapse;')
    sRes.append('            margin-bottom: 20px;')
    sRes.append('            box-shadow: 0 2px 5px rgba(0,0,0,0.1);')
    sRes.append('        }')
    sRes.append('        th, td {')
    sRes.append('            border: 1px solid #ddd;')
    sRes.append('            padding: 6px;')
    sRes.append('            text-align: left;')
    sRes.append('        }')
    sRes.append('        th {')
    sRes.append('            background-color: #f8f9fa;')
    sRes.append('            font-weight: bold;')
    sRes.append('        }')
    sRes.append('        .section-header {')
    sRes.append('            background-color: #e9ecef;')
    sRes.append('            font-weight: bold;')
    sRes.append('            text-align: center;')
    sRes.append('        }')
    sRes.append('        .points-column {')
    sRes.append('            text-align: center;')
    sRes.append('            width: 58px;')
    sRes.append('            padding: 3px;')
    sRes.append('        }')
    sRes.append('        .points-double-column {')
    sRes.append('            text-align: center;')
    sRes.append('            width: 135px;')
    sRes.append('            padding: 3px;')
    sRes.append('        }')
    sRes.append('        .year-column {')
    sRes.append('            text-align: center;')
    sRes.append('            width: 40px;')
    sRes.append('            padding: 3px;')
    sRes.append('        }')
    sRes.append('        .subtotal-row {')
    sRes.append('            background-color: #f8f9fa;')
    sRes.append('            font-weight: bold;')
    sRes.append('        }')
    sRes.append('        .footer-note {')
    sRes.append('            font-style: italic;')
    sRes.append('            margin-top: 20px;')
    sRes.append('            text-align: center;')
    sRes.append('            color: #666;')
    sRes.append('        }')
    sRes.append('    </style>')
    sRes.append('</head>')
    sRes.append('<body>')
    sRes.append('    <div class="container">')
    sRes.append(f'        <h3>Avaliação de {p.nome}</h3>')
    sRes.append('        ')
    sRes.append('        <!-- Formação Acadêmica -->')
    sRes.append('        <table>')
    sRes.append('            <thead>')
    sRes.append('                <tr>')
    sRes.append('                    <th>Formação Acadêmica</th>')
    sRes.append('                    <th class="points-column">Pontuação</th>')
    sRes.append('                    <th class="points-double-column">Pontuação Indicada</th>')
    sRes.append('                    <th class="points-column">Subtotal</th>')
    sRes.append('                </tr>')
    sRes.append('            </thead>')
    sRes.append('            <tbody>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Titulação Máxima (mestrado = 30; doutorado = 50)</td>')
    sRes.append('                    <td class="points-column">30 ou 50</td>')
    if p.doutorado:
        sRes.append('                    <td class="points-double-column">50</td>')
        sRes.append('                    <td class="points-column">50</td>')
        tit = 50
    elif p.mestrado:
        sRes.append('                    <td class="points-double-column">30</td>')
        sRes.append('                    <td class="points-column">30</td>')
        tit = 30
    else:
        sRes.append('                    <td class="points-double-column">0</td>')
        sRes.append('                    <td class="points-column">0</td>')
        tit = 0
    sRes.append('                </tr>')
    sRes.append('            </tbody>')
    sRes.append('        </table>')
    sRes.append('')
    sRes.append('        <!-- Produção Técnica, Científica e de Inovação -->')
    sRes.append('        <table>')
    sRes.append('            <thead>')
    sRes.append('                <tr>')
    sRes.append('                    <th>Produção Técnica, Científica e de Inovação</th>')
    sRes.append('                    <th class="points-column">Pontuação</th>')
    sRes.append(printColunas('<th class="year-column">%s</th>', [x for x in p.anos]))
    sRes.append('                    <th class="points-column">Subtotal</th>')
    sRes.append('                </tr>')
    sRes.append('            </thead>')
    sRes.append('            <tbody>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Artigo indexado com JCR</td>')
    sRes.append('                    <td class="points-column">10</td>')
    lst = [pontoItem(p, x, "artigo_jcr") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis A1</td>')
    sRes.append('                    <td class="points-column">10</td>')
    lst = [pontoItem(p, x, "qualis_a1") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis A2</td>')
    sRes.append('                    <td class="points-column">8</td>')
    lst = [pontoItem(p, x, "qualis_a2") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis A3</td>')
    sRes.append('                    <td class="points-column">6</td>')
    lst = [pontoItem(p, x, "qualis_a3") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis A4</td>')
    sRes.append('                    <td class="points-column">4</td>')
    lst = [pontoItem(p, x, "qualis_a4") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis B1 e B2</td>')
    sRes.append('                    <td class="points-column">2</td>')
    lst = [pontoItem(p, x, "qualis_b1_b2") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Periódico Qualis B3 e B4</td>')
    sRes.append('                    <td class="points-column">1</td>')
    lst = [pontoItem(p, x, "qualis_b3_b4") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Publicação de Livro Técnico-Científico (como autor)</td>')
    sRes.append('                    <td class="points-column">10</td>')
    lst = [pontoItem(p, x, "livro_tecnico") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Organização ou Edição de livro com ISBN (exceto livros de anais de evento)</td>')
    sRes.append('                    <td class="points-column">5</td>')
    lst = [pontoItem(p, x, "organizacao_edicao_livro") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Capítulo de Livro (máximo 1 por livro)</td>')
    sRes.append('                    <td class="points-column">5</td>')
    lst = [pontoItem(p, x, "capitulo_livro") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Trabalhos completos publicados em anais com ISSN - Internacional (máximo 4 por ano)</td>')
    sRes.append('                    <td class="points-column">4</td>')
    lst = [pontoItem(p, x, "trabalhos_internacional") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Trabalhos completos publicados em anais com ISSN - Nacional (máximo 4 por ano)</td>')
    sRes.append('                    <td class="points-column">2</td>')
    lst = [pontoItem(p, x, "trabalhos_nacional") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Atuação como Bolsista de Produtividade ou Produtividade em Desenvolvimento Tecnológico e Extensão Inovadora pelo CNPq</td>')
    sRes.append('                    <td class="points-column">20</td>')
    lst = [pontoItem(p, x, "bolsista_pq") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Atuação como editor/a chefe ou associado/a de periódico científico com ISSN internacional</td>')
    sRes.append('                    <td class="points-column">5</td>')
    lst = [pontoItem(p, x, "editor_internacional") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Atuação como editor/a chefe ou associado/a de periódico científico com ISSN nacional</td>')
    sRes.append('                    <td class="points-column">3</td>')
    lst = [pontoItem(p, x, "editor_nacional") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    if (isinstance(p, (PesquisadorA, PesquisadorH))):
        sRes.append('                <tr>')
        sRes.append('                    <td>Organização de eventos técnico-científicos (internacional, nacional e regional)</td>')
        sRes.append('                    <td class="points-column">3</td>')
        lst = [pontoItem(p, x, "organizacao_eventos") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
    if (isinstance(p, PesquisadorA)):
        sRes.append('                <tr>')
        sRes.append('                    <td>Tradução integral de livro técnico-científico da área com ISBN</td>')
        sRes.append('                    <td class="points-column">5</td>')
        lst = [pontoItem(p, x, "traducao_livro") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Tradução de artigo científico</td>')
        sRes.append('                    <td class="points-column">3</td>')
        lst = [pontoItem(p, x, "traducao_artigo") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Curadoria de festival, concerto, exposição, concurso</td>')
        sRes.append('                    <td class="points-column">5</td>')
        lst = [pontoItem(p, x, "curadoria") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Organização de festival, concerto, exposição, concurso</td>')
        sRes.append('                    <td class="points-column">5</td>')
        lst = [pontoItem(p, x, "organizacao_festival") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Produção Visual (filme, fotografia, vídeo, instalação, performance, animação, desenho, pintura, gravura)</td>')
        sRes.append('                    <td class="points-column">5</td>')
        lst = [pontoItem(p, x, "producao_visual") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Produção musical (apresentação de obra, composição, trilha sonora, interpretação, publicação de partitura, arranjo)</td>')
        sRes.append('                    <td class="points-column">5</td>')
        lst = [pontoItem(p, x, "producao_musical") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Artes cênicas (audiovisual, performática, operística, coreográfica, circense, teatral)</td>')
        sRes.append('                    <td class="points-column">5</td>')
        lst = [pontoItem(p, x, "artes_cenicas") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
    elif (isinstance(p, PesquisadorH)):
        sRes.append('                <tr>')
        sRes.append('                    <td>Produção de material didático</td>')
        sRes.append('                    <td class="points-column">3</td>')
        lst = [pontoItem(p, x, "material_didatico") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
    else:
        sRes.append('                <tr>')
        sRes.append('                    <td>Programa de computador registrado</td>')
        sRes.append('                    <td class="points-column">10</td>')
        lst = [pontoItem(p, x, "programa_computador") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Patente Depositada no INPI</td>')
        sRes.append('                    <td class="points-column">10</td>')
        lst = [pontoItem(p, x, "patente_depositada") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Patente Concedida no INPI</td>')
        sRes.append('                    <td class="points-column">20</td>')
        lst = [pontoItem(p, x, "patente_concedida") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')
        sRes.append('                <tr>')
        sRes.append('                    <td>Patente Licenciada</td>')
        sRes.append('                    <td class="points-column">20</td>')
        lst = [pontoItem(p, x, "patente_licenciada") for x in range(len(p.anos))]
        sRes.append(printColunas('<td class="year-column">%s</td>', lst))
        sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
        sRes.append('                </tr>')

    sRes.append('                <tr class="subtotal-row">')
    sRes.append('                    <td><strong>Subtotal da Produção Técnica, Científica e de Inovação</strong></td>')
    sRes.append('                    <td class="points-column"></td>')
    lst = [pontosG1Ava(p, x) for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('            </tbody>')
    sRes.append('        </table>')
    sRes.append('')
    sRes.append('        <!-- Formação de Recursos Humanos em Pesquisa -->')
    sRes.append('        <table>')
    sRes.append('            <thead>')
    sRes.append('                <tr>')
    sRes.append('                    <th>Formação de Recursos Humanos em Pesquisa</th>')
    sRes.append('                    <th class="points-column">Pontuação</th>')
    sRes.append(printColunas('<th class="year-column">%s</th>', [x for x in p.anos]))
    sRes.append('                    <th class="points-column">Subtotal</th>')
    sRes.append('                </tr>')
    sRes.append('            </thead>')
    sRes.append('            <tbody>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Tese de doutorado orientada e defendida</td>')
    sRes.append('                    <td class="points-column">15</td>')
    lst = [pontoItem(p, x, "tese_doutorado") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Dissertação de Mestrado Orientada e Defendida</td>')
    sRes.append('                    <td class="points-column">10</td>')
    lst = [pontoItem(p, x, "dissertacao_mestrado") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>TCC/Monografia de especialização lato sensu orientada e defendida (máximo 3 ano)</td>')
    sRes.append('                    <td class="points-column">2</td>')
    lst = [pontoItem(p, x, "tcc_especializacao") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Orientação de Iniciação Científica concluída</td>')
    sRes.append('                    <td class="points-column">5</td>')
    lst = [pontoItem(p, x, "iniciacao_cientifica") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>TCC/Monografia de graduação orientada e defendida (máximo 5/ano)</td>')
    sRes.append('                    <td class="points-column">1</td>')
    lst = [pontoItem(p, x, "tcc_graduacao") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr>')
    sRes.append('                    <td>Supervisão de pós-doutorado</td>')
    sRes.append('                    <td class="points-column">10</td>')
    lst = [pontoItem(p, x, "supervisao_pos_doc") for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('                <tr class="subtotal-row">')
    sRes.append('                    <td><strong>Subtotal da Formação de Recursos Humanos em Pesquisa</strong></td>')
    sRes.append('                    <td class="points-column"></td>')
    lst = [pontosG2Ava(p, x) for x in range(len(p.anos))]
    sRes.append(printColunas('<td class="year-column">%s</td>', lst))
    sRes.append(f'                    <td class="points-column">{sum(lst)}</td>')
    sRes.append('                </tr>')
    sRes.append('            </tbody>')
    sRes.append('        </table>')
    sRes.append('')
    sRes.append('        <!-- Resumo Final -->')
    sRes.append('        <table>')
    sRes.append('            <thead>')
    sRes.append('                <tr>')
    sRes.append('                    <th>Planilha atualizada pela PROPESQ em março de 2025</th>')
    sRes.append('                    <th class="points-column">Titulação</th>')
    sRes.append('                    ')
    sRes.append(printColunas('<th class="year-column">%s</th>', [x for x in p.anos]))
    sRes.append('                    <th class="points-column">Total</th>')
    sRes.append('                </tr>')
    sRes.append('            </thead>')
    sRes.append('            <tbody>')
    sRes.append('                <tr>')
    sRes.append('                    <td></td>')
    sRes.append(f'                    <td class="points-column">{tit}</td>')
    sRes.append(printColunas('<td class="year-column">%s</td>', [pontosAva(p, x) for x in range(len(p.anos))]))
    sRes.append(f'                    <td class="points-column">{p.pontuacao_total()}</td>')
    sRes.append('                </tr>')
    sRes.append('            </tbody>')
    sRes.append('        </table>')
    sRes.append('')
    sRes.append('        <div class="footer-note">')
    sRes.append('            <em>Planilha atualizada pela PROPESQ em março de 2026</em>')
    sRes.append('        </div>')
    sRes.append('    </div>')
    sRes.append('</body>')
    sRes.append('</html>')
    return sRes

