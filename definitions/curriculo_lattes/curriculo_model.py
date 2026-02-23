######
# versao para o XSD de 2022-09-12
######

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class AperfeicoamentoStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


class AreaDeAtuacaoNomeGrandeAreaDoConhecimento(Enum):
    OUTROS = "OUTROS"
    LINGUISTICA_LETRAS_E_ARTES = "LINGUISTICA_LETRAS_E_ARTES"
    CIENCIAS_HUMANAS = "CIENCIAS_HUMANAS"
    CIENCIAS_SOCIAIS_APLICADAS = "CIENCIAS_SOCIAIS_APLICADAS"
    CIENCIAS_AGRARIAS = "CIENCIAS_AGRARIAS"
    CIENCIAS_DA_SAUDE = "CIENCIAS_DA_SAUDE"
    ENGENHARIAS = "ENGENHARIAS"
    CIENCIAS_BIOLOGICAS = "CIENCIAS_BIOLOGICAS"
    CIENCIAS_EXATAS_E_DA_TERRA = "CIENCIAS_EXATAS_E_DA_TERRA"


class AreaDoConhecimento1NomeGrandeAreaDoConhecimento(Enum):
    OUTROS = "OUTROS"
    LINGUISTICA_LETRAS_E_ARTES = "LINGUISTICA_LETRAS_E_ARTES"
    CIENCIAS_HUMANAS = "CIENCIAS_HUMANAS"
    CIENCIAS_SOCIAIS_APLICADAS = "CIENCIAS_SOCIAIS_APLICADAS"
    CIENCIAS_AGRARIAS = "CIENCIAS_AGRARIAS"
    CIENCIAS_DA_SAUDE = "CIENCIAS_DA_SAUDE"
    ENGENHARIAS = "ENGENHARIAS"
    CIENCIAS_BIOLOGICAS = "CIENCIAS_BIOLOGICAS"
    CIENCIAS_EXATAS_E_DA_TERRA = "CIENCIAS_EXATAS_E_DA_TERRA"


class AreaDoConhecimento2NomeGrandeAreaDoConhecimento(Enum):
    OUTROS = "OUTROS"
    LINGUISTICA_LETRAS_E_ARTES = "LINGUISTICA_LETRAS_E_ARTES"
    CIENCIAS_HUMANAS = "CIENCIAS_HUMANAS"
    CIENCIAS_SOCIAIS_APLICADAS = "CIENCIAS_SOCIAIS_APLICADAS"
    CIENCIAS_AGRARIAS = "CIENCIAS_AGRARIAS"
    CIENCIAS_DA_SAUDE = "CIENCIAS_DA_SAUDE"
    ENGENHARIAS = "ENGENHARIAS"
    CIENCIAS_BIOLOGICAS = "CIENCIAS_BIOLOGICAS"
    CIENCIAS_EXATAS_E_DA_TERRA = "CIENCIAS_EXATAS_E_DA_TERRA"


class AreaDoConhecimento3NomeGrandeAreaDoConhecimento(Enum):
    OUTROS = "OUTROS"
    LINGUISTICA_LETRAS_E_ARTES = "LINGUISTICA_LETRAS_E_ARTES"
    CIENCIAS_HUMANAS = "CIENCIAS_HUMANAS"
    CIENCIAS_SOCIAIS_APLICADAS = "CIENCIAS_SOCIAIS_APLICADAS"
    CIENCIAS_AGRARIAS = "CIENCIAS_AGRARIAS"
    CIENCIAS_DA_SAUDE = "CIENCIAS_DA_SAUDE"
    ENGENHARIAS = "ENGENHARIAS"
    CIENCIAS_BIOLOGICAS = "CIENCIAS_BIOLOGICAS"
    CIENCIAS_EXATAS_E_DA_TERRA = "CIENCIAS_EXATAS_E_DA_TERRA"


@dataclass(kw_only=True)
class Autores:
    class Meta:
        name = "AUTORES"

    nome_completo_do_autor: None | object = field(
        default=None,
        metadata={
            "name": "NOME-COMPLETO-DO-AUTOR",
            "type": "Attribute",
        },
    )
    nome_para_citacao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-PARA-CITACAO",
            "type": "Attribute",
        },
    )
    ordem_de_autoria: None | object = field(
        default=None,
        metadata={
            "name": "ORDEM-DE-AUTORIA",
            "type": "Attribute",
        },
    )
    cpf: None | object = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Attribute",
        },
    )
    nro_id_cnpq: None | object = field(
        default=None,
        metadata={
            "name": "NRO-ID-CNPQ",
            "type": "Attribute",
        },
    )


class ConselhoComissaoEConsultoriaFlagPeriodo(Enum):
    ANTERIOR = "ANTERIOR"
    ATUAL = "ATUAL"


class CurriculoVitaeFormatoDataAtualizacao(Enum):
    DDMMAAAA = "DDMMAAAA"


class CurriculoVitaeFormatoHoraAtualizacao(Enum):
    HHMMSS = "HHMMSS"


class CursoTecnicoProfissionalizanteStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


class DadosBasicosDaApresentacaoDeObraArtisticaFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaApresentacaoDeObraArtisticaMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaApresentacaoDeObraArtisticaNatureza(Enum):
    COREOGRAFICA = "COREOGRAFICA"
    LITERARIA = "LITERARIA"
    MUSICAL = "MUSICAL"
    TEATRAL = "TEATRAL"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaApresentacaoDeTrabalhoFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaApresentacaoDeTrabalhoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaApresentacaoDeTrabalhoNatureza(Enum):
    COMUNICACAO = "COMUNICACAO"
    CONFERENCIA = "CONFERENCIA"
    CONGRESSO = "CONGRESSO"
    SEMINARIO = "SEMINARIO"
    SIMPOSIO = "SIMPOSIO"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaApresentacaoEmRadioOuTvFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaApresentacaoEmRadioOuTvFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaApresentacaoEmRadioOuTvNatureza(Enum):
    DANCA = "DANCA"
    MUSICA = "MUSICA"
    TEATRO = "TEATRO"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


@dataclass(kw_only=True)
class DadosBasicosDaBancaJulgadoraParaAvaliacaoCursos:
    class Meta:
        name = "DADOS-BASICOS-DA-BANCA-JULGADORA-PARA-AVALIACAO-CURSOS"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaBancaJulgadoraParaConcursoPublico:
    class Meta:
        name = "DADOS-BASICOS-DA-BANCA-JULGADORA-PARA-CONCURSO-PUBLICO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaBancaJulgadoraParaLivreDocencia:
    class Meta:
        name = "DADOS-BASICOS-DA-BANCA-JULGADORA-PARA-LIVRE-DOCENCIA"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaBancaJulgadoraParaProfessorTitular:
    class Meta:
        name = "DADOS-BASICOS-DA-BANCA-JULGADORA-PARA-PROFESSOR-TITULAR"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


class DadosBasicosDaComposicaoMusicalFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaComposicaoMusicalMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaComposicaoMusicalNatureza(Enum):
    CANTO = "CANTO"
    CORAL = "CORAL"
    ORQUESTRA = "ORQUESTRA"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaCultivarFlagPotencialInovacao(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaCultivarFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaMaqueteFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaMaqueteMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaMarcaFlagPotencialInovacao(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaMarcaFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaMidiaSocialWebsiteBlogFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaMidiaSocialWebsiteBlogFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaMidiaSocialWebsiteBlogNatureza(Enum):
    REDE_SOCIAL = "REDE_SOCIAL"
    FORUM = "FORUM"
    BLOG = "BLOG"
    SITE = "SITE"


class DadosBasicosDaMusicaFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaMusicaFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaMusicaMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaMusicaNatureza(Enum):
    APRESENTACAO_DE_OBRA = "APRESENTACAO_DE_OBRA"
    ARRANJO = "ARRANJO"
    AUDIOVISUAL = "AUDIOVISUAL"
    COMPOSICAO = "COMPOSICAO"
    DIVERSAS = "DIVERSAS"
    INTERPRETACAO = "INTERPRETACAO"
    PUBLICACAO_DE_PARTITURA = "PUBLICACAO_DE_PARTITURA"
    REGISTRO_FONOGRAFICO = "REGISTRO_FONOGRAFICO"
    TRILHA_SONORA = "TRILHA_SONORA"
    OUTRA = "OUTRA"


class DadosBasicosDaObraDeArtesVisuaisFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaObraDeArtesVisuaisMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaObraDeArtesVisuaisNatureza(Enum):
    CINEMA = "CINEMA"
    DESENHO = "DESENHO"
    ESCULTURA = "ESCULTURA"
    FOTOGRAFIA = "FOTOGRAFIA"
    GRAVURA = "GRAVURA"
    INSTALACAO = "INSTALACAO"
    PINTURA = "PINTURA"
    TELEVISAO = "TELEVISAO"
    VIDEO = "VIDEO"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaOrganizacaoDeEventoFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaOrganizacaoDeEventoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaOrganizacaoDeEventoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaOrganizacaoDeEventoNatureza(Enum):
    CURADORIA = "CURADORIA"
    MONTAGEM = "MONTAGEM"
    MUSEOLOGIA = "MUSEOLOGIA"
    ORGANIZACAO = "ORGANIZACAO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaOrganizacaoDeEventoTipo(Enum):
    CONCERTO = "CONCERTO"
    CONCURSO = "CONCURSO"
    CONGRESSO = "CONGRESSO"
    EXPOSICAO = "EXPOSICAO"
    FESTIVAL = "FESTIVAL"
    FEIRA = "FEIRA"
    OLIMPIADA = "OLIMPIADA"
    OUTRO = "OUTRO"
    NAO_INFORMADO = "NAO_INFORMADO"


@dataclass(kw_only=True)
class DadosBasicosDaOrientacaoEmAndamentoDeAperfeicoamentoEspecializacao:
    class Meta:
        name = "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-APERFEICOAMENTO-ESPECIALIZACAO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaOrientacaoEmAndamentoDeDoutorado:
    class Meta:
        name = "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-DOUTORADO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaOrientacaoEmAndamentoDeGraduacao:
    class Meta:
        name = "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-GRADUACAO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaOrientacaoEmAndamentoDeIniciacaoCientifica:
    class Meta:
        name = (
            "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-INICIACAO-CIENTIFICA"
        )

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-INGLES",
            "type": "Attribute",
        },
    )


class DadosBasicosDaOrientacaoEmAndamentoDeMestradoTipo(Enum):
    ACADEMICO = "ACADEMICO"
    PROFISSIONALIZANTE = "PROFISSIONALIZANTE"
    NAO_INFORMADO = "NAO_INFORMADO"


@dataclass(kw_only=True)
class DadosBasicosDaOrientacaoEmAndamentoDePosDoutorado:
    class Meta:
        name = "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-POS-DOUTORADO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmBancaDeAperfeicoamentoEspecializacao:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-BANCA-DE-APERFEICOAMENTO-ESPECIALIZACAO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmBancaDeDoutorado:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-BANCA-DE-DOUTORADO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmBancaDeExameQualificacao:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-BANCA-DE-EXAME-QUALIFICACAO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmBancaDeGraduacao:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-BANCA-DE-GRADUACAO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


class DadosBasicosDaParticipacaoEmBancaDeMestradoTipo(Enum):
    ACADEMICO = "ACADEMICO"
    PROFISSIONALIZANTE = "PROFISSIONALIZANTE"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaParticipacaoEmCongressoFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmCongressoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmCongressoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaParticipacaoEmEncontroFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmEncontroFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmEncontroMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaParticipacaoEmExposicaoFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmExposicaoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmExposicaoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaParticipacaoEmFeiraFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmFeiraFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmFeiraMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaParticipacaoEmOficinaFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmOficinaFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmOficinaMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaParticipacaoEmOlimpiadaFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmOlimpiadaFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmOlimpiadaMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaParticipacaoEmSeminarioFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmSeminarioFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmSeminarioMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaParticipacaoEmSimposioFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmSimposioFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaParticipacaoEmSimposioMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaPartituraFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaPartituraMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaPartituraNatureza(Enum):
    CANTO = "CANTO"
    CORAL = "CORAL"
    ORQUESTRA = "ORQUESTRA"
    OUTRO = "OUTRO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaPatenteFlagPotencialInovacao(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaPatenteFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaPatenteMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaTopografiaDeCircuitoIntegradoFlagPotencialInovacao(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaTopografiaDeCircuitoIntegradoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaTraducaoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDaTraducaoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDaTraducaoNatureza(Enum):
    ARTIGO = "ARTIGO"
    LIVRO = "LIVRO"
    OUTRO = "OUTRO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeArtesCenicasFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeArtesCenicasFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeArtesCenicasMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeArtesCenicasNatureza(Enum):
    AUDIOVISUAL = "AUDIOVISUAL"
    CIRCENSE = "CIRCENSE"
    COREOGRAFICA = "COREOGRAFICA"
    DIVERSAS = "DIVERSAS"
    OPERISTICA = "OPERISTICA"
    PERFORMATICA = "PERFORMATICA"
    RADIALISTICA = "RADIALISTICA"
    TEATRAL = "TEATRAL"
    OUTRA = "OUTRA"


class DadosBasicosDeArtesVisuaisFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeArtesVisuaisFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeArtesVisuaisMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeArtesVisuaisNatureza(Enum):
    INTERVENCAO_URBANA = "INTERVENCAO_URBANA"
    LIVRO_DE_ARTISTA = "LIVRO_DE_ARTISTA"
    PERFORMANCE = "PERFORMANCE"
    PINTURA = "PINTURA"
    PROGRAMACAO_VISUAL = "PROGRAMACAO_VISUAL"
    VIDEO = "VIDEO"
    WEBART = "WEBART"
    ANIMACAO = "ANIMACAO"
    INSTALACAO = "INSTALACAO"
    COMPUTACAO_GRAFICA = "COMPUTACAO_GRAFICA"
    DESENHO = "DESENHO"
    DIVERSAS = "DIVERSAS"
    ESCULTURA = "ESCULTURA"
    FILME = "FILME"
    FOTOGRAFIA = "FOTOGRAFIA"
    GRAVURA = "GRAVURA"
    ILUSTRACAO = "ILUSTRACAO"
    OUTRA = "OUTRA"


class DadosBasicosDeCartaMapaOuSimilarFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeCartaMapaOuSimilarMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeCartaMapaOuSimilarNatureza(Enum):
    AEROFOTOGRAMA = "AEROFOTOGRAMA"
    CARTA = "CARTA"
    FOTOGRAMA = "FOTOGRAMA"
    MAPA = "MAPA"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeCursosCurtaDuracaoMinistradoFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeCursosCurtaDuracaoMinistradoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeCursosCurtaDuracaoMinistradoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeCursosCurtaDuracaoMinistradoNivelDoCurso(Enum):
    EXTENSAO = "EXTENSAO"
    APERFEICOAMENTO = "APERFEICOAMENTO"
    ESPECIALIZACAO = "ESPECIALIZACAO"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeDemaisTrabalhosFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeDemaisTrabalhosMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeEditoracaoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeEditoracaoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeEditoracaoNatureza(Enum):
    LIVRO = "LIVRO"
    ANAIS = "ANAIS"
    CATALOGO = "CATALOGO"
    COLETANEA = "COLETANEA"
    ENCICLOPEDIA = "ENCICLOPEDIA"
    PERIODICO = "PERIODICO"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeManutencaoDeObraArtisticaFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeManutencaoDeObraArtisticaNatureza(Enum):
    ARQUITETURA = "ARQUITETURA"
    DESENHO = "DESENHO"
    ESCULTURA = "ESCULTURA"
    FOTOGRAFIA = "FOTOGRAFIA"
    GRAVURA = "GRAVURA"
    OUTRA = "OUTRA"
    PINTURA = "PINTURA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeManutencaoDeObraArtisticaTipo(Enum):
    CONSERVACAO = "CONSERVACAO"
    RESTAURACAO = "RESTAURACAO"
    OUTRO = "OUTRO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeOrientacoesConcluidasParaDoutoradoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOrientacoesConcluidasParaMestradoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOrientacoesConcluidasParaMestradoTipo(Enum):
    ACADEMICO = "ACADEMICO"
    PROFISSIONALIZANTE = "PROFISSIONALIZANTE"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeOrientacoesConcluidasParaPosDoutoradoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOutraProducaoArtisticaCulturalFlagDivulgacaoCientifica(
    Enum
):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOutraProducaoArtisticaCulturalFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOutraProducaoArtisticaCulturalMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeOutraProducaoTecnicaFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOutraProducaoTecnicaFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOutraProducaoTecnicaMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeOutraProducaoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOutraProducaoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


@dataclass(kw_only=True)
class DadosBasicosDeOutrasBancasJulgadoras:
    class Meta:
        name = "DADOS-BASICOS-DE-OUTRAS-BANCAS-JULGADORAS"

    tipo: None | object = field(
        default=None,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    tipo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-INGLES",
            "type": "Attribute",
        },
    )


class DadosBasicosDeOutrasOrientacoesConcluidasFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOutrasOrientacoesConcluidasNatureza(Enum):
    MONOGRAFIA_DE_CONCLUSAO_DE_CURSO_APERFEICOAMENTO_E_ESPECIALIZACAO = (
        "MONOGRAFIA_DE_CONCLUSAO_DE_CURSO_APERFEICOAMENTO_E_ESPECIALIZACAO"
    )
    TRABALHO_DE_CONCLUSAO_DE_CURSO_GRADUACAO = (
        "TRABALHO_DE_CONCLUSAO_DE_CURSO_GRADUACAO"
    )
    INICIACAO_CIENTIFICA = "INICIACAO_CIENTIFICA"
    ORIENTACAO_DE_OUTRA_NATUREZA = "ORIENTACAO-DE-OUTRA-NATUREZA"


@dataclass(kw_only=True)
class DadosBasicosDeOutrasOrientacoesEmAndamento:
    class Meta:
        name = "DADOS-BASICOS-DE-OUTRAS-ORIENTACOES-EM-ANDAMENTO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeOutrasParticipacoesEmBanca:
    class Meta:
        name = "DADOS-BASICOS-DE-OUTRAS-PARTICIPACOES-EM-BANCA"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    tipo: None | object = field(
        default=None,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    tipo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-INGLES",
            "type": "Attribute",
        },
    )


class DadosBasicosDeOutrasParticipacoesEmEventosCongressosFlagDivulgacaoCientifica(
    Enum
):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOutrasParticipacoesEmEventosCongressosFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeOutrasParticipacoesEmEventosCongressosMeioDeDivulgacao(
    Enum
):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeSonoplastiaFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDeSonoplastiaMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDeSonoplastiaNatureza(Enum):
    CINEMA = "CINEMA"
    MUSICA = "MUSICA"
    RADIO = "RADIO"
    TELEVISAO = "TELEVISAO"
    TEATRO = "TEATRO"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoArranjoMusicalFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoArranjoMusicalMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoArranjoMusicalNatureza(Enum):
    CANTO = "CANTO"
    CORAL = "CORAL"
    ORQUESTRA = "ORQUESTRA"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoArtigoFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoArtigoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoArtigoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoArtigoNatureza(Enum):
    COMPLETO = "COMPLETO"
    RESUMO = "RESUMO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoCapituloFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoCapituloFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoCapituloMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoCursoDeCurtaDuracaoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoCursoDeCurtaDuracaoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoCursoDeCurtaDuracaoNatureza(Enum):
    EXTENSAO = "EXTENSAO"
    APERFEICOAMENTO = "APERFEICOAMENTO"
    ESPECIALIZACAO = "ESPECIALIZACAO"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoDesenhoIndustrialFlagPotencialInovacao(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoDesenhoIndustrialFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoLivroFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoLivroFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoLivroMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoLivroNatureza(Enum):
    COLETANEA = "COLETANEA"
    TEXTO_INTEGRAL = "TEXTO_INTEGRAL"
    VERBETE = "VERBETE"
    ANAIS = "ANAIS"
    CATALOGO = "CATALOGO"
    ENCICLOPEDIA = "ENCICLOPEDIA"
    LIVRO = "LIVRO"
    OUTRA = "OUTRA"
    PERIODICO = "PERIODICO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoLivroTipo(Enum):
    LIVRO_PUBLICADO = "LIVRO_PUBLICADO"
    LIVRO_ORGANIZADO_OU_EDICAO = "LIVRO_ORGANIZADO_OU_EDICAO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoMaterialDidaticoOuInstrucionalFlagDivulgacaoCientifica(
    Enum
):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoMaterialDidaticoOuInstrucionalFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoMaterialDidaticoOuInstrucionalMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoPrefacioPosfacioFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoPrefacioPosfacioMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoPrefacioPosfacioNatureza(Enum):
    LIVRO = "LIVRO"
    OUTRA = "OUTRA"
    REVISTAS_OU_PERIODICOS = "REVISTAS_OU_PERIODICOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoPrefacioPosfacioTipo(Enum):
    PREFACIO = "PREFACIO"
    POSFACIO = "POSFACIO"
    APRESENTACAO = "APRESENTACAO"
    INTRODUCAO = "INTRODUCAO"


class DadosBasicosDoProcessosOuTecnicasFlagPotencialInovacao(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoProcessosOuTecnicasFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoProcessosOuTecnicasMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoProcessosOuTecnicasNatureza(Enum):
    ANALITICA = "ANALITICA"
    INSTRUMENTAL = "INSTRUMENTAL"
    PEDAGOGICA = "PEDAGOGICA"
    PROCESSUAL = "PROCESSUAL"
    TERAPEUTICA = "TERAPEUTICA"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoProdutoTecnologicoFlagPotencialInovacao(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoProdutoTecnologicoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoProdutoTecnologicoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoProdutoTecnologicoNatureza(Enum):
    APARELHO = "APARELHO"
    EQUIPAMENTO = "EQUIPAMENTO"
    FARMACOS_E_SIMILARES = "FARMACOS_E_SIMILARES"
    INSTRUMENTO = "INSTRUMENTO"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoProdutoTecnologicoTipoProduto(Enum):
    PILOTO = "PILOTO"
    PROJETO = "PROJETO"
    PROTOTIPO = "PROTOTIPO"
    OUTRO = "OUTRO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoProgramaDeRadioOuTvFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoProgramaDeRadioOuTvFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoProgramaDeRadioOuTvMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoProgramaDeRadioOuTvNatureza(Enum):
    ENTREVISTA = "ENTREVISTA"
    MESA_REDONDA = "MESA_REDONDA"
    COMENTARIO = "COMENTARIO"
    PROGRAMA = "PROGRAMA"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoRelatorioDePesquisaFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoRelatorioDePesquisaMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoSoftwareFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoSoftwareFlagPotencialInovacao(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoSoftwareFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoSoftwareMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoSoftwareNatureza(Enum):
    COMPUTACIONAL = "COMPUTACIONAL"
    MULTIMIDIA = "MULTIMIDIA"
    OUTRO = "OUTRO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoTextoFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoTextoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoTextoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoTextoNatureza(Enum):
    JORNAL_DE_NOTICIAS = "JORNAL_DE_NOTICIAS"
    REVISTA_MAGAZINE = "REVISTA_MAGAZINE"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoTrabalhoTecnicoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoTrabalhoTecnicoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoTrabalhoTecnicoNatureza(Enum):
    ASSESSORIA = "ASSESSORIA"
    CONSULTORIA = "CONSULTORIA"
    PARECER = "PARECER"
    ELABORACAO_DE_PROJETO = "ELABORACAO_DE_PROJETO"
    RELATORIO_TECNICO = "RELATORIO_TECNICO"
    SERVICOS_NA_AREA_DA_SAUDE = "SERVICOS_NA_AREA_DA_SAUDE"
    EXTENSAO_TECNOLOGICA = "EXTENSAO_TECNOLOGICA"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoTrabalhoFlagDivulgacaoCientifica(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoTrabalhoFlagRelevancia(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosBasicosDoTrabalhoMeioDeDivulgacao(Enum):
    IMPRESSO = "IMPRESSO"
    WEB = "WEB"
    MEIO_MAGNETICO = "MEIO_MAGNETICO"
    MEIO_DIGITAL = "MEIO_DIGITAL"
    FILME = "FILME"
    HIPERTEXTO = "HIPERTEXTO"
    OUTRO = "OUTRO"
    VARIOS = "VARIOS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosBasicosDoTrabalhoNatureza(Enum):
    COMPLETO = "COMPLETO"
    RESUMO = "RESUMO"
    RESUMO_EXPANDIDO = "RESUMO_EXPANDIDO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DadosGeraisFormatoDataDeEmissao(Enum):
    DDMMAAAA = "DDMMAAAA"


class DadosGeraisFormatoDataDeNascimento(Enum):
    DDMMAAAA = "DDMMAAAA"


class DadosGeraisPermissaoDeDivulgacao(Enum):
    SIM = "SIM"
    NAO = "NAO"


class DadosGeraisSexo(Enum):
    MASCULINO = "MASCULINO"
    FEMININO = "FEMININO"


class DetalhamentoDaApresentacaoDeObraArtisticaAtividadeDosAutores(Enum):
    CANTO = "CANTO"
    CRIACAO = "CRIACAO"
    DANCA = "DANCA"
    DIRECAO = "DIRECAO"
    ENCENACAO = "ENCENACAO"
    INSTRUMENTO_MUSICAL = "INSTRUMENTO_MUSICAL"
    REGENCIA = "REGENCIA"
    ROTEIRO = "ROTEIRO"
    OUTRA = "OUTRA"
    VARIAS = "VARIAS"
    NAO_INFORMADO = "NAO_INFORMADO"


class DetalhamentoDaApresentacaoDeObraArtisticaTipoDeEvento(Enum):
    CONCERTO = "CONCERTO"
    CONCURSO = "CONCURSO"
    FESTIVAL = "FESTIVAL"
    GRAVACAO = "GRAVACAO"
    RECITAL = "RECITAL"
    OUTRO = "OUTRO"
    NAO_INFORMADO = "NAO_INFORMADO"


@dataclass(kw_only=True)
class DetalhamentoDaApresentacaoDeTrabalho:
    class Meta:
        name = "DETALHAMENTO-DA-APRESENTACAO-DE-TRABALHO"

    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    instituicao_promotora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA",
            "type": "Attribute",
        },
    )
    local_da_apresentacao: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DA-APRESENTACAO",
            "type": "Attribute",
        },
    )
    cidade_da_apresentacao: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DA-APRESENTACAO",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


class DetalhamentoDaApresentacaoEmRadioOuTvFormatoDataDeApresentacao(Enum):
    DDMMAAAA = "DDMMAAAA"


@dataclass(kw_only=True)
class DetalhamentoDaBancaJulgadoraParaAvaliacaoCursos:
    class Meta:
        name = "DETALHAMENTO-DA-BANCA-JULGADORA-PARA-AVALIACAO-CURSOS"

    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaBancaJulgadoraParaConcursoPublico:
    class Meta:
        name = "DETALHAMENTO-DA-BANCA-JULGADORA-PARA-CONCURSO-PUBLICO"

    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaBancaJulgadoraParaLivreDocencia:
    class Meta:
        name = "DETALHAMENTO-DA-BANCA-JULGADORA-PARA-LIVRE-DOCENCIA"

    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaBancaJulgadoraParaProfessorTitular:
    class Meta:
        name = "DETALHAMENTO-DA-BANCA-JULGADORA-PARA-PROFESSOR-TITULAR"

    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaComposicaoMusical:
    class Meta:
        name = "DETALHAMENTO-DA-COMPOSICAO-MUSICAL"

    formacao_instrumental: None | object = field(
        default=None,
        metadata={
            "name": "FORMACAO-INSTRUMENTAL",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    registro_de_direito_autoral: None | object = field(
        default=None,
        metadata={
            "name": "REGISTRO-DE-DIREITO-AUTORAL",
            "type": "Attribute",
        },
    )
    premiacao: None | object = field(
        default=None,
        metadata={
            "name": "PREMIACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaMaquete:
    class Meta:
        name = "DETALHAMENTO-DA-MAQUETE"

    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    objeto_representado: None | object = field(
        default=None,
        metadata={
            "name": "OBJETO-REPRESENTADO",
            "type": "Attribute",
        },
    )
    material_utilizado: None | object = field(
        default=None,
        metadata={
            "name": "MATERIAL-UTILIZADO",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaMidiaSocialWebsiteBlog:
    class Meta:
        name = "DETALHAMENTO-DA-MIDIA-SOCIAL-WEBSITE-BLOG"

    tema: None | object = field(
        default=None,
        metadata={
            "name": "TEMA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaMusica:
    class Meta:
        name = "DETALHAMENTO-DA-MUSICA"

    tipo_de_evento: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-DE-EVENTO",
            "type": "Attribute",
        },
    )
    atividade_dos_autores: None | object = field(
        default=None,
        metadata={
            "name": "ATIVIDADE-DOS-AUTORES",
            "type": "Attribute",
        },
    )
    formacao_instrumental: None | object = field(
        default=None,
        metadata={
            "name": "FORMACAO-INSTRUMENTAL",
            "type": "Attribute",
        },
    )
    flag_ineditismo_da_obra: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-INEDITISMO-DA-OBRA",
            "type": "Attribute",
        },
    )
    data_estreia: None | object = field(
        default=None,
        metadata={
            "name": "DATA-ESTREIA",
            "type": "Attribute",
        },
    )
    data_encerramento: None | object = field(
        default=None,
        metadata={
            "name": "DATA-ENCERRAMENTO",
            "type": "Attribute",
        },
    )
    local_de_estreia: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DE-ESTREIA",
            "type": "Attribute",
        },
    )
    premiacao: None | object = field(
        default=None,
        metadata={
            "name": "PREMIACAO",
            "type": "Attribute",
        },
    )
    instituicao_promotora_do_premio: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA-DO-PREMIO",
            "type": "Attribute",
        },
    )
    obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    autor_da_obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "AUTOR-DA-OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    ano_da_obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DA-OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    duracao: None | object = field(
        default=None,
        metadata={
            "name": "DURACAO",
            "type": "Attribute",
        },
    )
    temporada: None | object = field(
        default=None,
        metadata={
            "name": "TEMPORADA",
            "type": "Attribute",
        },
    )
    instituicao_promotora_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA-DO-EVENTO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )


class DetalhamentoDaObraDeArtesVisuaisAcervo(Enum):
    PUBLICO = "PUBLICO"
    PRIVADO = "PRIVADO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DetalhamentoDaObraDeArtesVisuaisTipoDeEvento(Enum):
    APRESENTACAO = "APRESENTACAO"
    CONCURSO = "CONCURSO"
    CRIACAO = "CRIACAO"
    EXPOSICAO = "EXPOSICAO"
    FESTIVAL = "FESTIVAL"
    OUTRO = "OUTRO"
    NAO_INFORMADO = "NAO_INFORMADO"


@dataclass(kw_only=True)
class DetalhamentoDaOrganizacaoDeEvento:
    class Meta:
        name = "DETALHAMENTO-DA-ORGANIZACAO-DE-EVENTO"

    instituicao_promotora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA",
            "type": "Attribute",
        },
    )
    duracao_em_semanas: None | object = field(
        default=None,
        metadata={
            "name": "DURACAO-EM-SEMANAS",
            "type": "Attribute",
        },
    )
    flag_evento_itinerante: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-EVENTO-ITINERANTE",
            "type": "Attribute",
        },
    )
    flag_catalogo: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-CATALOGO",
            "type": "Attribute",
        },
    )
    local: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaOrientacaoEmAndamentoDeAperfeicoamentoEspecializacao:
    class Meta:
        name = "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-APERFEICOAMENTO-ESPECIALIZACAO"

    nome_do_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTANDO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_id_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTANDO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


class DetalhamentoDaOrientacaoEmAndamentoDeDoutoradoTipoDeOrientacao(Enum):
    ORIENTADOR_PRINCIPAL = "ORIENTADOR_PRINCIPAL"
    CO_ORIENTADOR = "CO_ORIENTADOR"


@dataclass(kw_only=True)
class DetalhamentoDaOrientacaoEmAndamentoDeGraduacao:
    class Meta:
        name = "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-GRADUACAO"

    nome_do_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTANDO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_id_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTANDO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaOrientacaoEmAndamentoDeIniciacaoCientifica:
    class Meta:
        name = (
            "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-INICIACAO-CIENTIFICA"
        )

    nome_do_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTANDO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_id_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTANDO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


class DetalhamentoDaOrientacaoEmAndamentoDeMestradoTipoDeOrientacao(Enum):
    ORIENTADOR_PRINCIPAL = "ORIENTADOR_PRINCIPAL"
    CO_ORIENTADOR = "CO_ORIENTADOR"


@dataclass(kw_only=True)
class DetalhamentoDaOrientacaoEmAndamentoDePosDoutorado:
    class Meta:
        name = "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-POS-DOUTORADO"

    tipo_de_orientacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-DE-ORIENTACAO",
            "type": "Attribute",
        },
    )
    nome_do_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTANDO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_id_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTANDO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmBancaDeAperfeicoamentoEspecializacao:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-BANCA-DE-APERFEICOAMENTO-ESPECIALIZACAO"

    nome_do_candidato: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CANDIDATO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmBancaDeDoutorado:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-BANCA-DE-DOUTORADO"

    nome_do_candidato: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CANDIDATO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmBancaDeExameQualificacao:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-BANCA-DE-EXAME-QUALIFICACAO"

    nome_do_candidato: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CANDIDATO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmBancaDeGraduacao:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-BANCA-DE-GRADUACAO"

    nome_do_candidato: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CANDIDATO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmBancaDeMestrado:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-BANCA-DE-MESTRADO"

    nome_do_candidato: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CANDIDATO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmCongresso:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-CONGRESSO"

    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmEncontro:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-ENCONTRO"

    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmExposicao:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-EXPOSICAO"

    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmFeira:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-FEIRA"

    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmOficina:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-OFICINA"

    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmOlimpiada:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-OLIMPIADA"

    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmSeminario:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-SEMINARIO"

    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaParticipacaoEmSimposio:
    class Meta:
        name = "DETALHAMENTO-DA-PARTICIPACAO-EM-SIMPOSIO"

    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaPartitura:
    class Meta:
        name = "DETALHAMENTO-DA-PARTITURA"

    formacao_instrumental: None | object = field(
        default=None,
        metadata={
            "name": "FORMACAO-INSTRUMENTAL",
            "type": "Attribute",
        },
    )
    editora: None | object = field(
        default=None,
        metadata={
            "name": "EDITORA",
            "type": "Attribute",
        },
    )
    cidade_da_editora: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DA-EDITORA",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    numero_do_catalogo: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DO-CATALOGO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaTraducao:
    class Meta:
        name = "DETALHAMENTO-DA-TRADUCAO"

    nome_do_autor_traduzido: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-AUTOR-TRADUZIDO",
            "type": "Attribute",
        },
    )
    titulo_da_obra_original: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-OBRA-ORIGINAL",
            "type": "Attribute",
        },
    )
    issn_isbn: None | object = field(
        default=None,
        metadata={
            "name": "ISSN-ISBN",
            "type": "Attribute",
        },
    )
    idioma_da_obra_original: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA-DA-OBRA-ORIGINAL",
            "type": "Attribute",
        },
    )
    editora_da_traducao: None | object = field(
        default=None,
        metadata={
            "name": "EDITORA-DA-TRADUCAO",
            "type": "Attribute",
        },
    )
    cidade_da_editora: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DA-EDITORA",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    numero_da_edicao_revisao: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DA-EDICAO-REVISAO",
            "type": "Attribute",
        },
    )
    volume: None | object = field(
        default=None,
        metadata={
            "name": "VOLUME",
            "type": "Attribute",
        },
    )
    fasciculo: None | object = field(
        default=None,
        metadata={
            "name": "FASCICULO",
            "type": "Attribute",
        },
    )
    serie: None | object = field(
        default=None,
        metadata={
            "name": "SERIE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeArtesCenicas:
    class Meta:
        name = "DETALHAMENTO-DE-ARTES-CENICAS"

    tipo_de_evento: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-DE-EVENTO",
            "type": "Attribute",
        },
    )
    atividade_dos_autores: None | object = field(
        default=None,
        metadata={
            "name": "ATIVIDADE-DOS-AUTORES",
            "type": "Attribute",
        },
    )
    data_estreia: None | object = field(
        default=None,
        metadata={
            "name": "DATA-ESTREIA",
            "type": "Attribute",
        },
    )
    data_encerramento: None | object = field(
        default=None,
        metadata={
            "name": "DATA-ENCERRAMENTO",
            "type": "Attribute",
        },
    )
    local_de_estreia: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DE-ESTREIA",
            "type": "Attribute",
        },
    )
    premiacao: None | object = field(
        default=None,
        metadata={
            "name": "PREMIACAO",
            "type": "Attribute",
        },
    )
    instituicao_promotora_do_premio: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA-DO-PREMIO",
            "type": "Attribute",
        },
    )
    obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    autor_da_obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "AUTOR-DA-OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    ano_da_obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DA-OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    duracao: None | object = field(
        default=None,
        metadata={
            "name": "DURACAO",
            "type": "Attribute",
        },
    )
    temporada: None | object = field(
        default=None,
        metadata={
            "name": "TEMPORADA",
            "type": "Attribute",
        },
    )
    instituicao_promotora_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA-DO-EVENTO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    flag_itinerante: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-ITINERANTE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeArtesVisuais:
    class Meta:
        name = "DETALHAMENTO-DE-ARTES-VISUAIS"

    premiacao: None | object = field(
        default=None,
        metadata={
            "name": "PREMIACAO",
            "type": "Attribute",
        },
    )
    atividade_dos_autores: None | object = field(
        default=None,
        metadata={
            "name": "ATIVIDADE-DOS-AUTORES",
            "type": "Attribute",
        },
    )
    instituicao_promotora_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA-DO-EVENTO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    temporada: None | object = field(
        default=None,
        metadata={
            "name": "TEMPORADA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeCartaMapaOuSimilar:
    class Meta:
        name = "DETALHAMENTO-DE-CARTA-MAPA-OU-SIMILAR"

    tema_da_carta_mapa_ou_similar: None | object = field(
        default=None,
        metadata={
            "name": "TEMA-DA-CARTA-MAPA-OU-SIMILAR",
            "type": "Attribute",
        },
    )
    tecnica_utilizada: None | object = field(
        default=None,
        metadata={
            "name": "TECNICA-UTILIZADA",
            "type": "Attribute",
        },
    )
    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    area_representada: None | object = field(
        default=None,
        metadata={
            "name": "AREA-REPRESENTADA",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


class DetalhamentoDeCursosCurtaDuracaoMinistradoParticipacaoDosAutores(Enum):
    DOCENTE = "DOCENTE"
    ORGANIZADOR = "ORGANIZADOR"
    OUTRA = "OUTRA"
    NAO_INFORMADO = "NAO_INFORMADO"


@dataclass(kw_only=True)
class DetalhamentoDeDemaisTrabalhos:
    class Meta:
        name = "DETALHAMENTO-DE-DEMAIS-TRABALHOS"

    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    local: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeEditoracao:
    class Meta:
        name = "DETALHAMENTO-DE-EDITORACAO"

    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    instituicao_promotora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA",
            "type": "Attribute",
        },
    )
    editora: None | object = field(
        default=None,
        metadata={
            "name": "EDITORA",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )


class DetalhamentoDeManutencaoDeObraArtisticaAcervo(Enum):
    PUBLICO = "PUBLICO"
    PRIVADO = "PRIVADO"
    NAO_INFORMADO = "NAO_INFORMADO"


class DetalhamentoDeOrientacoesConcluidasParaDoutoradoTipoDeOrientacao(Enum):
    ORIENTADOR_PRINCIPAL = "ORIENTADOR_PRINCIPAL"
    CO_ORIENTADOR = "CO_ORIENTADOR"


class DetalhamentoDeOrientacoesConcluidasParaMestradoTipoDeOrientacao(Enum):
    ORIENTADOR_PRINCIPAL = "ORIENTADOR_PRINCIPAL"
    CO_ORIENTADOR = "CO_ORIENTADOR"


@dataclass(kw_only=True)
class DetalhamentoDeOrientacoesConcluidasParaPosDoutorado:
    class Meta:
        name = "DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO"

    tipo_de_orientacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-DE-ORIENTACAO",
            "type": "Attribute",
        },
    )
    nome_do_orientado: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTADO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_da_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_do_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    numero_id_orientado: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTADO",
            "type": "Attribute",
        },
    )
    nome_do_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeOutraProducao:
    class Meta:
        name = "DETALHAMENTO-DE-OUTRA-PRODUCAO"

    editora: None | object = field(
        default=None,
        metadata={
            "name": "EDITORA",
            "type": "Attribute",
        },
    )
    cidade_da_editora: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DA-EDITORA",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    issn_isbn: None | object = field(
        default=None,
        metadata={
            "name": "ISSN-ISBN",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeOutraProducaoArtisticaCultural:
    class Meta:
        name = "DETALHAMENTO-DE-OUTRA-PRODUCAO-ARTISTICA-CULTURAL"

    instituicao_promotora_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA-DO-EVENTO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )
    exposicao: None | object = field(
        default=None,
        metadata={
            "name": "EXPOSICAO",
            "type": "Attribute",
        },
    )
    premiacao: None | object = field(
        default=None,
        metadata={
            "name": "PREMIACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeOutraProducaoTecnica:
    class Meta:
        name = "DETALHAMENTO-DE-OUTRA-PRODUCAO-TECNICA"

    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    instituicao_promotora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA",
            "type": "Attribute",
        },
    )
    local: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeOutrasBancasJulgadoras:
    class Meta:
        name = "DETALHAMENTO-DE-OUTRAS-BANCAS-JULGADORAS"

    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeOutrasOrientacoesConcluidas:
    class Meta:
        name = "DETALHAMENTO-DE-OUTRAS-ORIENTACOES-CONCLUIDAS"

    nome_do_orientado: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTADO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_da_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_do_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    tipo_de_orientacao_concluida: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-DE-ORIENTACAO-CONCLUIDA",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    numero_id_orientado: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTADO",
            "type": "Attribute",
        },
    )
    nome_do_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeOutrasOrientacoesEmAndamento:
    class Meta:
        name = "DETALHAMENTO-DE-OUTRAS-ORIENTACOES-EM-ANDAMENTO"

    nome_do_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTANDO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_id_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTANDO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeOutrasParticipacoesEmBanca:
    class Meta:
        name = "DETALHAMENTO-DE-OUTRAS-PARTICIPACOES-EM-BANCA"

    nome_do_candidato: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CANDIDATO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeOutrasParticipacoesEmEventosCongressos:
    class Meta:
        name = "DETALHAMENTO-DE-OUTRAS-PARTICIPACOES-EM-EVENTOS-CONGRESSOS"

    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeSonoplastia:
    class Meta:
        name = "DETALHAMENTO-DE-SONOPLASTIA"

    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    premiacao: None | object = field(
        default=None,
        metadata={
            "name": "PREMIACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoArranjoMusical:
    class Meta:
        name = "DETALHAMENTO-DO-ARRANJO-MUSICAL"

    autor_da_obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "AUTOR-DA-OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    ano_da_obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DA-OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    formacao_instrumental: None | object = field(
        default=None,
        metadata={
            "name": "FORMACAO-INSTRUMENTAL",
            "type": "Attribute",
        },
    )
    registro_de_direito_autoral: None | object = field(
        default=None,
        metadata={
            "name": "REGISTRO-DE-DIREITO-AUTORAL",
            "type": "Attribute",
        },
    )
    premiacao: None | object = field(
        default=None,
        metadata={
            "name": "PREMIACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoArtigo:
    class Meta:
        name = "DETALHAMENTO-DO-ARTIGO"

    titulo_do_periodico_ou_revista: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-PERIODICO-OU-REVISTA",
            "type": "Attribute",
        },
    )
    issn: None | object = field(
        default=None,
        metadata={
            "name": "ISSN",
            "type": "Attribute",
        },
    )
    volume: None | object = field(
        default=None,
        metadata={
            "name": "VOLUME",
            "type": "Attribute",
        },
    )
    fasciculo: None | object = field(
        default=None,
        metadata={
            "name": "FASCICULO",
            "type": "Attribute",
        },
    )
    serie: None | object = field(
        default=None,
        metadata={
            "name": "SERIE",
            "type": "Attribute",
        },
    )
    pagina_inicial: None | object = field(
        default=None,
        metadata={
            "name": "PAGINA-INICIAL",
            "type": "Attribute",
        },
    )
    pagina_final: None | object = field(
        default=None,
        metadata={
            "name": "PAGINA-FINAL",
            "type": "Attribute",
        },
    )
    local_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoCapitulo:
    class Meta:
        name = "DETALHAMENTO-DO-CAPITULO"

    titulo_do_livro: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-LIVRO",
            "type": "Attribute",
        },
    )
    numero_de_volumes: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-VOLUMES",
            "type": "Attribute",
        },
    )
    pagina_inicial: None | object = field(
        default=None,
        metadata={
            "name": "PAGINA-INICIAL",
            "type": "Attribute",
        },
    )
    pagina_final: None | object = field(
        default=None,
        metadata={
            "name": "PAGINA-FINAL",
            "type": "Attribute",
        },
    )
    isbn: None | object = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Attribute",
        },
    )
    organizadores: None | object = field(
        default=None,
        metadata={
            "name": "ORGANIZADORES",
            "type": "Attribute",
        },
    )
    numero_da_edicao_revisao: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DA-EDICAO-REVISAO",
            "type": "Attribute",
        },
    )
    numero_da_serie: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DA-SERIE",
            "type": "Attribute",
        },
    )
    cidade_da_editora: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DA-EDITORA",
            "type": "Attribute",
        },
    )
    nome_da_editora: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-EDITORA",
            "type": "Attribute",
        },
    )


class DetalhamentoDoCursoDeCurtaDuracaoUnidade(Enum):
    SEMANAS = "SEMANAS"
    DIAS = "DIAS"
    HORAS = "HORAS"
    NAO_INFORMADO = "NAO_INFORMADO"


@dataclass(kw_only=True)
class DetalhamentoDoLivro:
    class Meta:
        name = "DETALHAMENTO-DO-LIVRO"

    numero_de_volumes: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-VOLUMES",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    isbn: None | object = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Attribute",
        },
    )
    numero_da_edicao_revisao: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DA-EDICAO-REVISAO",
            "type": "Attribute",
        },
    )
    numero_da_serie: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DA-SERIE",
            "type": "Attribute",
        },
    )
    cidade_da_editora: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DA-EDITORA",
            "type": "Attribute",
        },
    )
    nome_da_editora: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-EDITORA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoMaterialDidaticoOuInstrucional:
    class Meta:
        name = "DETALHAMENTO-DO-MATERIAL-DIDATICO-OU-INSTRUCIONAL"

    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoPrefacioPosfacio:
    class Meta:
        name = "DETALHAMENTO-DO-PREFACIO-POSFACIO"

    nome_do_autor_da_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-AUTOR-DA-PUBLICACAO",
            "type": "Attribute",
        },
    )
    titulo_da_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-PUBLICACAO",
            "type": "Attribute",
        },
    )
    issn_isbn: None | object = field(
        default=None,
        metadata={
            "name": "ISSN-ISBN",
            "type": "Attribute",
        },
    )
    numero_da_edicao_revisao: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DA-EDICAO-REVISAO",
            "type": "Attribute",
        },
    )
    volume: None | object = field(
        default=None,
        metadata={
            "name": "VOLUME",
            "type": "Attribute",
        },
    )
    serie: None | object = field(
        default=None,
        metadata={
            "name": "SERIE",
            "type": "Attribute",
        },
    )
    fasciculo: None | object = field(
        default=None,
        metadata={
            "name": "FASCICULO",
            "type": "Attribute",
        },
    )
    editora_do_prefacio_posfacio: None | object = field(
        default=None,
        metadata={
            "name": "EDITORA-DO-PREFACIO-POSFACIO",
            "type": "Attribute",
        },
    )
    cidade_da_editora: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DA-EDITORA",
            "type": "Attribute",
        },
    )


class DetalhamentoDoProgramaDeRadioOuTvFormatoDataDaApresentacao(Enum):
    DDMMAAAA = "DDMMAAAA"


@dataclass(kw_only=True)
class DetalhamentoDoRelatorioDePesquisa:
    class Meta:
        name = "DETALHAMENTO-DO-RELATORIO-DE-PESQUISA"

    nome_do_projeto: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-PROJETO",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    disponibilidade: None | object = field(
        default=None,
        metadata={
            "name": "DISPONIBILIDADE",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )


class DetalhamentoDoSoftwareDisponibilidade(Enum):
    RESTRITA = "RESTRITA"
    IRRESTRITA = "IRRESTRITA"
    NAO_INFORMADO = "NAO_INFORMADO"


class DetalhamentoDoTextoFormatoDataDePublicacao(Enum):
    DDMMAAAA = "DDMMAAAA"


@dataclass(kw_only=True)
class DetalhamentoDoTrabalhoTecnico:
    class Meta:
        name = "DETALHAMENTO-DO-TRABALHO-TECNICO"

    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    duracao_em_meses: None | object = field(
        default=None,
        metadata={
            "name": "DURACAO-EM-MESES",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    disponibilidade: None | object = field(
        default=None,
        metadata={
            "name": "DISPONIBILIDADE",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )
    cidade_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


class DetalhamentoDoTrabalhoClassificacaoDoEvento(Enum):
    INTERNACIONAL = "INTERNACIONAL"
    NACIONAL = "NACIONAL"
    REGIONAL = "REGIONAL"
    LOCAL = "LOCAL"
    NAO_INFORMADO = "NAO_INFORMADO"


class DirecaoEAdministracaoFlagPeriodo(Enum):
    ANTERIOR = "ANTERIOR"
    ATUAL = "ATUAL"


class DirecaoEAdministracaoFormatoCargoOuFuncao(Enum):
    CHEFE_DE_DEPARTMENTO = "CHEFE_DE_DEPARTMENTO"
    COORDENADOR_DE_CURSO = "COORDENADOR_DE_CURSO"
    COORDENADOR_DE_PROGRAMA = "COORDENADOR_DE_PROGRAMA"
    DECANO_DE_CENTRO = "DECANO_DE_CENTRO"
    DIRETOR_DE_UNIDADE = "DIRETOR_DE_UNIDADE"
    MEMBRO_DE_COLEGIADO_SUPERIOR = "MEMBRO_DE_COLEGIADO_SUPERIOR"
    MEMBRO_DE_COMISSAO_PERMANENTE = "MEMBRO_DE_COMISSAO_PERMANENTE"
    MEMBRO_DE_COMISSAO_TEMPORARIA = "MEMBRO_DE_COMISSAO_TEMPORARIA"
    MEMBRO_DE_CONSELHO_DE_CENTRO = "MEMBRO_DE_CONSELHO_DE_CENTRO"
    MEMBRO_DE_CONSELHO_DE_UNIDADE = "MEMBRO_DE_CONSELHO_DE_UNIDADE"
    REITOR = "REITOR"
    VICE_REITOR_OU_PRO_REITOR = "VICE_REITOR_OU_PRO_REITOR"
    OUTRO = "OUTRO"
    LIVRE = "LIVRE"


@dataclass(kw_only=True)
class Disciplina:
    class Meta:
        name = "DISCIPLINA"

    sequencia_especificacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-ESPECIFICACAO",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


class DoutoradoStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


@dataclass(kw_only=True)
class EnderecoProfissional:
    class Meta:
        name = "ENDERECO-PROFISSIONAL"

    codigo_instituicao_empresa: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-EMPRESA",
            "type": "Attribute",
        },
    )
    nome_instituicao_empresa: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO-EMPRESA",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_unidade: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-UNIDADE",
            "type": "Attribute",
        },
    )
    nome_unidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-UNIDADE",
            "type": "Attribute",
        },
    )
    logradouro_complemento: None | object = field(
        default=None,
        metadata={
            "name": "LOGRADOURO-COMPLEMENTO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    uf: None | object = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Attribute",
        },
    )
    cep: None | object = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )
    bairro: None | object = field(
        default=None,
        metadata={
            "name": "BAIRRO",
            "type": "Attribute",
        },
    )
    ddd: None | object = field(
        default=None,
        metadata={
            "name": "DDD",
            "type": "Attribute",
        },
    )
    telefone: None | object = field(
        default=None,
        metadata={
            "name": "TELEFONE",
            "type": "Attribute",
        },
    )
    ramal: None | object = field(
        default=None,
        metadata={
            "name": "RAMAL",
            "type": "Attribute",
        },
    )
    fax: None | object = field(
        default=None,
        metadata={
            "name": "FAX",
            "type": "Attribute",
        },
    )
    caixa_postal: None | object = field(
        default=None,
        metadata={
            "name": "CAIXA-POSTAL",
            "type": "Attribute",
        },
    )
    e_mail: None | object = field(
        default=None,
        metadata={
            "name": "E-MAIL",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EnderecoResidencial:
    class Meta:
        name = "ENDERECO-RESIDENCIAL"

    logradouro: None | object = field(
        default=None,
        metadata={
            "name": "LOGRADOURO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    uf: None | object = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Attribute",
        },
    )
    cep: None | object = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )
    bairro: None | object = field(
        default=None,
        metadata={
            "name": "BAIRRO",
            "type": "Attribute",
        },
    )
    ddd: None | object = field(
        default=None,
        metadata={
            "name": "DDD",
            "type": "Attribute",
        },
    )
    telefone: None | object = field(
        default=None,
        metadata={
            "name": "TELEFONE",
            "type": "Attribute",
        },
    )
    ramal: None | object = field(
        default=None,
        metadata={
            "name": "RAMAL",
            "type": "Attribute",
        },
    )
    fax: None | object = field(
        default=None,
        metadata={
            "name": "FAX",
            "type": "Attribute",
        },
    )
    caixa_postal: None | object = field(
        default=None,
        metadata={
            "name": "CAIXA-POSTAL",
            "type": "Attribute",
        },
    )
    e_mail: None | object = field(
        default=None,
        metadata={
            "name": "E-MAIL",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )


class EnderecoFlagDePreferencia(Enum):
    ENDERECO_INSTITUCIONAL = "ENDERECO_INSTITUCIONAL"
    ENDERECO_RESIDENCIAL = "ENDERECO_RESIDENCIAL"


class EnsinoFundamentalPrimeiroGrauStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


class EnsinoMedioSegundoGrauStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


class EnsinoFlagPeriodo(Enum):
    ANTERIOR = "ANTERIOR"
    ATUAL = "ATUAL"


class EnsinoTipoEnsino(Enum):
    GRADUACAO = "GRADUACAO"
    POS_GRADUACAO = "POS-GRADUACAO"
    ESPECIALIZACAO = "ESPECIALIZACAO"
    APERFEICOAMENTO = "APERFEICOAMENTO"
    ENSINO_FUNDAMENTAL = "ENSINO-FUNDAMENTAL"
    ENSINO_MEDIO = "ENSINO-MEDIO"
    OUTRO = "OUTRO"


class EspecializacaoStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


class EstagioFlagPeriodo(Enum):
    ANTERIOR = "ANTERIOR"
    ATUAL = "ATUAL"


class ExtensaoUniversitariaFlagPeriodo(Enum):
    ANTERIOR = "ANTERIOR"
    ATUAL = "ATUAL"


class FinanciadorDoProjetoNatureza(Enum):
    BOLSA = "BOLSA"
    AUXILIO_FINANCEIRO = "AUXILIO_FINANCEIRO"
    REMUNERACAO = "REMUNERACAO"
    OUTRO = "OUTRO"
    COOPERACAO = "COOPERACAO"
    NAO_INFORMADO = "NAO_INFORMADO"


class FormacaoComplementarCursoDeCurtaDuracaoStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


class FormacaoComplementarDeExtensaoUniversitariaStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


class GraduacaoStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


class HistoricoSituacoesPatenteFormatoDataSituacaoPatente(Enum):
    DDMMAAAA = "DDMMAAAA"


class HistoricoSituacoesPatenteStatusSituacaoPatente(Enum):
    SIM = "SIM"
    NAO = "NAO"


class IdiomaProficienciaDeCompreensao(Enum):
    POUCO = "POUCO"
    RAZOAVELMENTE = "RAZOAVELMENTE"
    BEM = "BEM"
    NAO_INFORMADO = "NAO_INFORMADO"


class IdiomaProficienciaDeEscrita(Enum):
    POUCO = "POUCO"
    RAZOAVELMENTE = "RAZOAVELMENTE"
    BEM = "BEM"
    NAO_INFORMADO = "NAO_INFORMADO"


class IdiomaProficienciaDeFala(Enum):
    POUCO = "POUCO"
    RAZOAVELMENTE = "RAZOAVELMENTE"
    BEM = "BEM"
    NAO_INFORMADO = "NAO_INFORMADO"


class IdiomaProficienciaDeLeitura(Enum):
    POUCO = "POUCO"
    RAZOAVELMENTE = "RAZOAVELMENTE"
    BEM = "BEM"
    NAO_INFORMADO = "NAO_INFORMADO"


class InformacaoAdicionalCursoNivelCurso(Enum):
    APERFEICOAMENTO_ESPECIALIZACAO = "APERFEICOAMENTO_ESPECIALIZACAO"
    APERFEICOAMENTO = "APERFEICOAMENTO"
    CURSO_DE_CURTA_DURACAO = "CURSO_DE_CURTA_DURACAO"
    ESPECIALIZACAO = "ESPECIALIZACAO"
    ESTAGIO = "ESTAGIO"
    EXTENSAO_UNIVERSITARIA = "EXTENSAO_UNIVERSITARIA"
    DOUTORADO = "DOUTORADO"
    GRADUACAO = "GRADUACAO"
    MESTRADO = "MESTRADO"
    MESTRADO_DOUTORADO = "MESTRADO_DOUTORADO"
    OT = "OT"
    OUTRO = "OUTRO"


class InformacaoAdicionalCursoNomeGrandeAreaDoConhecimento(Enum):
    OUTROS = "OUTROS"
    LINGUISTICA_LETRAS_E_ARTES = "LINGUISTICA_LETRAS_E_ARTES"
    CIENCIAS_HUMANAS = "CIENCIAS_HUMANAS"
    CIENCIAS_SOCIAIS_APLICADAS = "CIENCIAS_SOCIAIS_APLICADAS"
    CIENCIAS_AGRARIAS = "CIENCIAS_AGRARIAS"
    CIENCIAS_DA_SAUDE = "CIENCIAS_DA_SAUDE"
    ENGENHARIAS = "ENGENHARIAS"
    CIENCIAS_BIOLOGICAS = "CIENCIAS_BIOLOGICAS"
    CIENCIAS_EXATAS_E_DA_TERRA = "CIENCIAS_EXATAS_E_DA_TERRA"
    NAO_INFORMADO = "NAO_INFORMADO"


class InformacaoAdicionalInstituicaoFlagAgenciaFomento(Enum):
    SIM = "SIM"
    NAO = "NAO"


class InformacaoAdicionalInstituicaoFlagInstituicaoDeEnsino(Enum):
    SIM = "SIM"
    NAO = "NAO"


@dataclass(kw_only=True)
class InformacoesAdicionais:
    class Meta:
        name = "INFORMACOES-ADICIONAIS"

    descricao_informacoes_adicionais: None | object = field(
        default=None,
        metadata={
            "name": "DESCRICAO-INFORMACOES-ADICIONAIS",
            "type": "Attribute",
        },
    )
    descricao_informacoes_adicionais_ingles: None | object = field(
        default=None,
        metadata={
            "name": "DESCRICAO-INFORMACOES-ADICIONAIS-INGLES",
            "type": "Attribute",
        },
    )


class IntegrantesDoProjetoFlagResponsavel(Enum):
    SIM = "SIM"
    NAO = "NAO"


class LicencaFormatoDataFimLicenca(Enum):
    DDMMAAAA = "DDMMAAAA"


class LicencaFormatoDataInicioLicenca(Enum):
    DDMMAAAA = "DDMMAAAA"


class LicencaTipoLicenca(Enum):
    MATERNIDADE = "MATERNIDADE"


class LinhaDePesquisaFlagLinhaDePesquisaAtiva(Enum):
    SIM = "SIM"
    NAO = "NAO"


class MbaStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


class MestradoProfissionalizanteStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


class MestradoStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


@dataclass(kw_only=True)
class Orientacao:
    class Meta:
        name = "ORIENTACAO"

    sequencia_orientacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-ORIENTACAO",
            "type": "Attribute",
        },
    )
    titulo_orientacao: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-ORIENTACAO",
            "type": "Attribute",
        },
    )
    tipo_orientacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-ORIENTACAO",
            "type": "Attribute",
        },
    )
    titulo_orientacao_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-ORIENTACAO-INGLES",
            "type": "Attribute",
        },
    )


class OutraAtividadeTecnicoCientificaFlagPeriodo(Enum):
    ANTERIOR = "ANTERIOR"
    ATUAL = "ATUAL"


@dataclass(kw_only=True)
class OutrasInformacoesRelevantes:
    class Meta:
        name = "OUTRAS-INFORMACOES-RELEVANTES"

    outras_informacoes_relevantes: None | object = field(
        default=None,
        metadata={
            "name": "OUTRAS-INFORMACOES-RELEVANTES",
            "type": "Attribute",
        },
    )


class OutrosStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


@dataclass(kw_only=True)
class PalavrasChave:
    class Meta:
        name = "PALAVRAS-CHAVE"

    palavra_chave_1: None | object = field(
        default=None,
        metadata={
            "name": "PALAVRA-CHAVE-1",
            "type": "Attribute",
        },
    )
    palavra_chave_2: None | object = field(
        default=None,
        metadata={
            "name": "PALAVRA-CHAVE-2",
            "type": "Attribute",
        },
    )
    palavra_chave_3: None | object = field(
        default=None,
        metadata={
            "name": "PALAVRA-CHAVE-3",
            "type": "Attribute",
        },
    )
    palavra_chave_4: None | object = field(
        default=None,
        metadata={
            "name": "PALAVRA-CHAVE-4",
            "type": "Attribute",
        },
    )
    palavra_chave_5: None | object = field(
        default=None,
        metadata={
            "name": "PALAVRA-CHAVE-5",
            "type": "Attribute",
        },
    )
    palavra_chave_6: None | object = field(
        default=None,
        metadata={
            "name": "PALAVRA-CHAVE-6",
            "type": "Attribute",
        },
    )


class ParticipacaoEmProjetoFlagPeriodo(Enum):
    ANTERIOR = "ANTERIOR"
    ATUAL = "ATUAL"


@dataclass(kw_only=True)
class ParticipanteBanca:
    class Meta:
        name = "PARTICIPANTE-BANCA"

    nome_completo_do_participante_da_banca: None | object = field(
        default=None,
        metadata={
            "name": "NOME-COMPLETO-DO-PARTICIPANTE-DA-BANCA",
            "type": "Attribute",
        },
    )
    nome_para_citacao_do_participante_da_banca: None | object = field(
        default=None,
        metadata={
            "name": "NOME-PARA-CITACAO-DO-PARTICIPANTE-DA-BANCA",
            "type": "Attribute",
        },
    )
    ordem_participante: None | object = field(
        default=None,
        metadata={
            "name": "ORDEM-PARTICIPANTE",
            "type": "Attribute",
        },
    )
    cpf_do_participante_da_banca: None | object = field(
        default=None,
        metadata={
            "name": "CPF-DO-PARTICIPANTE-DA-BANCA",
            "type": "Attribute",
        },
    )
    nro_id_cnpq: None | object = field(
        default=None,
        metadata={
            "name": "NRO-ID-CNPQ",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipanteDeEventosCongressos:
    class Meta:
        name = "PARTICIPANTE-DE-EVENTOS-CONGRESSOS"

    nome_completo_do_participante_de_eventos_congressos: None | object = field(
        default=None,
        metadata={
            "name": "NOME-COMPLETO-DO-PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
            "type": "Attribute",
        },
    )
    nome_para_citacao_do_participante_de_eventos_congressos: None | object = (
        field(
            default=None,
            metadata={
                "name": "NOME-PARA-CITACAO-DO-PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
                "type": "Attribute",
            },
        )
    )
    ordem_participante: None | object = field(
        default=None,
        metadata={
            "name": "ORDEM-PARTICIPANTE",
            "type": "Attribute",
        },
    )
    cpf_do_participante_participante_de_eventos_congressos: None | object = (
        field(
            default=None,
            metadata={
                "name": "CPF-DO-PARTICIPANTE-PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
                "type": "Attribute",
            },
        )
    )
    nro_id_cnpq: None | object = field(
        default=None,
        metadata={
            "name": "NRO-ID-CNPQ",
            "type": "Attribute",
        },
    )


class PesquisaEDesenvolvimentoFlagPeriodo(Enum):
    ANTERIOR = "ANTERIOR"
    ATUAL = "ATUAL"


@dataclass(kw_only=True)
class PremioTitulo:
    class Meta:
        name = "PREMIO-TITULO"

    nome_do_premio_ou_titulo: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-PREMIO-OU-TITULO",
            "type": "Attribute",
        },
    )
    nome_da_entidade_promotora: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-ENTIDADE-PROMOTORA",
            "type": "Attribute",
        },
    )
    ano_da_premiacao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DA-PREMIACAO",
            "type": "Attribute",
        },
    )
    nome_do_premio_ou_titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-PREMIO-OU-TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ProducaoCtDoProjeto:
    class Meta:
        name = "PRODUCAO-CT-DO-PROJETO"

    sequencia_producao_ct: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO-CT",
            "type": "Attribute",
        },
    )
    titulo_da_producao_ct: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-PRODUCAO-CT",
            "type": "Attribute",
        },
    )
    tipo_producao_ct: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-PRODUCAO-CT",
            "type": "Attribute",
        },
    )
    titulo_da_producao_ct_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-PRODUCAO-CT-INGLES",
            "type": "Attribute",
        },
    )


class ProjetoDePesquisaFlagPotencialInovacao(Enum):
    SIM = "SIM"
    NAO = "NAO"


class ProjetoDePesquisaFormatoDataCertificacao(Enum):
    DDMMAAAA = "DDMMAAAA"


class ProjetoDePesquisaNatureza(Enum):
    DESENVOLVIMENTO = "DESENVOLVIMENTO"
    EXTENSAO = "EXTENSAO"
    PESQUISA = "PESQUISA"
    ENSINO = "ENSINO"
    OUTRA = "OUTRA"


class ProjetoDePesquisaSituacao(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    DESATIVADO = "DESATIVADO"
    CONCLUIDO = "CONCLUIDO"


class RegistroOuPatenteFormatoDataDepositoPct(Enum):
    DDMMAAAA = "DDMMAAAA"


class RegistroOuPatenteFormatoDataPedido(Enum):
    DDMMAAAA = "DDMMAAAA"


class RegistroOuPatenteTipoPatente(Enum):
    PRIVILEGIO_DE_INOVACAO_PI = "PRIVILEGIO_DE_INOVACAO_PI"
    MODELO_DE_UTILIDADE_MU = "MODELO_DE_UTILIDADE_MU"
    DESENHO_INDUSTRIAL_DI = "DESENHO_INDUSTRIAL_DI"
    MODELO_INDUSTRIAL_MI = "MODELO_INDUSTRIAL_MI"
    PATENTE_NO_EXTERIOR_PE = "PATENTE_NO_EXTERIOR_PE"
    PROGRAMA_DE_COMPUTADOR_PC = "PROGRAMA_DE_COMPUTADOR_PC"
    OUTRO_OU = "OUTRO_OU"
    OUTRO_OU_1 = "OUTRO_Ou"
    CERTIFICADO_DE_ADICAO_CA = "CERTIFICADO_DE_ADICAO_CA"
    CULTIVAR_PROTEGIDA_CTV = "CULTIVAR_PROTEGIDA_CTV"
    MARCA_REGISTRADA_DE_PRODUTO_MPD = "MARCA_REGISTRADA_DE_PRODUTO_MPD"
    MARCA_REGISTRADA_DE_SERVICO_MSV = "MARCA_REGISTRADA_DE_SERVICO_MSV"
    MARCA_REGISTRADA_COLETIVA_MCL = "MARCA_REGISTRADA_COLETIVA_MCL"
    MARCA_REGISTRADA_DE_CERTIFICACAO_MCT = (
        "MARCA_REGISTRADA_DE_CERTIFICACAO_MCT"
    )
    TOPOGRAFIA_DE_CIRCUITO_INTEGRADO_REGISTRADA_TCI = (
        "TOPOGRAFIA_DE_CIRCUITO_INTEGRADO_REGISTRADA_TCI"
    )
    MARCA_REGISTRADA_FIGURATIVA_MRF = "MARCA_REGISTRADA_FIGURATIVA_MRF"
    MARCA_REGISTRADA_NOMINATIVA_MRN = "MARCA_REGISTRADA_NOMINATIVA_MRN"
    MARCA_REGISTRADA_MISTA_MRM = "MARCA_REGISTRADA_MISTA_MRM"
    MARCA_REGISTRADA_TRIDIMENSIONAL_MRT = "MARCA_REGISTRADA_TRIDIMENSIONAL_MRT"


class ResidenciaMedicaStatusDoCurso(Enum):
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"
    INCOMPLETO = "INCOMPLETO"


@dataclass(kw_only=True)
class ResumoCv:
    class Meta:
        name = "RESUMO-CV"

    texto_resumo_cv_rh: None | object = field(
        default=None,
        metadata={
            "name": "TEXTO-RESUMO-CV-RH",
            "type": "Attribute",
        },
    )
    texto_resumo_cv_rh_en: None | object = field(
        default=None,
        metadata={
            "name": "TEXTO-RESUMO-CV-RH-EN",
            "type": "Attribute",
        },
    )


class ServicoTecnicoEspecializadoFlagPeriodo(Enum):
    ANTERIOR = "ANTERIOR"
    ATUAL = "ATUAL"


@dataclass(kw_only=True)
class SetoresDeAtividade:
    class Meta:
        name = "SETORES-DE-ATIVIDADE"

    setor_de_atividade_1: None | object = field(
        default=None,
        metadata={
            "name": "SETOR-DE-ATIVIDADE-1",
            "type": "Attribute",
        },
    )
    setor_de_atividade_2: None | object = field(
        default=None,
        metadata={
            "name": "SETOR-DE-ATIVIDADE-2",
            "type": "Attribute",
        },
    )
    setor_de_atividade_3: None | object = field(
        default=None,
        metadata={
            "name": "SETOR-DE-ATIVIDADE-3",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Treinamento:
    class Meta:
        name = "TREINAMENTO"

    sequencia_especificacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-ESPECIFICACAO",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


class TreinamentoMinistradoFlagPeriodo(Enum):
    ANTERIOR = "ANTERIOR"
    ATUAL = "ATUAL"


class VinculosEnquadramentoFuncional(Enum):
    PROFESSOR_TITULAR = "PROFESSOR_TITULAR"
    OUTRO = "OUTRO"
    LIVRE = "LIVRE"


class VinculosFlagDedicacaoExclusiva(Enum):
    SIM = "SIM"
    NAO = "NAO"


class VinculosFlagVinculoEmpregaticio(Enum):
    SIM = "SIM"
    NAO = "NAO"


class VinculosTipoDeVinculo(Enum):
    SERVIDOR_PUBLICO_OU_CELETISTA = "SERVIDOR_PUBLICO_OU_CELETISTA"
    SERVIDOR_PUBLICO = "SERVIDOR_PUBLICO"
    CELETISTA = "CELETISTA"
    PROFESSOR_VISITANTE = "PROFESSOR_VISITANTE"
    COLABORADOR = "COLABORADOR"
    BOLSISTA_RECEM_DOUTOR = "BOLSISTA_RECEM_DOUTOR"
    OUTRO = "OUTRO"
    LIVRE = "LIVRE"


@dataclass(kw_only=True)
class Aperfeicoamento:
    class Meta:
        name = "APERFEICOAMENTO"

    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    titulo_da_monografia: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-MONOGRAFIA",
            "type": "Attribute",
        },
    )
    nome_do_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTADOR",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    codigo_area_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AREA-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | AperfeicoamentoStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-AGENCIA",
            "type": "Attribute",
        },
    )
    carga_horaria: None | object = field(
        default=None,
        metadata={
            "name": "CARGA-HORARIA",
            "type": "Attribute",
        },
    )
    titulo_da_monografia_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-MONOGRAFIA-INGLES",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class AreaDeAtuacao:
    class Meta:
        name = "AREA-DE-ATUACAO"

    sequencia_area_de_atuacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-AREA-DE-ATUACAO",
            "type": "Attribute",
        },
    )
    nome_grande_area_do_conhecimento: (
        None | AreaDeAtuacaoNomeGrandeAreaDoConhecimento
    ) = field(
        default=None,
        metadata={
            "name": "NOME-GRANDE-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_area_do_conhecimento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_sub_area_do_conhecimento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-SUB-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_especialidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-ESPECIALIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class AreaDoConhecimento1:
    class Meta:
        name = "AREA-DO-CONHECIMENTO-1"

    nome_grande_area_do_conhecimento: (
        None | AreaDoConhecimento1NomeGrandeAreaDoConhecimento
    ) = field(
        default=None,
        metadata={
            "name": "NOME-GRANDE-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_area_do_conhecimento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_sub_area_do_conhecimento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-SUB-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_especialidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-ESPECIALIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class AreaDoConhecimento2:
    class Meta:
        name = "AREA-DO-CONHECIMENTO-2"

    nome_grande_area_do_conhecimento: (
        None | AreaDoConhecimento2NomeGrandeAreaDoConhecimento
    ) = field(
        default=None,
        metadata={
            "name": "NOME-GRANDE-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_area_do_conhecimento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_sub_area_do_conhecimento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-SUB-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_especialidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-ESPECIALIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class AreaDoConhecimento3:
    class Meta:
        name = "AREA-DO-CONHECIMENTO-3"

    nome_grande_area_do_conhecimento: (
        None | AreaDoConhecimento3NomeGrandeAreaDoConhecimento
    ) = field(
        default=None,
        metadata={
            "name": "NOME-GRANDE-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_area_do_conhecimento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_sub_area_do_conhecimento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-SUB-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_especialidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-ESPECIALIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ConselhoComissaoEConsultoria:
    class Meta:
        name = "CONSELHO-COMISSAO-E-CONSULTORIA"

    sequencia_funcao_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FUNCAO-ATIVIDADE",
            "type": "Attribute",
        },
    )
    flag_periodo: None | ConselhoComissaoEConsultoriaFlagPeriodo = field(
        default=None,
        metadata={
            "name": "FLAG-PERIODO",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_unidade: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-UNIDADE",
            "type": "Attribute",
        },
    )
    nome_unidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-UNIDADE",
            "type": "Attribute",
        },
    )
    especificacao: None | object = field(
        default=None,
        metadata={
            "name": "ESPECIFICACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CursoTecnicoProfissionalizante:
    class Meta:
        name = "CURSO-TECNICO-PROFISSIONALIZANTE"

    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | CursoTecnicoProfissionalizanteStatusDoCurso = (
        field(
            default=None,
            metadata={
                "name": "STATUS-DO-CURSO",
                "type": "Attribute",
            },
        )
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-AGENCIA",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaApresentacaoDeObraArtistica:
    class Meta:
        name = "DADOS-BASICOS-DA-APRESENTACAO-DE-OBRA-ARTISTICA"

    natureza: None | DadosBasicosDaApresentacaoDeObraArtisticaNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaApresentacaoDeObraArtisticaMeioDeDivulgacao = field(
        default=DadosBasicosDaApresentacaoDeObraArtisticaMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaApresentacaoDeObraArtisticaFlagRelevancia = field(
        default=DadosBasicosDaApresentacaoDeObraArtisticaFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaApresentacaoDeTrabalho:
    class Meta:
        name = "DADOS-BASICOS-DA-APRESENTACAO-DE-TRABALHO"

    natureza: None | DadosBasicosDaApresentacaoDeTrabalhoNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaApresentacaoDeTrabalhoFlagRelevancia = (
        field(
            default=DadosBasicosDaApresentacaoDeTrabalhoFlagRelevancia.NAO,
            metadata={
                "name": "FLAG-RELEVANCIA",
                "type": "Attribute",
            },
        )
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaApresentacaoDeTrabalhoFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaApresentacaoDeTrabalhoFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaApresentacaoEmRadioOuTv:
    class Meta:
        name = "DADOS-BASICOS-DA-APRESENTACAO-EM-RADIO-OU-TV"

    natureza: None | DadosBasicosDaApresentacaoEmRadioOuTvNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaApresentacaoEmRadioOuTvFlagRelevancia = (
        field(
            default=DadosBasicosDaApresentacaoEmRadioOuTvFlagRelevancia.NAO,
            metadata={
                "name": "FLAG-RELEVANCIA",
                "type": "Attribute",
            },
        )
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaApresentacaoEmRadioOuTvFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaApresentacaoEmRadioOuTvFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaComposicaoMusical:
    class Meta:
        name = "DADOS-BASICOS-DA-COMPOSICAO-MUSICAL"

    natureza: None | DadosBasicosDaComposicaoMusicalNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaComposicaoMusicalMeioDeDivulgacao = field(
        default=DadosBasicosDaComposicaoMusicalMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaComposicaoMusicalFlagRelevancia = field(
        default=DadosBasicosDaComposicaoMusicalFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaCultivar:
    class Meta:
        name = "DADOS-BASICOS-DA-CULTIVAR"

    denominacao: None | object = field(
        default=None,
        metadata={
            "name": "DENOMINACAO",
            "type": "Attribute",
        },
    )
    ano_solicitacao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-SOLICITACAO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaCultivarFlagRelevancia = field(
        default=DadosBasicosDaCultivarFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    denominacao_ingles: None | object = field(
        default=None,
        metadata={
            "name": "DENOMINACAO-INGLES",
            "type": "Attribute",
        },
    )
    flag_potencial_inovacao: DadosBasicosDaCultivarFlagPotencialInovacao = (
        field(
            default=DadosBasicosDaCultivarFlagPotencialInovacao.NAO,
            metadata={
                "name": "FLAG-POTENCIAL-INOVACAO",
                "type": "Attribute",
            },
        )
    )


@dataclass(kw_only=True)
class DadosBasicosDaMaquete:
    class Meta:
        name = "DADOS-BASICOS-DA-MAQUETE"

    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaMaqueteMeioDeDivulgacao = field(
        default=DadosBasicosDaMaqueteMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaMaqueteFlagRelevancia = field(
        default=DadosBasicosDaMaqueteFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaMarca:
    class Meta:
        name = "DADOS-BASICOS-DA-MARCA"

    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano_desenvolvimento: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DESENVOLVIMENTO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaMarcaFlagRelevancia = field(
        default=DadosBasicosDaMarcaFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_potencial_inovacao: DadosBasicosDaMarcaFlagPotencialInovacao = field(
        default=DadosBasicosDaMarcaFlagPotencialInovacao.NAO,
        metadata={
            "name": "FLAG-POTENCIAL-INOVACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaMidiaSocialWebsiteBlog:
    class Meta:
        name = "DADOS-BASICOS-DA-MIDIA-SOCIAL-WEBSITE-BLOG"

    natureza: None | DadosBasicosDaMidiaSocialWebsiteBlogNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    natureza_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA-INGLES",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaMidiaSocialWebsiteBlogFlagRelevancia = (
        field(
            default=DadosBasicosDaMidiaSocialWebsiteBlogFlagRelevancia.NAO,
            metadata={
                "name": "FLAG-RELEVANCIA",
                "type": "Attribute",
            },
        )
    )
    flag_divulgacao_cientifica: DadosBasicosDaMidiaSocialWebsiteBlogFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaMidiaSocialWebsiteBlogFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaMusica:
    class Meta:
        name = "DADOS-BASICOS-DA-MUSICA"

    natureza: None | DadosBasicosDaMusicaNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaMusicaMeioDeDivulgacao = field(
        default=DadosBasicosDaMusicaMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaMusicaFlagRelevancia = field(
        default=DadosBasicosDaMusicaFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaMusicaFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaMusicaFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaObraDeArtesVisuais:
    class Meta:
        name = "DADOS-BASICOS-DA-OBRA-DE-ARTES-VISUAIS"

    natureza: None | DadosBasicosDaObraDeArtesVisuaisNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaObraDeArtesVisuaisMeioDeDivulgacao = field(
        default=DadosBasicosDaObraDeArtesVisuaisMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaObraDeArtesVisuaisFlagRelevancia = field(
        default=DadosBasicosDaObraDeArtesVisuaisFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaOrganizacaoDeEvento:
    class Meta:
        name = "DADOS-BASICOS-DA-ORGANIZACAO-DE-EVENTO"

    tipo: None | DadosBasicosDaOrganizacaoDeEventoTipo = field(
        default=None,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    natureza: DadosBasicosDaOrganizacaoDeEventoNatureza = field(
        default=DadosBasicosDaOrganizacaoDeEventoNatureza.NAO_INFORMADO,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaOrganizacaoDeEventoMeioDeDivulgacao = field(
        default=DadosBasicosDaOrganizacaoDeEventoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaOrganizacaoDeEventoFlagRelevancia = field(
        default=DadosBasicosDaOrganizacaoDeEventoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaOrganizacaoDeEventoFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaOrganizacaoDeEventoFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaOrientacaoEmAndamentoDeMestrado:
    class Meta:
        name = "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-MESTRADO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    tipo: DadosBasicosDaOrientacaoEmAndamentoDeMestradoTipo = field(
        default=DadosBasicosDaOrientacaoEmAndamentoDeMestradoTipo.NAO_INFORMADO,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmBancaDeMestrado:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-BANCA-DE-MESTRADO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    tipo: None | DadosBasicosDaParticipacaoEmBancaDeMestradoTipo = field(
        default=None,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmCongresso:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-CONGRESSO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaParticipacaoEmCongressoMeioDeDivulgacao = field(
        default=DadosBasicosDaParticipacaoEmCongressoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaParticipacaoEmCongressoFlagRelevancia = (
        field(
            default=DadosBasicosDaParticipacaoEmCongressoFlagRelevancia.NAO,
            metadata={
                "name": "FLAG-RELEVANCIA",
                "type": "Attribute",
            },
        )
    )
    tipo_participacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    forma_participacao: None | object = field(
        default=None,
        metadata={
            "name": "FORMA-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaParticipacaoEmCongressoFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaParticipacaoEmCongressoFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmEncontro:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-ENCONTRO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaParticipacaoEmEncontroMeioDeDivulgacao = field(
        default=DadosBasicosDaParticipacaoEmEncontroMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaParticipacaoEmEncontroFlagRelevancia = (
        field(
            default=DadosBasicosDaParticipacaoEmEncontroFlagRelevancia.NAO,
            metadata={
                "name": "FLAG-RELEVANCIA",
                "type": "Attribute",
            },
        )
    )
    tipo_participacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    forma_participacao: None | object = field(
        default=None,
        metadata={
            "name": "FORMA-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaParticipacaoEmEncontroFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaParticipacaoEmEncontroFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmExposicao:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-EXPOSICAO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaParticipacaoEmExposicaoMeioDeDivulgacao = field(
        default=DadosBasicosDaParticipacaoEmExposicaoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaParticipacaoEmExposicaoFlagRelevancia = (
        field(
            default=DadosBasicosDaParticipacaoEmExposicaoFlagRelevancia.NAO,
            metadata={
                "name": "FLAG-RELEVANCIA",
                "type": "Attribute",
            },
        )
    )
    tipo_participacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    forma_participacao: None | object = field(
        default=None,
        metadata={
            "name": "FORMA-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaParticipacaoEmExposicaoFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaParticipacaoEmExposicaoFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmFeira:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-FEIRA"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaParticipacaoEmFeiraMeioDeDivulgacao = field(
        default=DadosBasicosDaParticipacaoEmFeiraMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaParticipacaoEmFeiraFlagRelevancia = field(
        default=DadosBasicosDaParticipacaoEmFeiraFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    tipo_participacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    forma_participacao: None | object = field(
        default=None,
        metadata={
            "name": "FORMA-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaParticipacaoEmFeiraFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaParticipacaoEmFeiraFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmOficina:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-OFICINA"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaParticipacaoEmOficinaMeioDeDivulgacao = field(
        default=DadosBasicosDaParticipacaoEmOficinaMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaParticipacaoEmOficinaFlagRelevancia = field(
        default=DadosBasicosDaParticipacaoEmOficinaFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    tipo_participacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    forma_participacao: None | object = field(
        default=None,
        metadata={
            "name": "FORMA-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaParticipacaoEmOficinaFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaParticipacaoEmOficinaFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmOlimpiada:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-OLIMPIADA"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaParticipacaoEmOlimpiadaMeioDeDivulgacao = field(
        default=DadosBasicosDaParticipacaoEmOlimpiadaMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaParticipacaoEmOlimpiadaFlagRelevancia = (
        field(
            default=DadosBasicosDaParticipacaoEmOlimpiadaFlagRelevancia.NAO,
            metadata={
                "name": "FLAG-RELEVANCIA",
                "type": "Attribute",
            },
        )
    )
    tipo_participacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    forma_participacao: None | object = field(
        default=None,
        metadata={
            "name": "FORMA-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaParticipacaoEmOlimpiadaFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaParticipacaoEmOlimpiadaFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmSeminario:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-SEMINARIO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaParticipacaoEmSeminarioMeioDeDivulgacao = field(
        default=DadosBasicosDaParticipacaoEmSeminarioMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaParticipacaoEmSeminarioFlagRelevancia = (
        field(
            default=DadosBasicosDaParticipacaoEmSeminarioFlagRelevancia.NAO,
            metadata={
                "name": "FLAG-RELEVANCIA",
                "type": "Attribute",
            },
        )
    )
    tipo_participacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    forma_participacao: None | object = field(
        default=None,
        metadata={
            "name": "FORMA-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaParticipacaoEmSeminarioFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaParticipacaoEmSeminarioFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaParticipacaoEmSimposio:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTICIPACAO-EM-SIMPOSIO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaParticipacaoEmSimposioMeioDeDivulgacao = field(
        default=DadosBasicosDaParticipacaoEmSimposioMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaParticipacaoEmSimposioFlagRelevancia = (
        field(
            default=DadosBasicosDaParticipacaoEmSimposioFlagRelevancia.NAO,
            metadata={
                "name": "FLAG-RELEVANCIA",
                "type": "Attribute",
            },
        )
    )
    tipo_participacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    forma_participacao: None | object = field(
        default=None,
        metadata={
            "name": "FORMA-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDaParticipacaoEmSimposioFlagDivulgacaoCientifica = field(
        default=DadosBasicosDaParticipacaoEmSimposioFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaPartitura:
    class Meta:
        name = "DADOS-BASICOS-DA-PARTITURA"

    natureza: None | DadosBasicosDaPartituraNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaPartituraMeioDeDivulgacao = field(
        default=DadosBasicosDaPartituraMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaPartituraFlagRelevancia = field(
        default=DadosBasicosDaPartituraFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaPatente:
    class Meta:
        name = "DADOS-BASICOS-DA-PATENTE"

    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano_desenvolvimento: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DESENVOLVIMENTO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaPatenteMeioDeDivulgacao = field(
        default=DadosBasicosDaPatenteMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaPatenteFlagRelevancia = field(
        default=DadosBasicosDaPatenteFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_potencial_inovacao: DadosBasicosDaPatenteFlagPotencialInovacao = (
        field(
            default=DadosBasicosDaPatenteFlagPotencialInovacao.NAO,
            metadata={
                "name": "FLAG-POTENCIAL-INOVACAO",
                "type": "Attribute",
            },
        )
    )


@dataclass(kw_only=True)
class DadosBasicosDaTopografiaDeCircuitoIntegrado:
    class Meta:
        name = "DADOS-BASICOS-DA-TOPOGRAFIA-DE-CIRCUITO-INTEGRADO"

    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano_desenvolvimento: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DESENVOLVIMENTO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaTopografiaDeCircuitoIntegradoFlagRelevancia = field(
        default=DadosBasicosDaTopografiaDeCircuitoIntegradoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_potencial_inovacao: DadosBasicosDaTopografiaDeCircuitoIntegradoFlagPotencialInovacao = field(
        default=DadosBasicosDaTopografiaDeCircuitoIntegradoFlagPotencialInovacao.NAO,
        metadata={
            "name": "FLAG-POTENCIAL-INOVACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDaTraducao:
    class Meta:
        name = "DADOS-BASICOS-DA-TRADUCAO"

    natureza: None | DadosBasicosDaTraducaoNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDaTraducaoMeioDeDivulgacao = field(
        default=DadosBasicosDaTraducaoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDaTraducaoFlagRelevancia = field(
        default=DadosBasicosDaTraducaoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeArtesCenicas:
    class Meta:
        name = "DADOS-BASICOS-DE-ARTES-CENICAS"

    natureza: None | DadosBasicosDeArtesCenicasNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeArtesCenicasFlagRelevancia = field(
        default=DadosBasicosDeArtesCenicasFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeArtesCenicasMeioDeDivulgacao = field(
        default=DadosBasicosDeArtesCenicasMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDeArtesCenicasFlagDivulgacaoCientifica = field(
        default=DadosBasicosDeArtesCenicasFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeArtesVisuais:
    class Meta:
        name = "DADOS-BASICOS-DE-ARTES-VISUAIS"

    natureza: None | DadosBasicosDeArtesVisuaisNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeArtesVisuaisFlagRelevancia = field(
        default=DadosBasicosDeArtesVisuaisFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeArtesVisuaisMeioDeDivulgacao = field(
        default=DadosBasicosDeArtesVisuaisMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDeArtesVisuaisFlagDivulgacaoCientifica = field(
        default=DadosBasicosDeArtesVisuaisFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeCartaMapaOuSimilar:
    class Meta:
        name = "DADOS-BASICOS-DE-CARTA-MAPA-OU-SIMILAR"

    natureza: None | DadosBasicosDeCartaMapaOuSimilarNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeCartaMapaOuSimilarMeioDeDivulgacao = field(
        default=DadosBasicosDeCartaMapaOuSimilarMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeCartaMapaOuSimilarFlagRelevancia = field(
        default=DadosBasicosDeCartaMapaOuSimilarFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeCursosCurtaDuracaoMinistrado:
    class Meta:
        name = "DADOS-BASICOS-DE-CURSOS-CURTA-DURACAO-MINISTRADO"

    nivel_do_curso: (
        None | DadosBasicosDeCursosCurtaDuracaoMinistradoNivelDoCurso
    ) = field(
        default=None,
        metadata={
            "name": "NIVEL-DO-CURSO",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeCursosCurtaDuracaoMinistradoMeioDeDivulgacao = field(
        default=DadosBasicosDeCursosCurtaDuracaoMinistradoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeCursosCurtaDuracaoMinistradoFlagRelevancia = field(
        default=DadosBasicosDeCursosCurtaDuracaoMinistradoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDeCursosCurtaDuracaoMinistradoFlagDivulgacaoCientifica = field(
        default=DadosBasicosDeCursosCurtaDuracaoMinistradoFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeDemaisTrabalhos:
    class Meta:
        name = "DADOS-BASICOS-DE-DEMAIS-TRABALHOS"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeDemaisTrabalhosMeioDeDivulgacao = field(
        default=DadosBasicosDeDemaisTrabalhosMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeDemaisTrabalhosFlagRelevancia = field(
        default=DadosBasicosDeDemaisTrabalhosFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    natureza_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeEditoracao:
    class Meta:
        name = "DADOS-BASICOS-DE-EDITORACAO"

    natureza: None | DadosBasicosDeEditoracaoNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeEditoracaoMeioDeDivulgacao = field(
        default=DadosBasicosDeEditoracaoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeEditoracaoFlagRelevancia = field(
        default=DadosBasicosDeEditoracaoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeManutencaoDeObraArtistica:
    class Meta:
        name = "DADOS-BASICOS-DE-MANUTENCAO-DE-OBRA-ARTISTICA"

    tipo: None | DadosBasicosDeManutencaoDeObraArtisticaTipo = field(
        default=None,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    natureza: DadosBasicosDeManutencaoDeObraArtisticaNatureza = field(
        default=DadosBasicosDeManutencaoDeObraArtisticaNatureza.NAO_INFORMADO,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeManutencaoDeObraArtisticaFlagRelevancia = (
        field(
            default=DadosBasicosDeManutencaoDeObraArtisticaFlagRelevancia.NAO,
            metadata={
                "name": "FLAG-RELEVANCIA",
                "type": "Attribute",
            },
        )
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeOrientacoesConcluidasParaDoutorado:
    class Meta:
        name = "DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeOrientacoesConcluidasParaDoutoradoFlagRelevancia = field(
        default=DadosBasicosDeOrientacoesConcluidasParaDoutoradoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeOrientacoesConcluidasParaMestrado:
    class Meta:
        name = "DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    tipo: None | DadosBasicosDeOrientacoesConcluidasParaMestradoTipo = field(
        default=None,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeOrientacoesConcluidasParaMestradoFlagRelevancia = field(
        default=DadosBasicosDeOrientacoesConcluidasParaMestradoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeOrientacoesConcluidasParaPosDoutorado:
    class Meta:
        name = "DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeOrientacoesConcluidasParaPosDoutoradoFlagRelevancia = field(
        default=DadosBasicosDeOrientacoesConcluidasParaPosDoutoradoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeOutraProducao:
    class Meta:
        name = "DADOS-BASICOS-DE-OUTRA-PRODUCAO"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeOutraProducaoMeioDeDivulgacao = field(
        default=DadosBasicosDeOutraProducaoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeOutraProducaoFlagRelevancia = field(
        default=DadosBasicosDeOutraProducaoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    natureza_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeOutraProducaoArtisticaCultural:
    class Meta:
        name = "DADOS-BASICOS-DE-OUTRA-PRODUCAO-ARTISTICA-CULTURAL"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeOutraProducaoArtisticaCulturalMeioDeDivulgacao = field(
        default=DadosBasicosDeOutraProducaoArtisticaCulturalMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeOutraProducaoArtisticaCulturalFlagRelevancia = field(
        default=DadosBasicosDeOutraProducaoArtisticaCulturalFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    natureza_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDeOutraProducaoArtisticaCulturalFlagDivulgacaoCientifica = field(
        default=DadosBasicosDeOutraProducaoArtisticaCulturalFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeOutraProducaoTecnica:
    class Meta:
        name = "DADOS-BASICOS-DE-OUTRA-PRODUCAO-TECNICA"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeOutraProducaoTecnicaMeioDeDivulgacao = field(
        default=DadosBasicosDeOutraProducaoTecnicaMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeOutraProducaoTecnicaFlagRelevancia = field(
        default=DadosBasicosDeOutraProducaoTecnicaFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    natureza_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDeOutraProducaoTecnicaFlagDivulgacaoCientifica = field(
        default=DadosBasicosDeOutraProducaoTecnicaFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeOutrasOrientacoesConcluidas:
    class Meta:
        name = "DADOS-BASICOS-DE-OUTRAS-ORIENTACOES-CONCLUIDAS"

    natureza: None | DadosBasicosDeOutrasOrientacoesConcluidasNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    tipo: None | object = field(
        default=None,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeOutrasOrientacoesConcluidasFlagRelevancia = field(
        default=DadosBasicosDeOutrasOrientacoesConcluidasFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    tipo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeOutrasParticipacoesEmEventosCongressos:
    class Meta:
        name = "DADOS-BASICOS-DE-OUTRAS-PARTICIPACOES-EM-EVENTOS-CONGRESSOS"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeOutrasParticipacoesEmEventosCongressosMeioDeDivulgacao = field(
        default=DadosBasicosDeOutrasParticipacoesEmEventosCongressosMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeOutrasParticipacoesEmEventosCongressosFlagRelevancia = field(
        default=DadosBasicosDeOutrasParticipacoesEmEventosCongressosFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    tipo_participacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    forma_participacao: None | object = field(
        default=None,
        metadata={
            "name": "FORMA-PARTICIPACAO",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDeOutrasParticipacoesEmEventosCongressosFlagDivulgacaoCientifica = field(
        default=DadosBasicosDeOutrasParticipacoesEmEventosCongressosFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDeSonoplastia:
    class Meta:
        name = "DADOS-BASICOS-DE-SONOPLASTIA"

    natureza: None | DadosBasicosDeSonoplastiaNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDeSonoplastiaMeioDeDivulgacao = field(
        default=DadosBasicosDeSonoplastiaMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDeSonoplastiaFlagRelevancia = field(
        default=DadosBasicosDeSonoplastiaFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoArranjoMusical:
    class Meta:
        name = "DADOS-BASICOS-DO-ARRANJO-MUSICAL"

    natureza: None | DadosBasicosDoArranjoMusicalNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoArranjoMusicalMeioDeDivulgacao = field(
        default=DadosBasicosDoArranjoMusicalMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoArranjoMusicalFlagRelevancia = field(
        default=DadosBasicosDoArranjoMusicalFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoArtigo:
    class Meta:
        name = "DADOS-BASICOS-DO-ARTIGO"

    natureza: None | DadosBasicosDoArtigoNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_artigo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-ARTIGO",
            "type": "Attribute",
        },
    )
    ano_do_artigo: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DO-ARTIGO",
            "type": "Attribute",
        },
    )
    pais_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoArtigoMeioDeDivulgacao = field(
        default=DadosBasicosDoArtigoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoArtigoFlagRelevancia = field(
        default=DadosBasicosDoArtigoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_artigo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-ARTIGO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDoArtigoFlagDivulgacaoCientifica = field(
        default=DadosBasicosDoArtigoFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoCapitulo:
    class Meta:
        name = "DADOS-BASICOS-DO-CAPITULO"

    tipo: None | object = field(
        default=None,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    titulo_do_capitulo_do_livro: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-CAPITULO-DO-LIVRO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoCapituloMeioDeDivulgacao = field(
        default=DadosBasicosDoCapituloMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoCapituloFlagRelevancia = field(
        default=DadosBasicosDoCapituloFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_capitulo_do_livro_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-CAPITULO-DO-LIVRO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDoCapituloFlagDivulgacaoCientifica = field(
        default=DadosBasicosDoCapituloFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoCursoDeCurtaDuracao:
    class Meta:
        name = "DADOS-BASICOS-DO-CURSO-DE-CURTA-DURACAO"

    natureza: None | DadosBasicosDoCursoDeCurtaDuracaoNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoCursoDeCurtaDuracaoMeioDeDivulgacao = field(
        default=DadosBasicosDoCursoDeCurtaDuracaoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoCursoDeCurtaDuracaoFlagRelevancia = field(
        default=DadosBasicosDoCursoDeCurtaDuracaoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoDesenhoIndustrial:
    class Meta:
        name = "DADOS-BASICOS-DO-DESENHO-INDUSTRIAL"

    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano_desenvolvimento: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DESENVOLVIMENTO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoDesenhoIndustrialFlagRelevancia = field(
        default=DadosBasicosDoDesenhoIndustrialFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    flag_potencial_inovacao: DadosBasicosDoDesenhoIndustrialFlagPotencialInovacao = field(
        default=DadosBasicosDoDesenhoIndustrialFlagPotencialInovacao.NAO,
        metadata={
            "name": "FLAG-POTENCIAL-INOVACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoLivro:
    class Meta:
        name = "DADOS-BASICOS-DO-LIVRO"

    tipo: None | DadosBasicosDoLivroTipo = field(
        default=None,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    natureza: DadosBasicosDoLivroNatureza = field(
        default=DadosBasicosDoLivroNatureza.NAO_INFORMADO,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_livro: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-LIVRO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoLivroMeioDeDivulgacao = field(
        default=DadosBasicosDoLivroMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoLivroFlagRelevancia = field(
        default=DadosBasicosDoLivroFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_livro_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-LIVRO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDoLivroFlagDivulgacaoCientifica = (
        field(
            default=DadosBasicosDoLivroFlagDivulgacaoCientifica.NAO,
            metadata={
                "name": "FLAG-DIVULGACAO-CIENTIFICA",
                "type": "Attribute",
            },
        )
    )


@dataclass(kw_only=True)
class DadosBasicosDoMaterialDidaticoOuInstrucional:
    class Meta:
        name = "DADOS-BASICOS-DO-MATERIAL-DIDATICO-OU-INSTRUCIONAL"

    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoMaterialDidaticoOuInstrucionalMeioDeDivulgacao = field(
        default=DadosBasicosDoMaterialDidaticoOuInstrucionalMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoMaterialDidaticoOuInstrucionalFlagRelevancia = field(
        default=DadosBasicosDoMaterialDidaticoOuInstrucionalFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    natureza_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDoMaterialDidaticoOuInstrucionalFlagDivulgacaoCientifica = field(
        default=DadosBasicosDoMaterialDidaticoOuInstrucionalFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoPrefacioPosfacio:
    class Meta:
        name = "DADOS-BASICOS-DO-PREFACIO-POSFACIO"

    tipo: None | DadosBasicosDoPrefacioPosfacioTipo = field(
        default=None,
        metadata={
            "name": "TIPO",
            "type": "Attribute",
        },
    )
    natureza: DadosBasicosDoPrefacioPosfacioNatureza = field(
        default=DadosBasicosDoPrefacioPosfacioNatureza.NAO_INFORMADO,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoPrefacioPosfacioMeioDeDivulgacao = field(
        default=DadosBasicosDoPrefacioPosfacioMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoPrefacioPosfacioFlagRelevancia = field(
        default=DadosBasicosDoPrefacioPosfacioFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoProcessosOuTecnicas:
    class Meta:
        name = "DADOS-BASICOS-DO-PROCESSOS-OU-TECNICAS"

    natureza: None | DadosBasicosDoProcessosOuTecnicasNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_processo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-PROCESSO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoProcessosOuTecnicasMeioDeDivulgacao = field(
        default=DadosBasicosDoProcessosOuTecnicasMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoProcessosOuTecnicasFlagRelevancia = field(
        default=DadosBasicosDoProcessosOuTecnicasFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_processo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-PROCESSO-INGLES",
            "type": "Attribute",
        },
    )
    flag_potencial_inovacao: DadosBasicosDoProcessosOuTecnicasFlagPotencialInovacao = field(
        default=DadosBasicosDoProcessosOuTecnicasFlagPotencialInovacao.NAO,
        metadata={
            "name": "FLAG-POTENCIAL-INOVACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoProdutoTecnologico:
    class Meta:
        name = "DADOS-BASICOS-DO-PRODUTO-TECNOLOGICO"

    tipo_produto: None | DadosBasicosDoProdutoTecnologicoTipoProduto = field(
        default=None,
        metadata={
            "name": "TIPO-PRODUTO",
            "type": "Attribute",
        },
    )
    natureza: DadosBasicosDoProdutoTecnologicoNatureza = field(
        default=DadosBasicosDoProdutoTecnologicoNatureza.NAO_INFORMADO,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_produto: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-PRODUTO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoProdutoTecnologicoMeioDeDivulgacao = field(
        default=DadosBasicosDoProdutoTecnologicoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoProdutoTecnologicoFlagRelevancia = field(
        default=DadosBasicosDoProdutoTecnologicoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_produto_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-PRODUTO-INGLES",
            "type": "Attribute",
        },
    )
    flag_potencial_inovacao: DadosBasicosDoProdutoTecnologicoFlagPotencialInovacao = field(
        default=DadosBasicosDoProdutoTecnologicoFlagPotencialInovacao.NAO,
        metadata={
            "name": "FLAG-POTENCIAL-INOVACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoProgramaDeRadioOuTv:
    class Meta:
        name = "DADOS-BASICOS-DO-PROGRAMA-DE-RADIO-OU-TV"

    natureza: None | DadosBasicosDoProgramaDeRadioOuTvNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoProgramaDeRadioOuTvFlagRelevancia = field(
        default=DadosBasicosDoProgramaDeRadioOuTvFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )
    home_page: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoProgramaDeRadioOuTvMeioDeDivulgacao = field(
        default=DadosBasicosDoProgramaDeRadioOuTvMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDoProgramaDeRadioOuTvFlagDivulgacaoCientifica = field(
        default=DadosBasicosDoProgramaDeRadioOuTvFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoRelatorioDePesquisa:
    class Meta:
        name = "DADOS-BASICOS-DO-RELATORIO-DE-PESQUISA"

    titulo: None | object = field(
        default=None,
        metadata={
            "name": "TITULO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoRelatorioDePesquisaMeioDeDivulgacao = field(
        default=DadosBasicosDoRelatorioDePesquisaMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoRelatorioDePesquisaFlagRelevancia = field(
        default=DadosBasicosDoRelatorioDePesquisaFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoSoftware:
    class Meta:
        name = "DADOS-BASICOS-DO-SOFTWARE"

    natureza: None | DadosBasicosDoSoftwareNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_software: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-SOFTWARE",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoSoftwareMeioDeDivulgacao = field(
        default=DadosBasicosDoSoftwareMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoSoftwareFlagRelevancia = field(
        default=DadosBasicosDoSoftwareFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_software_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-SOFTWARE-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDoSoftwareFlagDivulgacaoCientifica = field(
        default=DadosBasicosDoSoftwareFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )
    flag_potencial_inovacao: DadosBasicosDoSoftwareFlagPotencialInovacao = (
        field(
            default=DadosBasicosDoSoftwareFlagPotencialInovacao.NAO,
            metadata={
                "name": "FLAG-POTENCIAL-INOVACAO",
                "type": "Attribute",
            },
        )
    )


@dataclass(kw_only=True)
class DadosBasicosDoTexto:
    class Meta:
        name = "DADOS-BASICOS-DO-TEXTO"

    natureza: None | DadosBasicosDoTextoNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_texto: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TEXTO",
            "type": "Attribute",
        },
    )
    ano_do_texto: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DO-TEXTO",
            "type": "Attribute",
        },
    )
    pais_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoTextoMeioDeDivulgacao = field(
        default=DadosBasicosDoTextoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoTextoFlagRelevancia = field(
        default=DadosBasicosDoTextoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_texto_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TEXTO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDoTextoFlagDivulgacaoCientifica = (
        field(
            default=DadosBasicosDoTextoFlagDivulgacaoCientifica.NAO,
            metadata={
                "name": "FLAG-DIVULGACAO-CIENTIFICA",
                "type": "Attribute",
            },
        )
    )


@dataclass(kw_only=True)
class DadosBasicosDoTrabalho:
    class Meta:
        name = "DADOS-BASICOS-DO-TRABALHO"

    natureza: None | DadosBasicosDoTrabalhoNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    ano_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    pais_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DO-EVENTO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoTrabalhoMeioDeDivulgacao = field(
        default=DadosBasicosDoTrabalhoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoTrabalhoFlagRelevancia = field(
        default=DadosBasicosDoTrabalhoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-INGLES",
            "type": "Attribute",
        },
    )
    flag_divulgacao_cientifica: DadosBasicosDoTrabalhoFlagDivulgacaoCientifica = field(
        default=DadosBasicosDoTrabalhoFlagDivulgacaoCientifica.NAO,
        metadata={
            "name": "FLAG-DIVULGACAO-CIENTIFICA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DadosBasicosDoTrabalhoTecnico:
    class Meta:
        name = "DADOS-BASICOS-DO-TRABALHO-TECNICO"

    natureza: None | DadosBasicosDoTrabalhoTecnicoNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_tecnico: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-TECNICO",
            "type": "Attribute",
        },
    )
    ano: None | object = field(
        default=None,
        metadata={
            "name": "ANO",
            "type": "Attribute",
        },
    )
    pais: None | object = field(
        default=None,
        metadata={
            "name": "PAIS",
            "type": "Attribute",
        },
    )
    meio_de_divulgacao: DadosBasicosDoTrabalhoTecnicoMeioDeDivulgacao = field(
        default=DadosBasicosDoTrabalhoTecnicoMeioDeDivulgacao.NAO_INFORMADO,
        metadata={
            "name": "MEIO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )
    home_page_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "HOME-PAGE-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    flag_relevancia: DadosBasicosDoTrabalhoTecnicoFlagRelevancia = field(
        default=DadosBasicosDoTrabalhoTecnicoFlagRelevancia.NAO,
        metadata={
            "name": "FLAG-RELEVANCIA",
            "type": "Attribute",
        },
    )
    doi: None | object = field(
        default=None,
        metadata={
            "name": "DOI",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_tecnico_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-TECNICO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaApresentacaoDeObraArtistica:
    class Meta:
        name = "DETALHAMENTO-DA-APRESENTACAO-DE-OBRA-ARTISTICA"

    tipo_de_evento: (
        None | DetalhamentoDaApresentacaoDeObraArtisticaTipoDeEvento
    ) = field(
        default=None,
        metadata={
            "name": "TIPO-DE-EVENTO",
            "type": "Attribute",
        },
    )
    atividade_dos_autores: (
        None | DetalhamentoDaApresentacaoDeObraArtisticaAtividadeDosAutores
    ) = field(
        default=None,
        metadata={
            "name": "ATIVIDADE-DOS-AUTORES",
            "type": "Attribute",
        },
    )
    flag_ineditismo_da_obra: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-INEDITISMO-DA-OBRA",
            "type": "Attribute",
        },
    )
    premiacao: None | object = field(
        default=None,
        metadata={
            "name": "PREMIACAO",
            "type": "Attribute",
        },
    )
    obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    autor_da_obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "AUTOR-DA-OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    ano_da_obra_de_referencia: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DA-OBRA-DE-REFERENCIA",
            "type": "Attribute",
        },
    )
    duracao_em_minutos: None | object = field(
        default=None,
        metadata={
            "name": "DURACAO-EM-MINUTOS",
            "type": "Attribute",
        },
    )
    instituicao_promotora_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA-DO-EVENTO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaApresentacaoEmRadioOuTv:
    class Meta:
        name = "DETALHAMENTO-DA-APRESENTACAO-EM-RADIO-OU-TV"

    emissora: None | object = field(
        default=None,
        metadata={
            "name": "EMISSORA",
            "type": "Attribute",
        },
    )
    formato_data_de_apresentacao: DetalhamentoDaApresentacaoEmRadioOuTvFormatoDataDeApresentacao = field(
        default=DetalhamentoDaApresentacaoEmRadioOuTvFormatoDataDeApresentacao.DDMMAAAA,
        metadata={
            "name": "FORMATO-DATA-DE-APRESENTACAO",
            "type": "Attribute",
        },
    )
    data_de_apresentacao: None | object = field(
        default=None,
        metadata={
            "name": "DATA-DE-APRESENTACAO",
            "type": "Attribute",
        },
    )
    duracao_em_minutos: None | object = field(
        default=None,
        metadata={
            "name": "DURACAO-EM-MINUTOS",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaObraDeArtesVisuais:
    class Meta:
        name = "DETALHAMENTO-DA-OBRA-DE-ARTES-VISUAIS"

    material_empregado: None | object = field(
        default=None,
        metadata={
            "name": "MATERIAL-EMPREGADO",
            "type": "Attribute",
        },
    )
    tipo_de_evento: None | DetalhamentoDaObraDeArtesVisuaisTipoDeEvento = (
        field(
            default=None,
            metadata={
                "name": "TIPO-DE-EVENTO",
                "type": "Attribute",
            },
        )
    )
    evento: None | object = field(
        default=None,
        metadata={
            "name": "EVENTO",
            "type": "Attribute",
        },
    )
    premiacao: None | object = field(
        default=None,
        metadata={
            "name": "PREMIACAO",
            "type": "Attribute",
        },
    )
    acervo: DetalhamentoDaObraDeArtesVisuaisAcervo = field(
        default=DetalhamentoDaObraDeArtesVisuaisAcervo.NAO_INFORMADO,
        metadata={
            "name": "ACERVO",
            "type": "Attribute",
        },
    )
    instituicao_promotora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaOrientacaoEmAndamentoDeDoutorado:
    class Meta:
        name = "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-DOUTORADO"

    tipo_de_orientacao: (
        None | DetalhamentoDaOrientacaoEmAndamentoDeDoutoradoTipoDeOrientacao
    ) = field(
        default=None,
        metadata={
            "name": "TIPO-DE-ORIENTACAO",
            "type": "Attribute",
        },
    )
    nome_do_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTANDO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_id_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTANDO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaOrientacaoEmAndamentoDeMestrado:
    class Meta:
        name = "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-MESTRADO"

    tipo_de_orientacao: (
        None | DetalhamentoDaOrientacaoEmAndamentoDeMestradoTipoDeOrientacao
    ) = field(
        default=None,
        metadata={
            "name": "TIPO-DE-ORIENTACAO",
            "type": "Attribute",
        },
    )
    nome_do_orientando: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTANDO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_id_orientado: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTADO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeCursosCurtaDuracaoMinistrado:
    class Meta:
        name = "DETALHAMENTO-DE-CURSOS-CURTA-DURACAO-MINISTRADO"

    participacao_dos_autores: (
        None | DetalhamentoDeCursosCurtaDuracaoMinistradoParticipacaoDosAutores
    ) = field(
        default=None,
        metadata={
            "name": "PARTICIPACAO-DOS-AUTORES",
            "type": "Attribute",
        },
    )
    instituicao_promotora_do_curso: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA-DO-CURSO",
            "type": "Attribute",
        },
    )
    local_do_curso: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-CURSO",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )
    duracao: None | object = field(
        default=None,
        metadata={
            "name": "DURACAO",
            "type": "Attribute",
        },
    )
    unidade: None | object = field(
        default=None,
        metadata={
            "name": "UNIDADE",
            "type": "Attribute",
        },
    )
    unidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "UNIDADE-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeManutencaoDeObraArtistica:
    class Meta:
        name = "DETALHAMENTO-DE-MANUTENCAO-DE-OBRA-ARTISTICA"

    nome_da_obra: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-OBRA",
            "type": "Attribute",
        },
    )
    autor_da_obra: None | object = field(
        default=None,
        metadata={
            "name": "AUTOR-DA-OBRA",
            "type": "Attribute",
        },
    )
    ano_da_obra: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DA-OBRA",
            "type": "Attribute",
        },
    )
    acervo: DetalhamentoDeManutencaoDeObraArtisticaAcervo = field(
        default=DetalhamentoDeManutencaoDeObraArtisticaAcervo.NAO_INFORMADO,
        metadata={
            "name": "ACERVO",
            "type": "Attribute",
        },
    )
    local: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeOrientacoesConcluidasParaDoutorado:
    class Meta:
        name = "DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO"

    tipo_de_orientacao: (
        None | DetalhamentoDeOrientacoesConcluidasParaDoutoradoTipoDeOrientacao
    ) = field(
        default=None,
        metadata={
            "name": "TIPO-DE-ORIENTACAO",
            "type": "Attribute",
        },
    )
    nome_do_orientado: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTADO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_da_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_do_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    numero_id_orientado: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTADO",
            "type": "Attribute",
        },
    )
    nome_do_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDeOrientacoesConcluidasParaMestrado:
    class Meta:
        name = "DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO"

    tipo_de_orientacao: (
        None | DetalhamentoDeOrientacoesConcluidasParaMestradoTipoDeOrientacao
    ) = field(
        default=None,
        metadata={
            "name": "TIPO-DE-ORIENTACAO",
            "type": "Attribute",
        },
    )
    nome_do_orientado: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTADO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_da_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_do_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CURSO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_da_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_de_paginas: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DE-PAGINAS",
            "type": "Attribute",
        },
    )
    numero_id_orientado: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTADO",
            "type": "Attribute",
        },
    )
    nome_do_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoCursoDeCurtaDuracao:
    class Meta:
        name = "DETALHAMENTO-DO-CURSO-DE-CURTA-DURACAO"

    duracao: None | object = field(
        default=None,
        metadata={
            "name": "DURACAO",
            "type": "Attribute",
        },
    )
    unidade: DetalhamentoDoCursoDeCurtaDuracaoUnidade = field(
        default=DetalhamentoDoCursoDeCurtaDuracaoUnidade.NAO_INFORMADO,
        metadata={
            "name": "UNIDADE",
            "type": "Attribute",
        },
    )
    instituicao_promotora_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-PROMOTORA-DO-EVENTO",
            "type": "Attribute",
        },
    )
    local_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoProgramaDeRadioOuTv:
    class Meta:
        name = "DETALHAMENTO-DO-PROGRAMA-DE-RADIO-OU-TV"

    emissora: None | object = field(
        default=None,
        metadata={
            "name": "EMISSORA",
            "type": "Attribute",
        },
    )
    tema: None | object = field(
        default=None,
        metadata={
            "name": "TEMA",
            "type": "Attribute",
        },
    )
    formato_data_da_apresentacao: DetalhamentoDoProgramaDeRadioOuTvFormatoDataDaApresentacao = field(
        default=DetalhamentoDoProgramaDeRadioOuTvFormatoDataDaApresentacao.DDMMAAAA,
        metadata={
            "name": "FORMATO-DATA-DA-APRESENTACAO",
            "type": "Attribute",
        },
    )
    data_da_apresentacao: None | object = field(
        default=None,
        metadata={
            "name": "DATA-DA-APRESENTACAO",
            "type": "Attribute",
        },
    )
    duracao_em_minutos: None | object = field(
        default=None,
        metadata={
            "name": "DURACAO-EM-MINUTOS",
            "type": "Attribute",
        },
    )
    cidade: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE",
            "type": "Attribute",
        },
    )
    veiculo_de_divulgacao: None | object = field(
        default=None,
        metadata={
            "name": "VEICULO-DE-DIVULGACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoTexto:
    class Meta:
        name = "DETALHAMENTO-DO-TEXTO"

    titulo_do_jornal_ou_revista: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-JORNAL-OU-REVISTA",
            "type": "Attribute",
        },
    )
    issn: None | object = field(
        default=None,
        metadata={
            "name": "ISSN",
            "type": "Attribute",
        },
    )
    formato_data_de_publicacao: DetalhamentoDoTextoFormatoDataDePublicacao = (
        field(
            default=DetalhamentoDoTextoFormatoDataDePublicacao.DDMMAAAA,
            metadata={
                "name": "FORMATO-DATA-DE-PUBLICACAO",
                "type": "Attribute",
            },
        )
    )
    data_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "DATA-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )
    volume: None | object = field(
        default=None,
        metadata={
            "name": "VOLUME",
            "type": "Attribute",
        },
    )
    pagina_inicial: None | object = field(
        default=None,
        metadata={
            "name": "PAGINA-INICIAL",
            "type": "Attribute",
        },
    )
    pagina_final: None | object = field(
        default=None,
        metadata={
            "name": "PAGINA-FINAL",
            "type": "Attribute",
        },
    )
    local_de_publicacao: None | object = field(
        default=None,
        metadata={
            "name": "LOCAL-DE-PUBLICACAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoTrabalho:
    class Meta:
        name = "DETALHAMENTO-DO-TRABALHO"

    classificacao_do_evento: DetalhamentoDoTrabalhoClassificacaoDoEvento = (
        field(
            default=DetalhamentoDoTrabalhoClassificacaoDoEvento.NAO_INFORMADO,
            metadata={
                "name": "CLASSIFICACAO-DO-EVENTO",
                "type": "Attribute",
            },
        )
    )
    nome_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO",
            "type": "Attribute",
        },
    )
    cidade_do_evento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-EVENTO",
            "type": "Attribute",
        },
    )
    ano_de_realizacao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-REALIZACAO",
            "type": "Attribute",
        },
    )
    titulo_dos_anais_ou_proceedings: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DOS-ANAIS-OU-PROCEEDINGS",
            "type": "Attribute",
        },
    )
    volume: None | object = field(
        default=None,
        metadata={
            "name": "VOLUME",
            "type": "Attribute",
        },
    )
    fasciculo: None | object = field(
        default=None,
        metadata={
            "name": "FASCICULO",
            "type": "Attribute",
        },
    )
    serie: None | object = field(
        default=None,
        metadata={
            "name": "SERIE",
            "type": "Attribute",
        },
    )
    pagina_inicial: None | object = field(
        default=None,
        metadata={
            "name": "PAGINA-INICIAL",
            "type": "Attribute",
        },
    )
    pagina_final: None | object = field(
        default=None,
        metadata={
            "name": "PAGINA-FINAL",
            "type": "Attribute",
        },
    )
    isbn: None | object = field(
        default=None,
        metadata={
            "name": "ISBN",
            "type": "Attribute",
        },
    )
    nome_da_editora: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-EDITORA",
            "type": "Attribute",
        },
    )
    cidade_da_editora: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DA-EDITORA",
            "type": "Attribute",
        },
    )
    nome_do_evento_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-EVENTO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DirecaoEAdministracao:
    class Meta:
        name = "DIRECAO-E-ADMINISTRACAO"

    sequencia_funcao_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FUNCAO-ATIVIDADE",
            "type": "Attribute",
        },
    )
    flag_periodo: None | DirecaoEAdministracaoFlagPeriodo = field(
        default=None,
        metadata={
            "name": "FLAG-PERIODO",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_unidade: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-UNIDADE",
            "type": "Attribute",
        },
    )
    formato_cargo_ou_funcao: (
        None | DirecaoEAdministracaoFormatoCargoOuFuncao
    ) = field(
        default=None,
        metadata={
            "name": "FORMATO-CARGO-OU-FUNCAO",
            "type": "Attribute",
        },
    )
    cargo_ou_funcao: None | object = field(
        default=None,
        metadata={
            "name": "CARGO-OU-FUNCAO",
            "type": "Attribute",
        },
    )
    nome_unidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-UNIDADE",
            "type": "Attribute",
        },
    )
    cargo_ou_funcao_ingles: None | object = field(
        default=None,
        metadata={
            "name": "CARGO-OU-FUNCAO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Endereco:
    class Meta:
        name = "ENDERECO"

    endereco_profissional: None | EnderecoProfissional = field(
        default=None,
        metadata={
            "name": "ENDERECO-PROFISSIONAL",
            "type": "Element",
        },
    )
    endereco_residencial: None | EnderecoResidencial = field(
        default=None,
        metadata={
            "name": "ENDERECO-RESIDENCIAL",
            "type": "Element",
        },
    )
    flag_de_preferencia: None | EnderecoFlagDePreferencia = field(
        default=None,
        metadata={
            "name": "FLAG-DE-PREFERENCIA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Ensino:
    class Meta:
        name = "ENSINO"

    disciplina: list[Disciplina] = field(
        default_factory=list,
        metadata={
            "name": "DISCIPLINA",
            "type": "Element",
        },
    )
    sequencia_funcao_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FUNCAO-ATIVIDADE",
            "type": "Attribute",
        },
    )
    flag_periodo: None | EnsinoFlagPeriodo = field(
        default=None,
        metadata={
            "name": "FLAG-PERIODO",
            "type": "Attribute",
        },
    )
    tipo_ensino: None | EnsinoTipoEnsino = field(
        default=None,
        metadata={
            "name": "TIPO-ENSINO",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EnsinoFundamentalPrimeiroGrau:
    class Meta:
        name = "ENSINO-FUNDAMENTAL-PRIMEIRO-GRAU"

    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | EnsinoFundamentalPrimeiroGrauStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EnsinoMedioSegundoGrau:
    class Meta:
        name = "ENSINO-MEDIO-SEGUNDO-GRAU"

    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | EnsinoMedioSegundoGrauStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Especializacao:
    class Meta:
        name = "ESPECIALIZACAO"

    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    titulo_da_monografia: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-MONOGRAFIA",
            "type": "Attribute",
        },
    )
    nome_do_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTADOR",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | EspecializacaoStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-AGENCIA",
            "type": "Attribute",
        },
    )
    carga_horaria: None | object = field(
        default=None,
        metadata={
            "name": "CARGA-HORARIA",
            "type": "Attribute",
        },
    )
    titulo_da_monografia_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-MONOGRAFIA-INGLES",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Estagio:
    class Meta:
        name = "ESTAGIO"

    sequencia_funcao_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FUNCAO-ATIVIDADE",
            "type": "Attribute",
        },
    )
    flag_periodo: None | EstagioFlagPeriodo = field(
        default=None,
        metadata={
            "name": "FLAG-PERIODO",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_unidade: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-UNIDADE",
            "type": "Attribute",
        },
    )
    nome_unidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-UNIDADE",
            "type": "Attribute",
        },
    )
    estagio_realizado: None | object = field(
        default=None,
        metadata={
            "name": "ESTAGIO-REALIZADO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ExtensaoUniversitaria:
    class Meta:
        name = "EXTENSAO-UNIVERSITARIA"

    sequencia_funcao_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FUNCAO-ATIVIDADE",
            "type": "Attribute",
        },
    )
    flag_periodo: None | ExtensaoUniversitariaFlagPeriodo = field(
        default=None,
        metadata={
            "name": "FLAG-PERIODO",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_unidade: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-UNIDADE",
            "type": "Attribute",
        },
    )
    nome_unidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-UNIDADE",
            "type": "Attribute",
        },
    )
    atividade_de_extensao_realizada: None | object = field(
        default=None,
        metadata={
            "name": "ATIVIDADE-DE-EXTENSAO-REALIZADA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class FinanciadorDoProjeto:
    class Meta:
        name = "FINANCIADOR-DO-PROJETO"

    sequencia_financiador: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FINANCIADOR",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    natureza: None | FinanciadorDoProjetoNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class FormacaoComplementarCursoDeCurtaDuracao:
    class Meta:
        name = "FORMACAO-COMPLEMENTAR-CURSO-DE-CURTA-DURACAO"

    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    carga_horaria: None | object = field(
        default=None,
        metadata={
            "name": "CARGA-HORARIA",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: (
        None | FormacaoComplementarCursoDeCurtaDuracaoStatusDoCurso
    ) = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class FormacaoComplementarDeExtensaoUniversitaria:
    class Meta:
        name = "FORMACAO-COMPLEMENTAR-DE-EXTENSAO-UNIVERSITARIA"

    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    carga_horaria: None | object = field(
        default=None,
        metadata={
            "name": "CARGA-HORARIA",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: (
        None | FormacaoComplementarDeExtensaoUniversitariaStatusDoCurso
    ) = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Graduacao:
    class Meta:
        name = "GRADUACAO"

    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_de_conclusao_de_curso: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-DE-CONCLUSAO-DE-CURSO",
            "type": "Attribute",
        },
    )
    nome_do_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTADOR",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    codigo_area_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AREA-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | GraduacaoStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-AGENCIA",
            "type": "Attribute",
        },
    )
    numero_id_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTADOR",
            "type": "Attribute",
        },
    )
    codigo_curso_capes: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO-CAPES",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_de_conclusao_de_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-DE-CONCLUSAO-DE-CURSO-INGLES",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )
    formacao_academica_titulacao: None | object = field(
        default=None,
        metadata={
            "name": "FORMACAO-ACADEMICA-TITULACAO",
            "type": "Attribute",
        },
    )
    tipo_graduacao: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-GRADUACAO",
            "type": "Attribute",
        },
    )
    codigo_instituicao_grad: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-GRAD",
            "type": "Attribute",
        },
    )
    nome_instituicao_grad: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO-GRAD",
            "type": "Attribute",
        },
    )
    codigo_instituicao_outra_grad: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-OUTRA-GRAD",
            "type": "Attribute",
        },
    )
    nome_instituicao_outra_grad: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO-OUTRA-GRAD",
            "type": "Attribute",
        },
    )
    nome_orientador_grad: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORIENTADOR-GRAD",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class HistoricoSituacoesPatente:
    class Meta:
        name = "HISTORICO-SITUACOES-PATENTE"

    descricao_situacao_patente: None | object = field(
        default=None,
        metadata={
            "name": "DESCRICAO-SITUACAO-PATENTE",
            "type": "Attribute",
        },
    )
    formato_data_situacao_patente: HistoricoSituacoesPatenteFormatoDataSituacaoPatente = field(
        default=HistoricoSituacoesPatenteFormatoDataSituacaoPatente.DDMMAAAA,
        metadata={
            "name": "FORMATO-DATA-SITUACAO-PATENTE",
            "type": "Attribute",
        },
    )
    data_situacao_patente: None | object = field(
        default=None,
        metadata={
            "name": "DATA-SITUACAO-PATENTE",
            "type": "Attribute",
        },
    )
    status_situacao_patente: HistoricoSituacoesPatenteStatusSituacaoPatente = (
        field(
            metadata={
                "name": "STATUS-SITUACAO-PATENTE",
                "type": "Attribute",
            }
        )
    )


@dataclass(kw_only=True)
class Idioma:
    class Meta:
        name = "IDIOMA"

    idioma: None | object = field(
        default=None,
        metadata={
            "name": "IDIOMA",
            "type": "Attribute",
        },
    )
    descricao_do_idioma: None | object = field(
        default=None,
        metadata={
            "name": "DESCRICAO-DO-IDIOMA",
            "type": "Attribute",
        },
    )
    proficiencia_de_leitura: None | IdiomaProficienciaDeLeitura = field(
        default=None,
        metadata={
            "name": "PROFICIENCIA-DE-LEITURA",
            "type": "Attribute",
        },
    )
    proficiencia_de_fala: None | IdiomaProficienciaDeFala = field(
        default=None,
        metadata={
            "name": "PROFICIENCIA-DE-FALA",
            "type": "Attribute",
        },
    )
    proficiencia_de_escrita: None | IdiomaProficienciaDeEscrita = field(
        default=None,
        metadata={
            "name": "PROFICIENCIA-DE-ESCRITA",
            "type": "Attribute",
        },
    )
    proficiencia_de_compreensao: None | IdiomaProficienciaDeCompreensao = (
        field(
            default=None,
            metadata={
                "name": "PROFICIENCIA-DE-COMPREENSAO",
                "type": "Attribute",
            },
        )
    )


@dataclass(kw_only=True)
class InformacaoAdicionalCurso:
    class Meta:
        name = "INFORMACAO-ADICIONAL-CURSO"

    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_grande_area_do_conhecimento: InformacaoAdicionalCursoNomeGrandeAreaDoConhecimento = field(
        default=InformacaoAdicionalCursoNomeGrandeAreaDoConhecimento.NAO_INFORMADO,
        metadata={
            "name": "NOME-GRANDE-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_area_do_conhecimento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_sub_area_do_conhecimento: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-SUB-AREA-DO-CONHECIMENTO",
            "type": "Attribute",
        },
    )
    nome_da_especialidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-ESPECIALIDADE",
            "type": "Attribute",
        },
    )
    nivel_curso: None | InformacaoAdicionalCursoNivelCurso = field(
        default=None,
        metadata={
            "name": "NIVEL-CURSO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class InformacaoAdicionalInstituicao:
    class Meta:
        name = "INFORMACAO-ADICIONAL-INSTITUICAO"

    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    sigla_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "SIGLA-INSTITUICAO",
            "type": "Attribute",
        },
    )
    sigla_uf_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "SIGLA-UF-INSTITUICAO",
            "type": "Attribute",
        },
    )
    sigla_pais_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "SIGLA-PAIS-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_pais_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-PAIS-INSTITUICAO",
            "type": "Attribute",
        },
    )
    flag_agencia_fomento: (
        None | InformacaoAdicionalInstituicaoFlagAgenciaFomento
    ) = field(
        default=None,
        metadata={
            "name": "FLAG-AGENCIA-FOMENTO",
            "type": "Attribute",
        },
    )
    flag_instituicao_de_ensino: (
        None | InformacaoAdicionalInstituicaoFlagInstituicaoDeEnsino
    ) = field(
        default=None,
        metadata={
            "name": "FLAG-INSTITUICAO-DE-ENSINO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class IntegrantesDoProjeto:
    class Meta:
        name = "INTEGRANTES-DO-PROJETO"

    nome_completo: None | object = field(
        default=None,
        metadata={
            "name": "NOME-COMPLETO",
            "type": "Attribute",
        },
    )
    nome_para_citacao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-PARA-CITACAO",
            "type": "Attribute",
        },
    )
    ordem_de_integracao: None | object = field(
        default=None,
        metadata={
            "name": "ORDEM-DE-INTEGRACAO",
            "type": "Attribute",
        },
    )
    flag_responsavel: None | IntegrantesDoProjetoFlagResponsavel = field(
        default=None,
        metadata={
            "name": "FLAG-RESPONSAVEL",
            "type": "Attribute",
        },
    )
    nro_id_cnpq: None | object = field(
        default=None,
        metadata={
            "name": "NRO-ID-CNPQ",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Licenca:
    class Meta:
        name = "LICENCA"

    tipo_licenca: None | LicencaTipoLicenca = field(
        default=None,
        metadata={
            "name": "TIPO-LICENCA",
            "type": "Attribute",
        },
    )
    formato_data_inicio_licenca: LicencaFormatoDataInicioLicenca = field(
        default=LicencaFormatoDataInicioLicenca.DDMMAAAA,
        metadata={
            "name": "FORMATO-DATA-INICIO-LICENCA",
            "type": "Attribute",
        },
    )
    data_inicio_licenca: None | object = field(
        default=None,
        metadata={
            "name": "DATA-INICIO-LICENCA",
            "type": "Attribute",
        },
    )
    formato_data_fim_licenca: LicencaFormatoDataFimLicenca = field(
        default=LicencaFormatoDataFimLicenca.DDMMAAAA,
        metadata={
            "name": "FORMATO-DATA-FIM-LICENCA",
            "type": "Attribute",
        },
    )
    data_fim_licenca: None | object = field(
        default=None,
        metadata={
            "name": "DATA-FIM-LICENCA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Orientacoes:
    class Meta:
        name = "ORIENTACOES"

    orientacao: list[Orientacao] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACAO",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OutraAtividadeTecnicoCientifica:
    class Meta:
        name = "OUTRA-ATIVIDADE-TECNICO-CIENTIFICA"

    sequencia_funcao_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FUNCAO-ATIVIDADE",
            "type": "Attribute",
        },
    )
    flag_periodo: None | OutraAtividadeTecnicoCientificaFlagPeriodo = field(
        default=None,
        metadata={
            "name": "FLAG-PERIODO",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_unidade: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-UNIDADE",
            "type": "Attribute",
        },
    )
    atividade_realizada: None | object = field(
        default=None,
        metadata={
            "name": "ATIVIDADE-REALIZADA",
            "type": "Attribute",
        },
    )
    nome_unidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-UNIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Outros:
    class Meta:
        name = "OUTROS"

    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    carga_horaria: None | object = field(
        default=None,
        metadata={
            "name": "CARGA-HORARIA",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | OutrosStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PremiosTitulos:
    class Meta:
        name = "PREMIOS-TITULOS"

    premio_titulo: list[PremioTitulo] = field(
        default_factory=list,
        metadata={
            "name": "PREMIO-TITULO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ProducoesCtDoProjeto:
    class Meta:
        name = "PRODUCOES-CT-DO-PROJETO"

    producao_ct_do_projeto: list[ProducaoCtDoProjeto] = field(
        default_factory=list,
        metadata={
            "name": "PRODUCAO-CT-DO-PROJETO",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class RegistroOuPatente:
    class Meta:
        name = "REGISTRO-OU-PATENTE"

    tipo_patente: None | RegistroOuPatenteTipoPatente = field(
        default=None,
        metadata={
            "name": "TIPO-PATENTE",
            "type": "Attribute",
        },
    )
    codigo_do_registro_ou_patente: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-DO-REGISTRO-OU-PATENTE",
            "type": "Attribute",
        },
    )
    titulo_patente: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-PATENTE",
            "type": "Attribute",
        },
    )
    formato_data_pedido: RegistroOuPatenteFormatoDataPedido = field(
        default=RegistroOuPatenteFormatoDataPedido.DDMMAAAA,
        metadata={
            "name": "FORMATO-DATA-PEDIDO",
            "type": "Attribute",
        },
    )
    data_pedido_de_deposito: None | object = field(
        default=None,
        metadata={
            "name": "DATA-PEDIDO-DE-DEPOSITO",
            "type": "Attribute",
        },
    )
    data_de_pedido_de_exame: None | object = field(
        default=None,
        metadata={
            "name": "DATA-DE-PEDIDO-DE-EXAME",
            "type": "Attribute",
        },
    )
    data_de_concessao: None | object = field(
        default=None,
        metadata={
            "name": "DATA-DE-CONCESSAO",
            "type": "Attribute",
        },
    )
    instituicao_deposito_registro: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-DEPOSITO-REGISTRO",
            "type": "Attribute",
        },
    )
    numero_deposito_pct: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DEPOSITO-PCT",
            "type": "Attribute",
        },
    )
    formato_data_deposito_pct: RegistroOuPatenteFormatoDataDepositoPct = field(
        default=RegistroOuPatenteFormatoDataDepositoPct.DDMMAAAA,
        metadata={
            "name": "FORMATO-DATA-DEPOSITO-PCT",
            "type": "Attribute",
        },
    )
    data_deposito_pct: None | object = field(
        default=None,
        metadata={
            "name": "DATA-DEPOSITO-PCT",
            "type": "Attribute",
        },
    )
    nome_do_titular: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-TITULAR",
            "type": "Attribute",
        },
    )
    nome_do_depositante: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-DEPOSITANTE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ServicoTecnicoEspecializado:
    class Meta:
        name = "SERVICO-TECNICO-ESPECIALIZADO"

    sequencia_funcao_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FUNCAO-ATIVIDADE",
            "type": "Attribute",
        },
    )
    flag_periodo: None | ServicoTecnicoEspecializadoFlagPeriodo = field(
        default=None,
        metadata={
            "name": "FLAG-PERIODO",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_unidade: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-UNIDADE",
            "type": "Attribute",
        },
    )
    nome_unidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-UNIDADE",
            "type": "Attribute",
        },
    )
    servico_realizado: None | object = field(
        default=None,
        metadata={
            "name": "SERVICO-REALIZADO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TreinamentoMinistrado:
    class Meta:
        name = "TREINAMENTO-MINISTRADO"

    treinamento: list[Treinamento] = field(
        default_factory=list,
        metadata={
            "name": "TREINAMENTO",
            "type": "Element",
        },
    )
    sequencia_funcao_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FUNCAO-ATIVIDADE",
            "type": "Attribute",
        },
    )
    flag_periodo: None | TreinamentoMinistradoFlagPeriodo = field(
        default=None,
        metadata={
            "name": "FLAG-PERIODO",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_unidade: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-UNIDADE",
            "type": "Attribute",
        },
    )
    nome_unidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-UNIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Vinculos:
    class Meta:
        name = "VINCULOS"

    sequencia_historico: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-HISTORICO",
            "type": "Attribute",
        },
    )
    tipo_de_vinculo: None | VinculosTipoDeVinculo = field(
        default=None,
        metadata={
            "name": "TIPO-DE-VINCULO",
            "type": "Attribute",
        },
    )
    enquadramento_funcional: None | VinculosEnquadramentoFuncional = field(
        default=None,
        metadata={
            "name": "ENQUADRAMENTO-FUNCIONAL",
            "type": "Attribute",
        },
    )
    carga_horaria_semanal: None | object = field(
        default=None,
        metadata={
            "name": "CARGA-HORARIA-SEMANAL",
            "type": "Attribute",
        },
    )
    flag_dedicacao_exclusiva: None | VinculosFlagDedicacaoExclusiva = field(
        default=None,
        metadata={
            "name": "FLAG-DEDICACAO-EXCLUSIVA",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    outras_informacoes: None | object = field(
        default=None,
        metadata={
            "name": "OUTRAS-INFORMACOES",
            "type": "Attribute",
        },
    )
    flag_vinculo_empregaticio: None | VinculosFlagVinculoEmpregaticio = field(
        default=None,
        metadata={
            "name": "FLAG-VINCULO-EMPREGATICIO",
            "type": "Attribute",
        },
    )
    outro_vinculo_informado: None | object = field(
        default=None,
        metadata={
            "name": "OUTRO-VINCULO-INFORMADO",
            "type": "Attribute",
        },
    )
    outro_enquadramento_funcional_informado: None | object = field(
        default=None,
        metadata={
            "name": "OUTRO-ENQUADRAMENTO-FUNCIONAL-INFORMADO",
            "type": "Attribute",
        },
    )
    outro_enquadramento_funcional_informado_ingles: None | object = field(
        default=None,
        metadata={
            "name": "OUTRO-ENQUADRAMENTO-FUNCIONAL-INFORMADO-INGLES",
            "type": "Attribute",
        },
    )
    outras_informacoes_ingles: None | object = field(
        default=None,
        metadata={
            "name": "OUTRAS-INFORMACOES-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class AreasDeAtuacao:
    class Meta:
        name = "AREAS-DE-ATUACAO"

    area_de_atuacao: list[AreaDeAtuacao] = field(
        default_factory=list,
        metadata={
            "name": "AREA-DE-ATUACAO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AreasDoConhecimento:
    class Meta:
        name = "AREAS-DO-CONHECIMENTO"

    area_do_conhecimento_1: None | AreaDoConhecimento1 = field(
        default=None,
        metadata={
            "name": "AREA-DO-CONHECIMENTO-1",
            "type": "Element",
        },
    )
    area_do_conhecimento_2: None | AreaDoConhecimento2 = field(
        default=None,
        metadata={
            "name": "AREA-DO-CONHECIMENTO-2",
            "type": "Element",
        },
    )
    area_do_conhecimento_3: None | AreaDoConhecimento3 = field(
        default=None,
        metadata={
            "name": "AREA-DO-CONHECIMENTO-3",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AtividadesDeConselhoComissaoEConsultoria:
    class Meta:
        name = "ATIVIDADES-DE-CONSELHO-COMISSAO-E-CONSULTORIA"

    conselho_comissao_e_consultoria: list[ConselhoComissaoEConsultoria] = (
        field(
            default_factory=list,
            metadata={
                "name": "CONSELHO-COMISSAO-E-CONSULTORIA",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class AtividadesDeDirecaoEAdministracao:
    class Meta:
        name = "ATIVIDADES-DE-DIRECAO-E-ADMINISTRACAO"

    direcao_e_administracao: list[DirecaoEAdministracao] = field(
        default_factory=list,
        metadata={
            "name": "DIRECAO-E-ADMINISTRACAO",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AtividadesDeEnsino:
    class Meta:
        name = "ATIVIDADES-DE-ENSINO"

    ensino: list[Ensino] = field(
        default_factory=list,
        metadata={
            "name": "ENSINO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AtividadesDeEstagio:
    class Meta:
        name = "ATIVIDADES-DE-ESTAGIO"

    estagio: list[Estagio] = field(
        default_factory=list,
        metadata={
            "name": "ESTAGIO",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AtividadesDeExtensaoUniversitaria:
    class Meta:
        name = "ATIVIDADES-DE-EXTENSAO-UNIVERSITARIA"

    extensao_universitaria: list[ExtensaoUniversitaria] = field(
        default_factory=list,
        metadata={
            "name": "EXTENSAO-UNIVERSITARIA",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AtividadesDeServicoTecnicoEspecializado:
    class Meta:
        name = "ATIVIDADES-DE-SERVICO-TECNICO-ESPECIALIZADO"

    servico_tecnico_especializado: list[ServicoTecnicoEspecializado] = field(
        default_factory=list,
        metadata={
            "name": "SERVICO-TECNICO-ESPECIALIZADO",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AtividadesDeTreinamentoMinistrado:
    class Meta:
        name = "ATIVIDADES-DE-TREINAMENTO-MINISTRADO"

    treinamento_ministrado: list[TreinamentoMinistrado] = field(
        default_factory=list,
        metadata={
            "name": "TREINAMENTO-MINISTRADO",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaCultivar:
    class Meta:
        name = "DETALHAMENTO-DA-CULTIVAR"

    registro_ou_patente: list[RegistroOuPatente] = field(
        default_factory=list,
        metadata={
            "name": "REGISTRO-OU-PATENTE",
            "type": "Element",
        },
    )
    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaMarca:
    class Meta:
        name = "DETALHAMENTO-DA-MARCA"

    registro_ou_patente: list[RegistroOuPatente] = field(
        default_factory=list,
        metadata={
            "name": "REGISTRO-OU-PATENTE",
            "type": "Element",
        },
    )
    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )
    natureza: None | object = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaPatente:
    class Meta:
        name = "DETALHAMENTO-DA-PATENTE"

    registro_ou_patente: list[RegistroOuPatente] = field(
        default_factory=list,
        metadata={
            "name": "REGISTRO-OU-PATENTE",
            "type": "Element",
        },
    )
    historico_situacoes_patente: list[HistoricoSituacoesPatente] = field(
        default_factory=list,
        metadata={
            "name": "HISTORICO-SITUACOES-PATENTE",
            "type": "Element",
        },
    )
    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )
    categoria: None | object = field(
        default=None,
        metadata={
            "name": "CATEGORIA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDaTopografiaDeCircuitoIntegrado:
    class Meta:
        name = "DETALHAMENTO-DA-TOPOGRAFIA-DE-CIRCUITO-INTEGRADO"

    registro_ou_patente: list[RegistroOuPatente] = field(
        default_factory=list,
        metadata={
            "name": "REGISTRO-OU-PATENTE",
            "type": "Element",
        },
    )
    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoDesenhoIndustrial:
    class Meta:
        name = "DETALHAMENTO-DO-DESENHO-INDUSTRIAL"

    registro_ou_patente: list[RegistroOuPatente] = field(
        default_factory=list,
        metadata={
            "name": "REGISTRO-OU-PATENTE",
            "type": "Element",
        },
    )
    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoProcessosOuTecnicas:
    class Meta:
        name = "DETALHAMENTO-DO-PROCESSOS-OU-TECNICAS"

    registro_ou_patente: list[RegistroOuPatente] = field(
        default_factory=list,
        metadata={
            "name": "REGISTRO-OU-PATENTE",
            "type": "Element",
        },
    )
    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    disponibilidade: None | object = field(
        default=None,
        metadata={
            "name": "DISPONIBILIDADE",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )
    cidade_do_processo: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-PROCESSO",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoProdutoTecnologico:
    class Meta:
        name = "DETALHAMENTO-DO-PRODUTO-TECNOLOGICO"

    registro_ou_patente: list[RegistroOuPatente] = field(
        default_factory=list,
        metadata={
            "name": "REGISTRO-OU-PATENTE",
            "type": "Element",
        },
    )
    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    disponibilidade: None | object = field(
        default=None,
        metadata={
            "name": "DISPONIBILIDADE",
            "type": "Attribute",
        },
    )
    cidade_do_produto: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-DO-PRODUTO",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DetalhamentoDoSoftware:
    class Meta:
        name = "DETALHAMENTO-DO-SOFTWARE"

    registro_ou_patente: list[RegistroOuPatente] = field(
        default_factory=list,
        metadata={
            "name": "REGISTRO-OU-PATENTE",
            "type": "Element",
        },
    )
    finalidade: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE",
            "type": "Attribute",
        },
    )
    plataforma: None | object = field(
        default=None,
        metadata={
            "name": "PLATAFORMA",
            "type": "Attribute",
        },
    )
    ambiente: None | object = field(
        default=None,
        metadata={
            "name": "AMBIENTE",
            "type": "Attribute",
        },
    )
    disponibilidade: DetalhamentoDoSoftwareDisponibilidade = field(
        default=DetalhamentoDoSoftwareDisponibilidade.NAO_INFORMADO,
        metadata={
            "name": "DISPONIBILIDADE",
            "type": "Attribute",
        },
    )
    instituicao_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "INSTITUICAO-FINANCIADORA",
            "type": "Attribute",
        },
    )
    finalidade_ingles: None | object = field(
        default=None,
        metadata={
            "name": "FINALIDADE-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EquipeDoProjeto:
    class Meta:
        name = "EQUIPE-DO-PROJETO"

    integrantes_do_projeto: list[IntegrantesDoProjeto] = field(
        default_factory=list,
        metadata={
            "name": "INTEGRANTES-DO-PROJETO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FinanciadoresDoProjeto:
    class Meta:
        name = "FINANCIADORES-DO-PROJETO"

    financiador_do_projeto: list[FinanciadorDoProjeto] = field(
        default_factory=list,
        metadata={
            "name": "FINANCIADOR-DO-PROJETO",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Idiomas:
    class Meta:
        name = "IDIOMAS"

    idioma: list[Idioma] = field(
        default_factory=list,
        metadata={
            "name": "IDIOMA",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class InformacoesAdicionaisCursos:
    class Meta:
        name = "INFORMACOES-ADICIONAIS-CURSOS"

    informacao_adicional_curso: list[InformacaoAdicionalCurso] = field(
        default_factory=list,
        metadata={
            "name": "INFORMACAO-ADICIONAL-CURSO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class InformacoesAdicionaisInstituicoes:
    class Meta:
        name = "INFORMACOES-ADICIONAIS-INSTITUICOES"

    informacao_adicional_instituicao: list[InformacaoAdicionalInstituicao] = (
        field(
            default_factory=list,
            metadata={
                "name": "INFORMACAO-ADICIONAL-INSTITUICAO",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class Licencas:
    class Meta:
        name = "LICENCAS"

    licenca: list[Licenca] = field(
        default_factory=list,
        metadata={
            "name": "LICENCA",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OutrasAtividadesTecnicoCientifica:
    class Meta:
        name = "OUTRAS-ATIVIDADES-TECNICO-CIENTIFICA"

    outra_atividade_tecnico_cientifica: list[
        OutraAtividadeTecnicoCientifica
    ] = field(
        default_factory=list,
        metadata={
            "name": "OUTRA-ATIVIDADE-TECNICO-CIENTIFICA",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ApresentacaoDeObraArtistica:
    class Meta:
        name = "APRESENTACAO-DE-OBRA-ARTISTICA"

    dados_basicos_da_apresentacao_de_obra_artistica: (
        None | DadosBasicosDaApresentacaoDeObraArtistica
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-APRESENTACAO-DE-OBRA-ARTISTICA",
            "type": "Element",
        },
    )
    detalhamento_da_apresentacao_de_obra_artistica: (
        None | DetalhamentoDaApresentacaoDeObraArtistica
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-APRESENTACAO-DE-OBRA-ARTISTICA",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ApresentacaoDeTrabalho:
    class Meta:
        name = "APRESENTACAO-DE-TRABALHO"

    dados_basicos_da_apresentacao_de_trabalho: (
        None | DadosBasicosDaApresentacaoDeTrabalho
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-APRESENTACAO-DE-TRABALHO",
            "type": "Element",
        },
    )
    detalhamento_da_apresentacao_de_trabalho: (
        None | DetalhamentoDaApresentacaoDeTrabalho
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-APRESENTACAO-DE-TRABALHO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ApresentacaoEmRadioOuTv:
    class Meta:
        name = "APRESENTACAO-EM-RADIO-OU-TV"

    dados_basicos_da_apresentacao_em_radio_ou_tv: (
        None | DadosBasicosDaApresentacaoEmRadioOuTv
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-APRESENTACAO-EM-RADIO-OU-TV",
            "type": "Element",
        },
    )
    detalhamento_da_apresentacao_em_radio_ou_tv: (
        None | DetalhamentoDaApresentacaoEmRadioOuTv
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-APRESENTACAO-EM-RADIO-OU-TV",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ArranjoMusical:
    class Meta:
        name = "ARRANJO-MUSICAL"

    dados_basicos_do_arranjo_musical: None | DadosBasicosDoArranjoMusical = (
        field(
            default=None,
            metadata={
                "name": "DADOS-BASICOS-DO-ARRANJO-MUSICAL",
                "type": "Element",
            },
        )
    )
    detalhamento_do_arranjo_musical: None | DetalhamentoDoArranjoMusical = (
        field(
            default=None,
            metadata={
                "name": "DETALHAMENTO-DO-ARRANJO-MUSICAL",
                "type": "Element",
            },
        )
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ArtesCenicas:
    class Meta:
        name = "ARTES-CENICAS"

    dados_basicos_de_artes_cenicas: None | DadosBasicosDeArtesCenicas = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-ARTES-CENICAS",
            "type": "Element",
        },
    )
    detalhamento_de_artes_cenicas: None | DetalhamentoDeArtesCenicas = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-ARTES-CENICAS",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ArtesVisuais:
    class Meta:
        name = "ARTES-VISUAIS"

    dados_basicos_de_artes_visuais: None | DadosBasicosDeArtesVisuais = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-ARTES-VISUAIS",
            "type": "Element",
        },
    )
    detalhamento_de_artes_visuais: None | DetalhamentoDeArtesVisuais = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-ARTES-VISUAIS",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ArtigoAceitoParaPublicacao:
    class Meta:
        name = "ARTIGO-ACEITO-PARA-PUBLICACAO"

    dados_basicos_do_artigo: None | DadosBasicosDoArtigo = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-ARTIGO",
            "type": "Element",
        },
    )
    detalhamento_do_artigo: None | DetalhamentoDoArtigo = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-ARTIGO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ArtigoPublicado:
    class Meta:
        name = "ARTIGO-PUBLICADO"

    dados_basicos_do_artigo: None | DadosBasicosDoArtigo = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-ARTIGO",
            "type": "Element",
        },
    )
    detalhamento_do_artigo: None | DetalhamentoDoArtigo = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-ARTIGO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )
    ordem_importancia: None | object = field(
        default=None,
        metadata={
            "name": "ORDEM-IMPORTANCIA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class BancaJulgadoraParaAvaliacaoCursos:
    class Meta:
        name = "BANCA-JULGADORA-PARA-AVALIACAO-CURSOS"

    dados_basicos_da_banca_julgadora_para_avaliacao_cursos: (
        None | DadosBasicosDaBancaJulgadoraParaAvaliacaoCursos
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-BANCA-JULGADORA-PARA-AVALIACAO-CURSOS",
            "type": "Element",
        },
    )
    detalhamento_da_banca_julgadora_para_avaliacao_cursos: (
        None | DetalhamentoDaBancaJulgadoraParaAvaliacaoCursos
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-BANCA-JULGADORA-PARA-AVALIACAO-CURSOS",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class BancaJulgadoraParaConcursoPublico:
    class Meta:
        name = "BANCA-JULGADORA-PARA-CONCURSO-PUBLICO"

    dados_basicos_da_banca_julgadora_para_concurso_publico: (
        None | DadosBasicosDaBancaJulgadoraParaConcursoPublico
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-BANCA-JULGADORA-PARA-CONCURSO-PUBLICO",
            "type": "Element",
        },
    )
    detalhamento_da_banca_julgadora_para_concurso_publico: (
        None | DetalhamentoDaBancaJulgadoraParaConcursoPublico
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-BANCA-JULGADORA-PARA-CONCURSO-PUBLICO",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class BancaJulgadoraParaLivreDocencia:
    class Meta:
        name = "BANCA-JULGADORA-PARA-LIVRE-DOCENCIA"

    dados_basicos_da_banca_julgadora_para_livre_docencia: (
        None | DadosBasicosDaBancaJulgadoraParaLivreDocencia
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-BANCA-JULGADORA-PARA-LIVRE-DOCENCIA",
            "type": "Element",
        },
    )
    detalhamento_da_banca_julgadora_para_livre_docencia: (
        None | DetalhamentoDaBancaJulgadoraParaLivreDocencia
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-BANCA-JULGADORA-PARA-LIVRE-DOCENCIA",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class BancaJulgadoraParaProfessorTitular:
    class Meta:
        name = "BANCA-JULGADORA-PARA-PROFESSOR-TITULAR"

    dados_basicos_da_banca_julgadora_para_professor_titular: (
        None | DadosBasicosDaBancaJulgadoraParaProfessorTitular
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-BANCA-JULGADORA-PARA-PROFESSOR-TITULAR",
            "type": "Element",
        },
    )
    detalhamento_da_banca_julgadora_para_professor_titular: (
        None | DetalhamentoDaBancaJulgadoraParaProfessorTitular
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-BANCA-JULGADORA-PARA-PROFESSOR-TITULAR",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CapituloDeLivroPublicado:
    class Meta:
        name = "CAPITULO-DE-LIVRO-PUBLICADO"

    dados_basicos_do_capitulo: DadosBasicosDoCapitulo = field(
        metadata={
            "name": "DADOS-BASICOS-DO-CAPITULO",
            "type": "Element",
        }
    )
    detalhamento_do_capitulo: DetalhamentoDoCapitulo = field(
        metadata={
            "name": "DETALHAMENTO-DO-CAPITULO",
            "type": "Element",
        }
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CartaMapaOuSimilar:
    class Meta:
        name = "CARTA-MAPA-OU-SIMILAR"

    dados_basicos_de_carta_mapa_ou_similar: (
        None | DadosBasicosDeCartaMapaOuSimilar
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-CARTA-MAPA-OU-SIMILAR",
            "type": "Element",
        },
    )
    detalhamento_de_carta_mapa_ou_similar: (
        None | DetalhamentoDeCartaMapaOuSimilar
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-CARTA-MAPA-OU-SIMILAR",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ComposicaoMusical:
    class Meta:
        name = "COMPOSICAO-MUSICAL"

    dados_basicos_da_composicao_musical: (
        None | DadosBasicosDaComposicaoMusical
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-COMPOSICAO-MUSICAL",
            "type": "Element",
        },
    )
    detalhamento_da_composicao_musical: (
        None | DetalhamentoDaComposicaoMusical
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-COMPOSICAO-MUSICAL",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CultivarProtegida:
    class Meta:
        name = "CULTIVAR-PROTEGIDA"

    dados_basicos_da_cultivar: None | DadosBasicosDaCultivar = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-CULTIVAR",
            "type": "Element",
        },
    )
    detalhamento_da_cultivar: None | DetalhamentoDaCultivar = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-CULTIVAR",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CultivarRegistrada:
    class Meta:
        name = "CULTIVAR-REGISTRADA"

    dados_basicos_da_cultivar: None | DadosBasicosDaCultivar = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-CULTIVAR",
            "type": "Element",
        },
    )
    detalhamento_da_cultivar: None | DetalhamentoDaCultivar = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-CULTIVAR",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CursoDeCurtaDuracao:
    class Meta:
        name = "CURSO-DE-CURTA-DURACAO"

    dados_basicos_do_curso_de_curta_duracao: (
        None | DadosBasicosDoCursoDeCurtaDuracao
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-CURSO-DE-CURTA-DURACAO",
            "type": "Element",
        },
    )
    detalhamento_do_curso_de_curta_duracao: (
        None | DetalhamentoDoCursoDeCurtaDuracao
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-CURSO-DE-CURTA-DURACAO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CursoDeCurtaDuracaoMinistrado:
    class Meta:
        name = "CURSO-DE-CURTA-DURACAO-MINISTRADO"

    dados_basicos_de_cursos_curta_duracao_ministrado: (
        None | DadosBasicosDeCursosCurtaDuracaoMinistrado
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-CURSOS-CURTA-DURACAO-MINISTRADO",
            "type": "Element",
        },
    )
    detalhamento_de_cursos_curta_duracao_ministrado: (
        None | DetalhamentoDeCursosCurtaDuracaoMinistrado
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-CURSOS-CURTA-DURACAO-MINISTRADO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DemaisTrabalhos:
    class Meta:
        name = "DEMAIS-TRABALHOS"

    dados_basicos_de_demais_trabalhos: None | DadosBasicosDeDemaisTrabalhos = (
        field(
            default=None,
            metadata={
                "name": "DADOS-BASICOS-DE-DEMAIS-TRABALHOS",
                "type": "Element",
            },
        )
    )
    detalhamento_de_demais_trabalhos: None | DetalhamentoDeDemaisTrabalhos = (
        field(
            default=None,
            metadata={
                "name": "DETALHAMENTO-DE-DEMAIS-TRABALHOS",
                "type": "Element",
            },
        )
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DesenhoIndustrial:
    class Meta:
        name = "DESENHO-INDUSTRIAL"

    dados_basicos_do_desenho_industrial: (
        None | DadosBasicosDoDesenhoIndustrial
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-DESENHO-INDUSTRIAL",
            "type": "Element",
        },
    )
    detalhamento_do_desenho_industrial: (
        None | DetalhamentoDoDesenhoIndustrial
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-DESENHO-INDUSTRIAL",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DesenvolvimentoDeMaterialDidaticoOuInstrucional:
    class Meta:
        name = "DESENVOLVIMENTO-DE-MATERIAL-DIDATICO-OU-INSTRUCIONAL"

    dados_basicos_do_material_didatico_ou_instrucional: (
        None | DadosBasicosDoMaterialDidaticoOuInstrucional
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-MATERIAL-DIDATICO-OU-INSTRUCIONAL",
            "type": "Element",
        },
    )
    detalhamento_do_material_didatico_ou_instrucional: (
        None | DetalhamentoDoMaterialDidaticoOuInstrucional
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-MATERIAL-DIDATICO-OU-INSTRUCIONAL",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doutorado:
    class Meta:
        name = "DOUTORADO"

    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    codigo_area_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AREA-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | DoutoradoStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-AGENCIA",
            "type": "Attribute",
        },
    )
    ano_de_obtencao_do_titulo: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-OBTENCAO-DO-TITULO",
            "type": "Attribute",
        },
    )
    titulo_da_dissertacao_tese: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-DISSERTACAO-TESE",
            "type": "Attribute",
        },
    )
    nome_completo_do_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NOME-COMPLETO-DO-ORIENTADOR",
            "type": "Attribute",
        },
    )
    tipo_doutorado: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-DOUTORADO",
            "type": "Attribute",
        },
    )
    codigo_instituicao_dout: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-DOUT",
            "type": "Attribute",
        },
    )
    nome_instituicao_dout: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO-DOUT",
            "type": "Attribute",
        },
    )
    codigo_instituicao_outra_dout: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-OUTRA-DOUT",
            "type": "Attribute",
        },
    )
    nome_instituicao_outra_dout: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO-OUTRA-DOUT",
            "type": "Attribute",
        },
    )
    nome_orientador_dout: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORIENTADOR-DOUT",
            "type": "Attribute",
        },
    )
    numero_id_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTADOR",
            "type": "Attribute",
        },
    )
    codigo_curso_capes: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO-CAPES",
            "type": "Attribute",
        },
    )
    titulo_da_dissertacao_tese_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-DISSERTACAO-TESE-INGLES",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )
    nome_do_orientador_co_tutela: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTADOR-CO-TUTELA",
            "type": "Attribute",
        },
    )
    codigo_instituicao_outra_co_tutela: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-OUTRA-CO-TUTELA",
            "type": "Attribute",
        },
    )
    codigo_instituicao_co_tutela: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-CO-TUTELA",
            "type": "Attribute",
        },
    )
    nome_do_orientador_sanduiche: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ORIENTADOR-SANDUICHE",
            "type": "Attribute",
        },
    )
    codigo_instituicao_outra_sanduiche: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-OUTRA-SANDUICHE",
            "type": "Attribute",
        },
    )
    codigo_instituicao_sanduiche: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-SANDUICHE",
            "type": "Attribute",
        },
    )
    nome_do_co_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CO-ORIENTADOR",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Editoracao:
    class Meta:
        name = "EDITORACAO"

    dados_basicos_de_editoracao: None | DadosBasicosDeEditoracao = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-EDITORACAO",
            "type": "Element",
        },
    )
    detalhamento_de_editoracao: None | DetalhamentoDeEditoracao = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-EDITORACAO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class LinhaDePesquisa:
    class Meta:
        name = "LINHA-DE-PESQUISA"

    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    sequencia_linha: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-LINHA",
            "type": "Attribute",
        },
    )
    titulo_da_linha_de_pesquisa: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-LINHA-DE-PESQUISA",
            "type": "Attribute",
        },
    )
    flag_linha_de_pesquisa_ativa: (
        None | LinhaDePesquisaFlagLinhaDePesquisaAtiva
    ) = field(
        default=None,
        metadata={
            "name": "FLAG-LINHA-DE-PESQUISA-ATIVA",
            "type": "Attribute",
        },
    )
    objetivos_linha_de_pesquisa: None | object = field(
        default=None,
        metadata={
            "name": "OBJETIVOS-LINHA-DE-PESQUISA",
            "type": "Attribute",
        },
    )
    titulo_da_linha_de_pesquisa_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-LINHA-DE-PESQUISA-INGLES",
            "type": "Attribute",
        },
    )
    objetivos_linha_de_pesquisa_ingles: None | object = field(
        default=None,
        metadata={
            "name": "OBJETIVOS-LINHA-DE-PESQUISA-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class LivreDocencia:
    class Meta:
        name = "LIVRE-DOCENCIA"

    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    ano_de_obtencao_do_titulo: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-OBTENCAO-DO-TITULO",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class LivroPublicadoOuOrganizado:
    class Meta:
        name = "LIVRO-PUBLICADO-OU-ORGANIZADO"

    dados_basicos_do_livro: None | DadosBasicosDoLivro = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-LIVRO",
            "type": "Element",
        },
    )
    detalhamento_do_livro: None | DetalhamentoDoLivro = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-LIVRO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ManutencaoDeObraArtistica:
    class Meta:
        name = "MANUTENCAO-DE-OBRA-ARTISTICA"

    dados_basicos_de_manutencao_de_obra_artistica: (
        None | DadosBasicosDeManutencaoDeObraArtistica
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-MANUTENCAO-DE-OBRA-ARTISTICA",
            "type": "Element",
        },
    )
    detalhamento_de_manutencao_de_obra_artistica: (
        None | DetalhamentoDeManutencaoDeObraArtistica
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-MANUTENCAO-DE-OBRA-ARTISTICA",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Maquete:
    class Meta:
        name = "MAQUETE"

    dados_basicos_da_maquete: None | DadosBasicosDaMaquete = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-MAQUETE",
            "type": "Element",
        },
    )
    detalhamento_da_maquete: None | DetalhamentoDaMaquete = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-MAQUETE",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Marca:
    class Meta:
        name = "MARCA"

    dados_basicos_da_marca: None | DadosBasicosDaMarca = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-MARCA",
            "type": "Element",
        },
    )
    detalhamento_da_marca: None | DetalhamentoDaMarca = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-MARCA",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Mba:
    class Meta:
        name = "MBA"

    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    carga_horaria: None | object = field(
        default=None,
        metadata={
            "name": "CARGA-HORARIA",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | MbaStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    ano_de_obtencao_do_titulo: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-OBTENCAO-DO-TITULO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-AGENCIA",
            "type": "Attribute",
        },
    )
    titulo_da_monografia: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-MONOGRAFIA",
            "type": "Attribute",
        },
    )
    nome_completo_do_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NOME-COMPLETO-DO-ORIENTADOR",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Mestrado:
    class Meta:
        name = "MESTRADO"

    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    codigo_area_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AREA-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | MestradoStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-AGENCIA",
            "type": "Attribute",
        },
    )
    ano_de_obtencao_do_titulo: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-OBTENCAO-DO-TITULO",
            "type": "Attribute",
        },
    )
    titulo_da_dissertacao_tese: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-DISSERTACAO-TESE",
            "type": "Attribute",
        },
    )
    nome_completo_do_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NOME-COMPLETO-DO-ORIENTADOR",
            "type": "Attribute",
        },
    )
    tipo_mestrado: None | object = field(
        default=None,
        metadata={
            "name": "TIPO-MESTRADO",
            "type": "Attribute",
        },
    )
    numero_id_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTADOR",
            "type": "Attribute",
        },
    )
    codigo_curso_capes: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO-CAPES",
            "type": "Attribute",
        },
    )
    titulo_da_dissertacao_tese_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-DISSERTACAO-TESE-INGLES",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )
    nome_do_co_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CO-ORIENTADOR",
            "type": "Attribute",
        },
    )
    codigo_instituicao_dout: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-DOUT",
            "type": "Attribute",
        },
    )
    nome_instituicao_dout: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO-DOUT",
            "type": "Attribute",
        },
    )
    codigo_instituicao_outra_dout: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO-OUTRA-DOUT",
            "type": "Attribute",
        },
    )
    nome_instituicao_outra_dout: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO-OUTRA-DOUT",
            "type": "Attribute",
        },
    )
    nome_orientador_dout: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORIENTADOR-DOUT",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MestradoProfissionalizante:
    class Meta:
        name = "MESTRADO-PROFISSIONALIZANTE"

    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO",
            "type": "Attribute",
        },
    )
    nome_curso: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO",
            "type": "Attribute",
        },
    )
    codigo_area_curso: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AREA-CURSO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | MestradoProfissionalizanteStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-AGENCIA",
            "type": "Attribute",
        },
    )
    ano_de_obtencao_do_titulo: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-OBTENCAO-DO-TITULO",
            "type": "Attribute",
        },
    )
    titulo_da_dissertacao_tese: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-DISSERTACAO-TESE",
            "type": "Attribute",
        },
    )
    nome_completo_do_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NOME-COMPLETO-DO-ORIENTADOR",
            "type": "Attribute",
        },
    )
    numero_id_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTADOR",
            "type": "Attribute",
        },
    )
    codigo_curso_capes: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO-CAPES",
            "type": "Attribute",
        },
    )
    titulo_da_dissertacao_tese_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-DISSERTACAO-TESE-INGLES",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )
    nome_do_co_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-CO-ORIENTADOR",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class MidiaSocialWebsiteBlog:
    class Meta:
        name = "MIDIA-SOCIAL-WEBSITE-BLOG"

    dados_basicos_da_midia_social_website_blog: (
        None | DadosBasicosDaMidiaSocialWebsiteBlog
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-MIDIA-SOCIAL-WEBSITE-BLOG",
            "type": "Element",
        },
    )
    detalhamento_da_midia_social_website_blog: (
        None | DetalhamentoDaMidiaSocialWebsiteBlog
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-MIDIA-SOCIAL-WEBSITE-BLOG",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Musica:
    class Meta:
        name = "MUSICA"

    dados_basicos_da_musica: None | DadosBasicosDaMusica = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-MUSICA",
            "type": "Element",
        },
    )
    detalhamento_da_musica: None | DetalhamentoDaMusica = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-MUSICA",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ObraDeArtesVisuais:
    class Meta:
        name = "OBRA-DE-ARTES-VISUAIS"

    dados_basicos_da_obra_de_artes_visuais: (
        None | DadosBasicosDaObraDeArtesVisuais
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-OBRA-DE-ARTES-VISUAIS",
            "type": "Element",
        },
    )
    detalhamento_da_obra_de_artes_visuais: (
        None | DetalhamentoDaObraDeArtesVisuais
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-OBRA-DE-ARTES-VISUAIS",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrganizacaoDeEvento:
    class Meta:
        name = "ORGANIZACAO-DE-EVENTO"

    dados_basicos_da_organizacao_de_evento: (
        None | DadosBasicosDaOrganizacaoDeEvento
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-ORGANIZACAO-DE-EVENTO",
            "type": "Element",
        },
    )
    detalhamento_da_organizacao_de_evento: (
        None | DetalhamentoDaOrganizacaoDeEvento
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-ORGANIZACAO-DE-EVENTO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrientacaoEmAndamentoDeAperfeicoamentoEspecializacao:
    class Meta:
        name = "ORIENTACAO-EM-ANDAMENTO-DE-APERFEICOAMENTO-ESPECIALIZACAO"

    dados_basicos_da_orientacao_em_andamento_de_aperfeicoamento_especializacao: (
        None
        | DadosBasicosDaOrientacaoEmAndamentoDeAperfeicoamentoEspecializacao
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-APERFEICOAMENTO-ESPECIALIZACAO",
            "type": "Element",
        },
    )
    detalhamento_da_orientacao_em_andamento_de_aperfeicoamento_especializacao: (
        None
        | DetalhamentoDaOrientacaoEmAndamentoDeAperfeicoamentoEspecializacao
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-APERFEICOAMENTO-ESPECIALIZACAO",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrientacaoEmAndamentoDeDoutorado:
    class Meta:
        name = "ORIENTACAO-EM-ANDAMENTO-DE-DOUTORADO"

    dados_basicos_da_orientacao_em_andamento_de_doutorado: (
        None | DadosBasicosDaOrientacaoEmAndamentoDeDoutorado
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-DOUTORADO",
            "type": "Element",
        },
    )
    detalhamento_da_orientacao_em_andamento_de_doutorado: (
        None | DetalhamentoDaOrientacaoEmAndamentoDeDoutorado
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-DOUTORADO",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrientacaoEmAndamentoDeGraduacao:
    class Meta:
        name = "ORIENTACAO-EM-ANDAMENTO-DE-GRADUACAO"

    dados_basicos_da_orientacao_em_andamento_de_graduacao: (
        None | DadosBasicosDaOrientacaoEmAndamentoDeGraduacao
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-GRADUACAO",
            "type": "Element",
        },
    )
    detalhamento_da_orientacao_em_andamento_de_graduacao: (
        None | DetalhamentoDaOrientacaoEmAndamentoDeGraduacao
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-GRADUACAO",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrientacaoEmAndamentoDeIniciacaoCientifica:
    class Meta:
        name = "ORIENTACAO-EM-ANDAMENTO-DE-INICIACAO-CIENTIFICA"

    dados_basicos_da_orientacao_em_andamento_de_iniciacao_cientifica: (
        None | DadosBasicosDaOrientacaoEmAndamentoDeIniciacaoCientifica
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-INICIACAO-CIENTIFICA",
            "type": "Element",
        },
    )
    detalhamento_da_orientacao_em_andamento_de_iniciacao_cientifica: (
        None | DetalhamentoDaOrientacaoEmAndamentoDeIniciacaoCientifica
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-INICIACAO-CIENTIFICA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrientacaoEmAndamentoDeMestrado:
    class Meta:
        name = "ORIENTACAO-EM-ANDAMENTO-DE-MESTRADO"

    dados_basicos_da_orientacao_em_andamento_de_mestrado: (
        None | DadosBasicosDaOrientacaoEmAndamentoDeMestrado
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-MESTRADO",
            "type": "Element",
        },
    )
    detalhamento_da_orientacao_em_andamento_de_mestrado: (
        None | DetalhamentoDaOrientacaoEmAndamentoDeMestrado
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-MESTRADO",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrientacaoEmAndamentoDePosDoutorado:
    class Meta:
        name = "ORIENTACAO-EM-ANDAMENTO-DE-POS-DOUTORADO"

    dados_basicos_da_orientacao_em_andamento_de_pos_doutorado: (
        None | DadosBasicosDaOrientacaoEmAndamentoDePosDoutorado
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-ORIENTACAO-EM-ANDAMENTO-DE-POS-DOUTORADO",
            "type": "Element",
        },
    )
    detalhamento_da_orientacao_em_andamento_de_pos_doutorado: (
        None | DetalhamentoDaOrientacaoEmAndamentoDePosDoutorado
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-ORIENTACAO-EM-ANDAMENTO-DE-POS-DOUTORADO",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrientacoesConcluidasParaDoutorado:
    class Meta:
        name = "ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO"

    dados_basicos_de_orientacoes_concluidas_para_doutorado: (
        None | DadosBasicosDeOrientacoesConcluidasParaDoutorado
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO",
            "type": "Element",
        },
    )
    detalhamento_de_orientacoes_concluidas_para_doutorado: (
        None | DetalhamentoDeOrientacoesConcluidasParaDoutorado
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrientacoesConcluidasParaMestrado:
    class Meta:
        name = "ORIENTACOES-CONCLUIDAS-PARA-MESTRADO"

    dados_basicos_de_orientacoes_concluidas_para_mestrado: (
        None | DadosBasicosDeOrientacoesConcluidasParaMestrado
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO",
            "type": "Element",
        },
    )
    detalhamento_de_orientacoes_concluidas_para_mestrado: (
        None | DetalhamentoDeOrientacoesConcluidasParaMestrado
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-MESTRADO",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OrientacoesConcluidasParaPosDoutorado:
    class Meta:
        name = "ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO"

    dados_basicos_de_orientacoes_concluidas_para_pos_doutorado: (
        None | DadosBasicosDeOrientacoesConcluidasParaPosDoutorado
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO",
            "type": "Element",
        },
    )
    detalhamento_de_orientacoes_concluidas_para_pos_doutorado: (
        None | DetalhamentoDeOrientacoesConcluidasParaPosDoutorado
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OutraProducaoArtisticaCultural:
    class Meta:
        name = "OUTRA-PRODUCAO-ARTISTICA-CULTURAL"

    dados_basicos_de_outra_producao_artistica_cultural: (
        None | DadosBasicosDeOutraProducaoArtisticaCultural
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-OUTRA-PRODUCAO-ARTISTICA-CULTURAL",
            "type": "Element",
        },
    )
    detalhamento_de_outra_producao_artistica_cultural: (
        None | DetalhamentoDeOutraProducaoArtisticaCultural
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-OUTRA-PRODUCAO-ARTISTICA-CULTURAL",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OutraProducaoBibliografica:
    class Meta:
        name = "OUTRA-PRODUCAO-BIBLIOGRAFICA"

    dados_basicos_de_outra_producao: None | DadosBasicosDeOutraProducao = (
        field(
            default=None,
            metadata={
                "name": "DADOS-BASICOS-DE-OUTRA-PRODUCAO",
                "type": "Element",
            },
        )
    )
    detalhamento_de_outra_producao: None | DetalhamentoDeOutraProducao = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-OUTRA-PRODUCAO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OutraProducaoTecnica:
    class Meta:
        name = "OUTRA-PRODUCAO-TECNICA"

    dados_basicos_de_outra_producao_tecnica: (
        None | DadosBasicosDeOutraProducaoTecnica
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-OUTRA-PRODUCAO-TECNICA",
            "type": "Element",
        },
    )
    detalhamento_de_outra_producao_tecnica: (
        None | DetalhamentoDeOutraProducaoTecnica
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-OUTRA-PRODUCAO-TECNICA",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    registro_ou_patente: None | RegistroOuPatente = field(
        default=None,
        metadata={
            "name": "REGISTRO-OU-PATENTE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OutrasBancasJulgadoras:
    class Meta:
        name = "OUTRAS-BANCAS-JULGADORAS"

    dados_basicos_de_outras_bancas_julgadoras: (
        None | DadosBasicosDeOutrasBancasJulgadoras
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-OUTRAS-BANCAS-JULGADORAS",
            "type": "Element",
        },
    )
    detalhamento_de_outras_bancas_julgadoras: (
        None | DetalhamentoDeOutrasBancasJulgadoras
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-OUTRAS-BANCAS-JULGADORAS",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OutrasOrientacoesConcluidas:
    class Meta:
        name = "OUTRAS-ORIENTACOES-CONCLUIDAS"

    dados_basicos_de_outras_orientacoes_concluidas: (
        None | DadosBasicosDeOutrasOrientacoesConcluidas
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-OUTRAS-ORIENTACOES-CONCLUIDAS",
            "type": "Element",
        },
    )
    detalhamento_de_outras_orientacoes_concluidas: (
        None | DetalhamentoDeOutrasOrientacoesConcluidas
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-OUTRAS-ORIENTACOES-CONCLUIDAS",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OutrasOrientacoesEmAndamento:
    class Meta:
        name = "OUTRAS-ORIENTACOES-EM-ANDAMENTO"

    dados_basicos_de_outras_orientacoes_em_andamento: (
        None | DadosBasicosDeOutrasOrientacoesEmAndamento
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-OUTRAS-ORIENTACOES-EM-ANDAMENTO",
            "type": "Element",
        },
    )
    detalhamento_de_outras_orientacoes_em_andamento: (
        None | DetalhamentoDeOutrasOrientacoesEmAndamento
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-OUTRAS-ORIENTACOES-EM-ANDAMENTO",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OutrasParticipacoesEmBanca:
    class Meta:
        name = "OUTRAS-PARTICIPACOES-EM-BANCA"

    dados_basicos_de_outras_participacoes_em_banca: (
        None | DadosBasicosDeOutrasParticipacoesEmBanca
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-OUTRAS-PARTICIPACOES-EM-BANCA",
            "type": "Element",
        },
    )
    detalhamento_de_outras_participacoes_em_banca: (
        None | DetalhamentoDeOutrasParticipacoesEmBanca
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-OUTRAS-PARTICIPACOES-EM-BANCA",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OutrasParticipacoesEmEventosCongressos:
    class Meta:
        name = "OUTRAS-PARTICIPACOES-EM-EVENTOS-CONGRESSOS"

    dados_basicos_de_outras_participacoes_em_eventos_congressos: (
        None | DadosBasicosDeOutrasParticipacoesEmEventosCongressos
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-OUTRAS-PARTICIPACOES-EM-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    detalhamento_de_outras_participacoes_em_eventos_congressos: (
        None | DetalhamentoDeOutrasParticipacoesEmEventosCongressos
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-OUTRAS-PARTICIPACOES-EM-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    participante_de_eventos_congressos: list[
        ParticipanteDeEventosCongressos
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmBancaDeAperfeicoamentoEspecializacao:
    class Meta:
        name = "PARTICIPACAO-EM-BANCA-DE-APERFEICOAMENTO-ESPECIALIZACAO"

    dados_basicos_da_participacao_em_banca_de_aperfeicoamento_especializacao: (
        None | DadosBasicosDaParticipacaoEmBancaDeAperfeicoamentoEspecializacao
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-BANCA-DE-APERFEICOAMENTO-ESPECIALIZACAO",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_banca_de_aperfeicoamento_especializacao: (
        None | DetalhamentoDaParticipacaoEmBancaDeAperfeicoamentoEspecializacao
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-BANCA-DE-APERFEICOAMENTO-ESPECIALIZACAO",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmBancaDeDoutorado:
    class Meta:
        name = "PARTICIPACAO-EM-BANCA-DE-DOUTORADO"

    dados_basicos_da_participacao_em_banca_de_doutorado: (
        None | DadosBasicosDaParticipacaoEmBancaDeDoutorado
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-BANCA-DE-DOUTORADO",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_banca_de_doutorado: (
        None | DetalhamentoDaParticipacaoEmBancaDeDoutorado
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-BANCA-DE-DOUTORADO",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmBancaDeExameQualificacao:
    class Meta:
        name = "PARTICIPACAO-EM-BANCA-DE-EXAME-QUALIFICACAO"

    dados_basicos_da_participacao_em_banca_de_exame_qualificacao: (
        None | DadosBasicosDaParticipacaoEmBancaDeExameQualificacao
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-BANCA-DE-EXAME-QUALIFICACAO",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_banca_de_exame_qualificacao: (
        None | DetalhamentoDaParticipacaoEmBancaDeExameQualificacao
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-BANCA-DE-EXAME-QUALIFICACAO",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmBancaDeGraduacao:
    class Meta:
        name = "PARTICIPACAO-EM-BANCA-DE-GRADUACAO"

    dados_basicos_da_participacao_em_banca_de_graduacao: (
        None | DadosBasicosDaParticipacaoEmBancaDeGraduacao
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-BANCA-DE-GRADUACAO",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_banca_de_graduacao: (
        None | DetalhamentoDaParticipacaoEmBancaDeGraduacao
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-BANCA-DE-GRADUACAO",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmBancaDeMestrado:
    class Meta:
        name = "PARTICIPACAO-EM-BANCA-DE-MESTRADO"

    dados_basicos_da_participacao_em_banca_de_mestrado: (
        None | DadosBasicosDaParticipacaoEmBancaDeMestrado
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-BANCA-DE-MESTRADO",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_banca_de_mestrado: (
        None | DetalhamentoDaParticipacaoEmBancaDeMestrado
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-BANCA-DE-MESTRADO",
            "type": "Element",
        },
    )
    participante_banca: list[ParticipanteBanca] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-BANCA",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmCongresso:
    class Meta:
        name = "PARTICIPACAO-EM-CONGRESSO"

    dados_basicos_da_participacao_em_congresso: (
        None | DadosBasicosDaParticipacaoEmCongresso
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-CONGRESSO",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_congresso: (
        None | DetalhamentoDaParticipacaoEmCongresso
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-CONGRESSO",
            "type": "Element",
        },
    )
    participante_de_eventos_congressos: list[
        ParticipanteDeEventosCongressos
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmEncontro:
    class Meta:
        name = "PARTICIPACAO-EM-ENCONTRO"

    dados_basicos_da_participacao_em_encontro: (
        None | DadosBasicosDaParticipacaoEmEncontro
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-ENCONTRO",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_encontro: (
        None | DetalhamentoDaParticipacaoEmEncontro
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-ENCONTRO",
            "type": "Element",
        },
    )
    participante_de_eventos_congressos: list[
        ParticipanteDeEventosCongressos
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmExposicao:
    class Meta:
        name = "PARTICIPACAO-EM-EXPOSICAO"

    dados_basicos_da_participacao_em_exposicao: (
        None | DadosBasicosDaParticipacaoEmExposicao
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-EXPOSICAO",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_exposicao: (
        None | DetalhamentoDaParticipacaoEmExposicao
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-EXPOSICAO",
            "type": "Element",
        },
    )
    participante_de_eventos_congressos: list[
        ParticipanteDeEventosCongressos
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmFeira:
    class Meta:
        name = "PARTICIPACAO-EM-FEIRA"

    dados_basicos_da_participacao_em_feira: (
        None | DadosBasicosDaParticipacaoEmFeira
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-FEIRA",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_feira: (
        None | DetalhamentoDaParticipacaoEmFeira
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-FEIRA",
            "type": "Element",
        },
    )
    participante_de_eventos_congressos: list[
        ParticipanteDeEventosCongressos
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmOficina:
    class Meta:
        name = "PARTICIPACAO-EM-OFICINA"

    dados_basicos_da_participacao_em_oficina: (
        None | DadosBasicosDaParticipacaoEmOficina
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-OFICINA",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_oficina: (
        None | DetalhamentoDaParticipacaoEmOficina
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-OFICINA",
            "type": "Element",
        },
    )
    participante_de_eventos_congressos: list[
        ParticipanteDeEventosCongressos
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmOlimpiada:
    class Meta:
        name = "PARTICIPACAO-EM-OLIMPIADA"

    dados_basicos_da_participacao_em_olimpiada: (
        None | DadosBasicosDaParticipacaoEmOlimpiada
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-OLIMPIADA",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_olimpiada: (
        None | DetalhamentoDaParticipacaoEmOlimpiada
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-OLIMPIADA",
            "type": "Element",
        },
    )
    participante_de_eventos_congressos: list[
        ParticipanteDeEventosCongressos
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmSeminario:
    class Meta:
        name = "PARTICIPACAO-EM-SEMINARIO"

    dados_basicos_da_participacao_em_seminario: (
        None | DadosBasicosDaParticipacaoEmSeminario
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-SEMINARIO",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_seminario: (
        None | DetalhamentoDaParticipacaoEmSeminario
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-SEMINARIO",
            "type": "Element",
        },
    )
    participante_de_eventos_congressos: list[
        ParticipanteDeEventosCongressos
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmSimposio:
    class Meta:
        name = "PARTICIPACAO-EM-SIMPOSIO"

    dados_basicos_da_participacao_em_simposio: (
        None | DadosBasicosDaParticipacaoEmSimposio
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTICIPACAO-EM-SIMPOSIO",
            "type": "Element",
        },
    )
    detalhamento_da_participacao_em_simposio: (
        None | DetalhamentoDaParticipacaoEmSimposio
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTICIPACAO-EM-SIMPOSIO",
            "type": "Element",
        },
    )
    participante_de_eventos_congressos: list[
        ParticipanteDeEventosCongressos
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPANTE-DE-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PartituraMusical:
    class Meta:
        name = "PARTITURA-MUSICAL"

    dados_basicos_da_partitura: None | DadosBasicosDaPartitura = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PARTITURA",
            "type": "Element",
        },
    )
    detalhamento_da_partitura: None | DetalhamentoDaPartitura = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PARTITURA",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Patente:
    class Meta:
        name = "PATENTE"

    dados_basicos_da_patente: None | DadosBasicosDaPatente = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-PATENTE",
            "type": "Element",
        },
    )
    detalhamento_da_patente: None | DetalhamentoDaPatente = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-PATENTE",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PosDoutorado:
    class Meta:
        name = "POS-DOUTORADO"

    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    ano_de_obtencao_do_titulo: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-OBTENCAO-DO-TITULO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-AGENCIA",
            "type": "Attribute",
        },
    )
    status_do_estagio: None | object = field(
        default=None,
        metadata={
            "name": "STATUS-DO-ESTAGIO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | object = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    numero_id_orientador: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ID-ORIENTADOR",
            "type": "Attribute",
        },
    )
    codigo_curso_capes: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-CURSO-CAPES",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO",
            "type": "Attribute",
        },
    )
    titulo_do_trabalho_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DO-TRABALHO-INGLES",
            "type": "Attribute",
        },
    )
    nome_curso_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-CURSO-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PrefacioPosfacio:
    class Meta:
        name = "PREFACIO-POSFACIO"

    dados_basicos_do_prefacio_posfacio: (
        None | DadosBasicosDoPrefacioPosfacio
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-PREFACIO-POSFACIO",
            "type": "Element",
        },
    )
    detalhamento_do_prefacio_posfacio: (
        None | DetalhamentoDoPrefacioPosfacio
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-PREFACIO-POSFACIO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ProcessosOuTecnicas:
    class Meta:
        name = "PROCESSOS-OU-TECNICAS"

    dados_basicos_do_processos_ou_tecnicas: (
        None | DadosBasicosDoProcessosOuTecnicas
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-PROCESSOS-OU-TECNICAS",
            "type": "Element",
        },
    )
    detalhamento_do_processos_ou_tecnicas: (
        None | DetalhamentoDoProcessosOuTecnicas
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-PROCESSOS-OU-TECNICAS",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ProdutoTecnologico:
    class Meta:
        name = "PRODUTO-TECNOLOGICO"

    dados_basicos_do_produto_tecnologico: DadosBasicosDoProdutoTecnologico = (
        field(
            metadata={
                "name": "DADOS-BASICOS-DO-PRODUTO-TECNOLOGICO",
                "type": "Element",
            }
        )
    )
    detalhamento_do_produto_tecnologico: DetalhamentoDoProdutoTecnologico = (
        field(
            metadata={
                "name": "DETALHAMENTO-DO-PRODUTO-TECNOLOGICO",
                "type": "Element",
            }
        )
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ProgramaDeRadioOuTv:
    class Meta:
        name = "PROGRAMA-DE-RADIO-OU-TV"

    dados_basicos_do_programa_de_radio_ou_tv: (
        None | DadosBasicosDoProgramaDeRadioOuTv
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-PROGRAMA-DE-RADIO-OU-TV",
            "type": "Element",
        },
    )
    detalhamento_do_programa_de_radio_ou_tv: (
        None | DetalhamentoDoProgramaDeRadioOuTv
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-PROGRAMA-DE-RADIO-OU-TV",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ProjetoDePesquisa:
    class Meta:
        name = "PROJETO-DE-PESQUISA"

    equipe_do_projeto: None | EquipeDoProjeto = field(
        default=None,
        metadata={
            "name": "EQUIPE-DO-PROJETO",
            "type": "Element",
        },
    )
    financiadores_do_projeto: None | FinanciadoresDoProjeto = field(
        default=None,
        metadata={
            "name": "FINANCIADORES-DO-PROJETO",
            "type": "Element",
        },
    )
    producoes_ct_do_projeto: None | ProducoesCtDoProjeto = field(
        default=None,
        metadata={
            "name": "PRODUCOES-CT-DO-PROJETO",
            "type": "Element",
        },
    )
    orientacoes: None | Orientacoes = field(
        default=None,
        metadata={
            "name": "ORIENTACOES",
            "type": "Element",
        },
    )
    sequencia_projeto: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PROJETO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    nome_do_projeto: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-PROJETO",
            "type": "Attribute",
        },
    )
    situacao: None | ProjetoDePesquisaSituacao = field(
        default=None,
        metadata={
            "name": "SITUACAO",
            "type": "Attribute",
        },
    )
    natureza: None | ProjetoDePesquisaNatureza = field(
        default=None,
        metadata={
            "name": "NATUREZA",
            "type": "Attribute",
        },
    )
    numero_graduacao: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-GRADUACAO",
            "type": "Attribute",
        },
    )
    numero_especializacao: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-ESPECIALIZACAO",
            "type": "Attribute",
        },
    )
    numero_mestrado_academico: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-MESTRADO-ACADEMICO",
            "type": "Attribute",
        },
    )
    numero_mestrado_prof: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-MESTRADO-PROF",
            "type": "Attribute",
        },
    )
    numero_doutorado: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DOUTORADO",
            "type": "Attribute",
        },
    )
    descricao_do_projeto: None | object = field(
        default=None,
        metadata={
            "name": "DESCRICAO-DO-PROJETO",
            "type": "Attribute",
        },
    )
    identificador_projeto: None | object = field(
        default=None,
        metadata={
            "name": "IDENTIFICADOR-PROJETO",
            "type": "Attribute",
        },
    )
    descricao_do_projeto_ingles: None | object = field(
        default=None,
        metadata={
            "name": "DESCRICAO-DO-PROJETO-INGLES",
            "type": "Attribute",
        },
    )
    nome_do_projeto_ingles: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-PROJETO-INGLES",
            "type": "Attribute",
        },
    )
    flag_potencial_inovacao: ProjetoDePesquisaFlagPotencialInovacao = field(
        default=ProjetoDePesquisaFlagPotencialInovacao.NAO,
        metadata={
            "name": "FLAG-POTENCIAL-INOVACAO",
            "type": "Attribute",
        },
    )
    nome_coordenador_certificacao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-COORDENADOR-CERTIFICACAO",
            "type": "Attribute",
        },
    )
    formato_data_certificacao: ProjetoDePesquisaFormatoDataCertificacao = (
        field(
            default=ProjetoDePesquisaFormatoDataCertificacao.DDMMAAAA,
            metadata={
                "name": "FORMATO-DATA-CERTIFICACAO",
                "type": "Attribute",
            },
        )
    )
    data_certificacao: None | object = field(
        default=None,
        metadata={
            "name": "DATA-CERTIFICACAO",
            "type": "Attribute",
        },
    )
    numero_tecnico_nivel_medio: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO_TECNICO_NIVEL_MEDIO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class RelatorioDePesquisa:
    class Meta:
        name = "RELATORIO-DE-PESQUISA"

    dados_basicos_do_relatorio_de_pesquisa: (
        None | DadosBasicosDoRelatorioDePesquisa
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-RELATORIO-DE-PESQUISA",
            "type": "Element",
        },
    )
    detalhamento_do_relatorio_de_pesquisa: (
        None | DetalhamentoDoRelatorioDePesquisa
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-RELATORIO-DE-PESQUISA",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ResidenciaMedica:
    class Meta:
        name = "RESIDENCIA-MEDICA"

    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    sequencia_formacao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FORMACAO",
            "type": "Attribute",
        },
    )
    nivel: None | object = field(
        default=None,
        metadata={
            "name": "NIVEL",
            "type": "Attribute",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    status_do_curso: None | ResidenciaMedicaStatusDoCurso = field(
        default=None,
        metadata={
            "name": "STATUS-DO-CURSO",
            "type": "Attribute",
        },
    )
    ano_de_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-INICIO",
            "type": "Attribute",
        },
    )
    ano_de_conclusao: None | object = field(
        default=None,
        metadata={
            "name": "ANO-DE-CONCLUSAO",
            "type": "Attribute",
        },
    )
    flag_bolsa: None | object = field(
        default=None,
        metadata={
            "name": "FLAG-BOLSA",
            "type": "Attribute",
        },
    )
    codigo_agencia_financiadora: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-AGENCIA-FINANCIADORA",
            "type": "Attribute",
        },
    )
    nome_agencia: None | object = field(
        default=None,
        metadata={
            "name": "NOME-AGENCIA",
            "type": "Attribute",
        },
    )
    titulo_da_residencia_medica: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-RESIDENCIA-MEDICA",
            "type": "Attribute",
        },
    )
    numero_do_registro: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DO-REGISTRO",
            "type": "Attribute",
        },
    )
    titulo_da_residencia_medica_ingles: None | object = field(
        default=None,
        metadata={
            "name": "TITULO-DA-RESIDENCIA-MEDICA-INGLES",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Software:
    class Meta:
        name = "SOFTWARE"

    dados_basicos_do_software: None | DadosBasicosDoSoftware = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-SOFTWARE",
            "type": "Element",
        },
    )
    detalhamento_do_software: None | DetalhamentoDoSoftware = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-SOFTWARE",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Sonoplastia:
    class Meta:
        name = "SONOPLASTIA"

    dados_basicos_de_sonoplastia: None | DadosBasicosDeSonoplastia = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DE-SONOPLASTIA",
            "type": "Element",
        },
    )
    detalhamento_de_sonoplastia: None | DetalhamentoDeSonoplastia = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DE-SONOPLASTIA",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TextoEmJornalOuRevista:
    class Meta:
        name = "TEXTO-EM-JORNAL-OU-REVISTA"

    dados_basicos_do_texto: None | DadosBasicosDoTexto = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-TEXTO",
            "type": "Element",
        },
    )
    detalhamento_do_texto: None | DetalhamentoDoTexto = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-TEXTO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TopografiaDeCircuitoIntegrado:
    class Meta:
        name = "TOPOGRAFIA-DE-CIRCUITO-INTEGRADO"

    dados_basicos_da_topografia_de_circuito_integrado: (
        None | DadosBasicosDaTopografiaDeCircuitoIntegrado
    ) = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-TOPOGRAFIA-DE-CIRCUITO-INTEGRADO",
            "type": "Element",
        },
    )
    detalhamento_da_topografia_de_circuito_integrado: (
        None | DetalhamentoDaTopografiaDeCircuitoIntegrado
    ) = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-TOPOGRAFIA-DE-CIRCUITO-INTEGRADO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TrabalhoEmEventos:
    class Meta:
        name = "TRABALHO-EM-EVENTOS"

    dados_basicos_do_trabalho: None | DadosBasicosDoTrabalho = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DO-TRABALHO",
            "type": "Element",
        },
    )
    detalhamento_do_trabalho: None | DetalhamentoDoTrabalho = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DO-TRABALHO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TrabalhoTecnico:
    class Meta:
        name = "TRABALHO-TECNICO"

    dados_basicos_do_trabalho_tecnico: None | DadosBasicosDoTrabalhoTecnico = (
        field(
            default=None,
            metadata={
                "name": "DADOS-BASICOS-DO-TRABALHO-TECNICO",
                "type": "Element",
            },
        )
    )
    detalhamento_do_trabalho_tecnico: None | DetalhamentoDoTrabalhoTecnico = (
        field(
            default=None,
            metadata={
                "name": "DETALHAMENTO-DO-TRABALHO-TECNICO",
                "type": "Element",
            },
        )
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Traducao:
    class Meta:
        name = "TRADUCAO"

    dados_basicos_da_traducao: None | DadosBasicosDaTraducao = field(
        default=None,
        metadata={
            "name": "DADOS-BASICOS-DA-TRADUCAO",
            "type": "Element",
        },
    )
    detalhamento_da_traducao: None | DetalhamentoDaTraducao = field(
        default=None,
        metadata={
            "name": "DETALHAMENTO-DA-TRADUCAO",
            "type": "Element",
        },
    )
    autores: list[Autores] = field(
        default_factory=list,
        metadata={
            "name": "AUTORES",
            "type": "Element",
        },
    )
    palavras_chave: None | PalavrasChave = field(
        default=None,
        metadata={
            "name": "PALAVRAS-CHAVE",
            "type": "Element",
        },
    )
    areas_do_conhecimento: None | AreasDoConhecimento = field(
        default=None,
        metadata={
            "name": "AREAS-DO-CONHECIMENTO",
            "type": "Element",
        },
    )
    setores_de_atividade: None | SetoresDeAtividade = field(
        default=None,
        metadata={
            "name": "SETORES-DE-ATIVIDADE",
            "type": "Element",
        },
    )
    informacoes_adicionais: None | InformacoesAdicionais = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS",
            "type": "Element",
        },
    )
    sequencia_producao: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-PRODUCAO",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ArtigosAceitosParaPublicacao:
    class Meta:
        name = "ARTIGOS-ACEITOS-PARA-PUBLICACAO"

    artigo_aceito_para_publicacao: list[ArtigoAceitoParaPublicacao] = field(
        default_factory=list,
        metadata={
            "name": "ARTIGO-ACEITO-PARA-PUBLICACAO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ArtigosPublicados:
    class Meta:
        name = "ARTIGOS-PUBLICADOS"

    artigo_publicado: list[ArtigoPublicado] = field(
        default_factory=list,
        metadata={
            "name": "ARTIGO-PUBLICADO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CapitulosDeLivrosPublicados:
    class Meta:
        name = "CAPITULOS-DE-LIVROS-PUBLICADOS"

    capitulo_de_livro_publicado: list[CapituloDeLivroPublicado] = field(
        default_factory=list,
        metadata={
            "name": "CAPITULO-DE-LIVRO-PUBLICADO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DemaisTiposDeProducaoBibliografica:
    class Meta:
        name = "DEMAIS-TIPOS-DE-PRODUCAO-BIBLIOGRAFICA"

    outra_producao_bibliografica: list[OutraProducaoBibliografica] = field(
        default_factory=list,
        metadata={
            "name": "OUTRA-PRODUCAO-BIBLIOGRAFICA",
            "type": "Element",
        },
    )
    partitura_musical: list[PartituraMusical] = field(
        default_factory=list,
        metadata={
            "name": "PARTITURA-MUSICAL",
            "type": "Element",
        },
    )
    prefacio_posfacio: list[PrefacioPosfacio] = field(
        default_factory=list,
        metadata={
            "name": "PREFACIO-POSFACIO",
            "type": "Element",
        },
    )
    traducao: list[Traducao] = field(
        default_factory=list,
        metadata={
            "name": "TRADUCAO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DemaisTiposDeProducaoTecnica:
    class Meta:
        name = "DEMAIS-TIPOS-DE-PRODUCAO-TECNICA"

    apresentacao_de_trabalho: list[ApresentacaoDeTrabalho] = field(
        default_factory=list,
        metadata={
            "name": "APRESENTACAO-DE-TRABALHO",
            "type": "Element",
        },
    )
    carta_mapa_ou_similar: list[CartaMapaOuSimilar] = field(
        default_factory=list,
        metadata={
            "name": "CARTA-MAPA-OU-SIMILAR",
            "type": "Element",
        },
    )
    curso_de_curta_duracao_ministrado: list[CursoDeCurtaDuracaoMinistrado] = (
        field(
            default_factory=list,
            metadata={
                "name": "CURSO-DE-CURTA-DURACAO-MINISTRADO",
                "type": "Element",
            },
        )
    )
    desenvolvimento_de_material_didatico_ou_instrucional: list[
        DesenvolvimentoDeMaterialDidaticoOuInstrucional
    ] = field(
        default_factory=list,
        metadata={
            "name": "DESENVOLVIMENTO-DE-MATERIAL-DIDATICO-OU-INSTRUCIONAL",
            "type": "Element",
        },
    )
    editoracao: list[Editoracao] = field(
        default_factory=list,
        metadata={
            "name": "EDITORACAO",
            "type": "Element",
        },
    )
    manutencao_de_obra_artistica: list[ManutencaoDeObraArtistica] = field(
        default_factory=list,
        metadata={
            "name": "MANUTENCAO-DE-OBRA-ARTISTICA",
            "type": "Element",
        },
    )
    maquete: list[Maquete] = field(
        default_factory=list,
        metadata={
            "name": "MAQUETE",
            "type": "Element",
        },
    )
    organizacao_de_evento: list[OrganizacaoDeEvento] = field(
        default_factory=list,
        metadata={
            "name": "ORGANIZACAO-DE-EVENTO",
            "type": "Element",
        },
    )
    programa_de_radio_ou_tv: list[ProgramaDeRadioOuTv] = field(
        default_factory=list,
        metadata={
            "name": "PROGRAMA-DE-RADIO-OU-TV",
            "type": "Element",
        },
    )
    relatorio_de_pesquisa: list[RelatorioDePesquisa] = field(
        default_factory=list,
        metadata={
            "name": "RELATORIO-DE-PESQUISA",
            "type": "Element",
        },
    )
    midia_social_website_blog: list[MidiaSocialWebsiteBlog] = field(
        default_factory=list,
        metadata={
            "name": "MIDIA-SOCIAL-WEBSITE-BLOG",
            "type": "Element",
        },
    )
    outra_producao_tecnica: list[OutraProducaoTecnica] = field(
        default_factory=list,
        metadata={
            "name": "OUTRA-PRODUCAO-TECNICA",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FormacaoAcademicaTitulacao:
    class Meta:
        name = "FORMACAO-ACADEMICA-TITULACAO"

    graduacao: list[Graduacao] = field(
        default_factory=list,
        metadata={
            "name": "GRADUACAO",
            "type": "Element",
        },
    )
    especializacao: list[Especializacao] = field(
        default_factory=list,
        metadata={
            "name": "ESPECIALIZACAO",
            "type": "Element",
        },
    )
    mestrado: list[Mestrado] = field(
        default_factory=list,
        metadata={
            "name": "MESTRADO",
            "type": "Element",
        },
    )
    doutorado: list[Doutorado] = field(
        default_factory=list,
        metadata={
            "name": "DOUTORADO",
            "type": "Element",
        },
    )
    pos_doutorado: list[PosDoutorado] = field(
        default_factory=list,
        metadata={
            "name": "POS-DOUTORADO",
            "type": "Element",
        },
    )
    livre_docencia: list[LivreDocencia] = field(
        default_factory=list,
        metadata={
            "name": "LIVRE-DOCENCIA",
            "type": "Element",
        },
    )
    curso_tecnico_profissionalizante: list[CursoTecnicoProfissionalizante] = (
        field(
            default_factory=list,
            metadata={
                "name": "CURSO-TECNICO-PROFISSIONALIZANTE",
                "type": "Element",
            },
        )
    )
    mestrado_profissionalizante: list[MestradoProfissionalizante] = field(
        default_factory=list,
        metadata={
            "name": "MESTRADO-PROFISSIONALIZANTE",
            "type": "Element",
        },
    )
    ensino_fundamental_primeiro_grau: list[EnsinoFundamentalPrimeiroGrau] = (
        field(
            default_factory=list,
            metadata={
                "name": "ENSINO-FUNDAMENTAL-PRIMEIRO-GRAU",
                "type": "Element",
            },
        )
    )
    ensino_medio_segundo_grau: list[EnsinoMedioSegundoGrau] = field(
        default_factory=list,
        metadata={
            "name": "ENSINO-MEDIO-SEGUNDO-GRAU",
            "type": "Element",
        },
    )
    residencia_medica: list[ResidenciaMedica] = field(
        default_factory=list,
        metadata={
            "name": "RESIDENCIA-MEDICA",
            "type": "Element",
        },
    )
    aperfeicoamento: list[Aperfeicoamento] = field(
        default_factory=list,
        metadata={
            "name": "APERFEICOAMENTO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FormacaoComplementar:
    class Meta:
        name = "FORMACAO-COMPLEMENTAR"

    formacao_complementar_de_extensao_universitaria: list[
        FormacaoComplementarDeExtensaoUniversitaria
    ] = field(
        default_factory=list,
        metadata={
            "name": "FORMACAO-COMPLEMENTAR-DE-EXTENSAO-UNIVERSITARIA",
            "type": "Element",
        },
    )
    mba: list[Mba] = field(
        default_factory=list,
        metadata={
            "name": "MBA",
            "type": "Element",
        },
    )
    formacao_complementar_curso_de_curta_duracao: list[
        FormacaoComplementarCursoDeCurtaDuracao
    ] = field(
        default_factory=list,
        metadata={
            "name": "FORMACAO-COMPLEMENTAR-CURSO-DE-CURTA-DURACAO",
            "type": "Element",
        },
    )
    outros: list[Outros] = field(
        default_factory=list,
        metadata={
            "name": "OUTROS",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class LivrosPublicadosOuOrganizados:
    class Meta:
        name = "LIVROS-PUBLICADOS-OU-ORGANIZADOS"

    livro_publicado_ou_organizado: list[LivroPublicadoOuOrganizado] = field(
        default_factory=list,
        metadata={
            "name": "LIVRO-PUBLICADO-OU-ORGANIZADO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrientacoesConcluidas:
    class Meta:
        name = "ORIENTACOES-CONCLUIDAS"

    orientacoes_concluidas_para_mestrado: list[
        OrientacoesConcluidasParaMestrado
    ] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACOES-CONCLUIDAS-PARA-MESTRADO",
            "type": "Element",
        },
    )
    orientacoes_concluidas_para_doutorado: list[
        OrientacoesConcluidasParaDoutorado
    ] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACOES-CONCLUIDAS-PARA-DOUTORADO",
            "type": "Element",
        },
    )
    orientacoes_concluidas_para_pos_doutorado: list[
        OrientacoesConcluidasParaPosDoutorado
    ] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACOES-CONCLUIDAS-PARA-POS-DOUTORADO",
            "type": "Element",
        },
    )
    outras_orientacoes_concluidas: list[OutrasOrientacoesConcluidas] = field(
        default_factory=list,
        metadata={
            "name": "OUTRAS-ORIENTACOES-CONCLUIDAS",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OrientacoesEmAndamento:
    class Meta:
        name = "ORIENTACOES-EM-ANDAMENTO"

    orientacao_em_andamento_de_mestrado: list[
        OrientacaoEmAndamentoDeMestrado
    ] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACAO-EM-ANDAMENTO-DE-MESTRADO",
            "type": "Element",
        },
    )
    orientacao_em_andamento_de_doutorado: list[
        OrientacaoEmAndamentoDeDoutorado
    ] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACAO-EM-ANDAMENTO-DE-DOUTORADO",
            "type": "Element",
        },
    )
    orientacao_em_andamento_de_pos_doutorado: list[
        OrientacaoEmAndamentoDePosDoutorado
    ] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACAO-EM-ANDAMENTO-DE-POS-DOUTORADO",
            "type": "Element",
        },
    )
    orientacao_em_andamento_de_aperfeicoamento_especializacao: list[
        OrientacaoEmAndamentoDeAperfeicoamentoEspecializacao
    ] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACAO-EM-ANDAMENTO-DE-APERFEICOAMENTO-ESPECIALIZACAO",
            "type": "Element",
        },
    )
    orientacao_em_andamento_de_graduacao: list[
        OrientacaoEmAndamentoDeGraduacao
    ] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACAO-EM-ANDAMENTO-DE-GRADUACAO",
            "type": "Element",
        },
    )
    orientacao_em_andamento_de_iniciacao_cientifica: list[
        OrientacaoEmAndamentoDeIniciacaoCientifica
    ] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACAO-EM-ANDAMENTO-DE-INICIACAO-CIENTIFICA",
            "type": "Element",
        },
    )
    outras_orientacoes_em_andamento: list[OutrasOrientacoesEmAndamento] = (
        field(
            default_factory=list,
            metadata={
                "name": "OUTRAS-ORIENTACOES-EM-ANDAMENTO",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class ParticipacaoEmBancaJulgadora:
    class Meta:
        name = "PARTICIPACAO-EM-BANCA-JULGADORA"

    banca_julgadora_para_professor_titular: list[
        BancaJulgadoraParaProfessorTitular
    ] = field(
        default_factory=list,
        metadata={
            "name": "BANCA-JULGADORA-PARA-PROFESSOR-TITULAR",
            "type": "Element",
        },
    )
    banca_julgadora_para_concurso_publico: list[
        BancaJulgadoraParaConcursoPublico
    ] = field(
        default_factory=list,
        metadata={
            "name": "BANCA-JULGADORA-PARA-CONCURSO-PUBLICO",
            "type": "Element",
        },
    )
    banca_julgadora_para_livre_docencia: list[
        BancaJulgadoraParaLivreDocencia
    ] = field(
        default_factory=list,
        metadata={
            "name": "BANCA-JULGADORA-PARA-LIVRE-DOCENCIA",
            "type": "Element",
        },
    )
    banca_julgadora_para_avaliacao_cursos: list[
        BancaJulgadoraParaAvaliacaoCursos
    ] = field(
        default_factory=list,
        metadata={
            "name": "BANCA-JULGADORA-PARA-AVALIACAO-CURSOS",
            "type": "Element",
        },
    )
    outras_bancas_julgadoras: list[OutrasBancasJulgadoras] = field(
        default_factory=list,
        metadata={
            "name": "OUTRAS-BANCAS-JULGADORAS",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmBancaTrabalhosConclusao:
    class Meta:
        name = "PARTICIPACAO-EM-BANCA-TRABALHOS-CONCLUSAO"

    participacao_em_banca_de_mestrado: list[ParticipacaoEmBancaDeMestrado] = (
        field(
            default_factory=list,
            metadata={
                "name": "PARTICIPACAO-EM-BANCA-DE-MESTRADO",
                "type": "Element",
            },
        )
    )
    participacao_em_banca_de_doutorado: list[
        ParticipacaoEmBancaDeDoutorado
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-BANCA-DE-DOUTORADO",
            "type": "Element",
        },
    )
    participacao_em_banca_de_exame_qualificacao: list[
        ParticipacaoEmBancaDeExameQualificacao
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-BANCA-DE-EXAME-QUALIFICACAO",
            "type": "Element",
        },
    )
    participacao_em_banca_de_aperfeicoamento_especializacao: list[
        ParticipacaoEmBancaDeAperfeicoamentoEspecializacao
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-BANCA-DE-APERFEICOAMENTO-ESPECIALIZACAO",
            "type": "Element",
        },
    )
    participacao_em_banca_de_graduacao: list[
        ParticipacaoEmBancaDeGraduacao
    ] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-BANCA-DE-GRADUACAO",
            "type": "Element",
        },
    )
    outras_participacoes_em_banca: list[OutrasParticipacoesEmBanca] = field(
        default_factory=list,
        metadata={
            "name": "OUTRAS-PARTICIPACOES-EM-BANCA",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmEventosCongressos:
    class Meta:
        name = "PARTICIPACAO-EM-EVENTOS-CONGRESSOS"

    participacao_em_congresso: list[ParticipacaoEmCongresso] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-CONGRESSO",
            "type": "Element",
        },
    )
    participacao_em_feira: list[ParticipacaoEmFeira] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-FEIRA",
            "type": "Element",
        },
    )
    participacao_em_seminario: list[ParticipacaoEmSeminario] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-SEMINARIO",
            "type": "Element",
        },
    )
    participacao_em_simposio: list[ParticipacaoEmSimposio] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-SIMPOSIO",
            "type": "Element",
        },
    )
    participacao_em_oficina: list[ParticipacaoEmOficina] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-OFICINA",
            "type": "Element",
        },
    )
    participacao_em_encontro: list[ParticipacaoEmEncontro] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-ENCONTRO",
            "type": "Element",
        },
    )
    participacao_em_exposicao: list[ParticipacaoEmExposicao] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-EXPOSICAO",
            "type": "Element",
        },
    )
    participacao_em_olimpiada: list[ParticipacaoEmOlimpiada] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-OLIMPIADA",
            "type": "Element",
        },
    )
    outras_participacoes_em_eventos_congressos: list[
        OutrasParticipacoesEmEventosCongressos
    ] = field(
        default_factory=list,
        metadata={
            "name": "OUTRAS-PARTICIPACOES-EM-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ParticipacaoEmProjeto:
    class Meta:
        name = "PARTICIPACAO-EM-PROJETO"

    projeto_de_pesquisa: list[ProjetoDePesquisa] = field(
        default_factory=list,
        metadata={
            "name": "PROJETO-DE-PESQUISA",
            "type": "Element",
        },
    )
    sequencia_funcao_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FUNCAO-ATIVIDADE",
            "type": "Attribute",
        },
    )
    flag_periodo: None | ParticipacaoEmProjetoFlagPeriodo = field(
        default=None,
        metadata={
            "name": "FLAG-PERIODO",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_unidade: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-UNIDADE",
            "type": "Attribute",
        },
    )
    nome_unidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-UNIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class PesquisaEDesenvolvimento:
    class Meta:
        name = "PESQUISA-E-DESENVOLVIMENTO"

    linha_de_pesquisa: list[LinhaDePesquisa] = field(
        default_factory=list,
        metadata={
            "name": "LINHA-DE-PESQUISA",
            "type": "Element",
        },
    )
    sequencia_funcao_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-FUNCAO-ATIVIDADE",
            "type": "Attribute",
        },
    )
    flag_periodo: None | PesquisaEDesenvolvimentoFlagPeriodo = field(
        default=None,
        metadata={
            "name": "FLAG-PERIODO",
            "type": "Attribute",
        },
    )
    mes_inicio: None | object = field(
        default=None,
        metadata={
            "name": "MES-INICIO",
            "type": "Attribute",
        },
    )
    ano_inicio: None | object = field(
        default=None,
        metadata={
            "name": "ANO-INICIO",
            "type": "Attribute",
        },
    )
    mes_fim: None | object = field(
        default=None,
        metadata={
            "name": "MES-FIM",
            "type": "Attribute",
        },
    )
    ano_fim: None | object = field(
        default=None,
        metadata={
            "name": "ANO-FIM",
            "type": "Attribute",
        },
    )
    codigo_orgao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-ORGAO",
            "type": "Attribute",
        },
    )
    nome_orgao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-ORGAO",
            "type": "Attribute",
        },
    )
    codigo_unidade: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-UNIDADE",
            "type": "Attribute",
        },
    )
    nome_unidade: None | object = field(
        default=None,
        metadata={
            "name": "NOME-UNIDADE",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ProducaoArtisticaCultural:
    class Meta:
        name = "PRODUCAO-ARTISTICA-CULTURAL"

    apresentacao_de_obra_artistica: list[ApresentacaoDeObraArtistica] = field(
        default_factory=list,
        metadata={
            "name": "APRESENTACAO-DE-OBRA-ARTISTICA",
            "type": "Element",
        },
    )
    apresentacao_em_radio_ou_tv: list[ApresentacaoEmRadioOuTv] = field(
        default_factory=list,
        metadata={
            "name": "APRESENTACAO-EM-RADIO-OU-TV",
            "type": "Element",
        },
    )
    arranjo_musical: list[ArranjoMusical] = field(
        default_factory=list,
        metadata={
            "name": "ARRANJO-MUSICAL",
            "type": "Element",
        },
    )
    composicao_musical: list[ComposicaoMusical] = field(
        default_factory=list,
        metadata={
            "name": "COMPOSICAO-MUSICAL",
            "type": "Element",
        },
    )
    curso_de_curta_duracao: list[CursoDeCurtaDuracao] = field(
        default_factory=list,
        metadata={
            "name": "CURSO-DE-CURTA-DURACAO",
            "type": "Element",
        },
    )
    obra_de_artes_visuais: list[ObraDeArtesVisuais] = field(
        default_factory=list,
        metadata={
            "name": "OBRA-DE-ARTES-VISUAIS",
            "type": "Element",
        },
    )
    outra_producao_artistica_cultural: list[OutraProducaoArtisticaCultural] = (
        field(
            default_factory=list,
            metadata={
                "name": "OUTRA-PRODUCAO-ARTISTICA-CULTURAL",
                "type": "Element",
            },
        )
    )
    sonoplastia: list[Sonoplastia] = field(
        default_factory=list,
        metadata={
            "name": "SONOPLASTIA",
            "type": "Element",
        },
    )
    artes_cenicas: list[ArtesCenicas] = field(
        default_factory=list,
        metadata={
            "name": "ARTES-CENICAS",
            "type": "Element",
        },
    )
    artes_visuais: list[ArtesVisuais] = field(
        default_factory=list,
        metadata={
            "name": "ARTES-VISUAIS",
            "type": "Element",
        },
    )
    musica: list[Musica] = field(
        default_factory=list,
        metadata={
            "name": "MUSICA",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TextosEmJornaisOuRevistas:
    class Meta:
        name = "TEXTOS-EM-JORNAIS-OU-REVISTAS"

    texto_em_jornal_ou_revista: list[TextoEmJornalOuRevista] = field(
        default_factory=list,
        metadata={
            "name": "TEXTO-EM-JORNAL-OU-REVISTA",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TrabalhosEmEventos:
    class Meta:
        name = "TRABALHOS-EM-EVENTOS"

    trabalho_em_eventos: list[TrabalhoEmEventos] = field(
        default_factory=list,
        metadata={
            "name": "TRABALHO-EM-EVENTOS",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AtividadesDeParticipacaoEmProjeto:
    class Meta:
        name = "ATIVIDADES-DE-PARTICIPACAO-EM-PROJETO"

    participacao_em_projeto: list[ParticipacaoEmProjeto] = field(
        default_factory=list,
        metadata={
            "name": "PARTICIPACAO-EM-PROJETO",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AtividadesDePesquisaEDesenvolvimento:
    class Meta:
        name = "ATIVIDADES-DE-PESQUISA-E-DESENVOLVIMENTO"

    pesquisa_e_desenvolvimento: list[PesquisaEDesenvolvimento] = field(
        default_factory=list,
        metadata={
            "name": "PESQUISA-E-DESENVOLVIMENTO",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class DadosComplementares:
    class Meta:
        name = "DADOS-COMPLEMENTARES"

    formacao_complementar: list[FormacaoComplementar] = field(
        default_factory=list,
        metadata={
            "name": "FORMACAO-COMPLEMENTAR",
            "type": "Element",
        },
    )
    participacao_em_banca_trabalhos_conclusao: (
        None | ParticipacaoEmBancaTrabalhosConclusao
    ) = field(
        default=None,
        metadata={
            "name": "PARTICIPACAO-EM-BANCA-TRABALHOS-CONCLUSAO",
            "type": "Element",
        },
    )
    participacao_em_banca_julgadora: None | ParticipacaoEmBancaJulgadora = (
        field(
            default=None,
            metadata={
                "name": "PARTICIPACAO-EM-BANCA-JULGADORA",
                "type": "Element",
            },
        )
    )
    participacao_em_eventos_congressos: (
        None | ParticipacaoEmEventosCongressos
    ) = field(
        default=None,
        metadata={
            "name": "PARTICIPACAO-EM-EVENTOS-CONGRESSOS",
            "type": "Element",
        },
    )
    orientacoes_em_andamento: None | OrientacoesEmAndamento = field(
        default=None,
        metadata={
            "name": "ORIENTACOES-EM-ANDAMENTO",
            "type": "Element",
        },
    )
    informacoes_adicionais_instituicoes: (
        None | InformacoesAdicionaisInstituicoes
    ) = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS-INSTITUICOES",
            "type": "Element",
        },
    )
    informacoes_adicionais_cursos: None | InformacoesAdicionaisCursos = field(
        default=None,
        metadata={
            "name": "INFORMACOES-ADICIONAIS-CURSOS",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class LivrosECapitulos:
    class Meta:
        name = "LIVROS-E-CAPITULOS"

    livros_publicados_ou_organizados: None | LivrosPublicadosOuOrganizados = (
        field(
            default=None,
            metadata={
                "name": "LIVROS-PUBLICADOS-OU-ORGANIZADOS",
                "type": "Element",
            },
        )
    )
    capitulos_de_livros_publicados: None | CapitulosDeLivrosPublicados = field(
        default=None,
        metadata={
            "name": "CAPITULOS-DE-LIVROS-PUBLICADOS",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OutraProducao:
    class Meta:
        name = "OUTRA-PRODUCAO"

    producao_artistica_cultural: list[ProducaoArtisticaCultural] = field(
        default_factory=list,
        metadata={
            "name": "PRODUCAO-ARTISTICA-CULTURAL",
            "type": "Element",
        },
    )
    orientacoes_concluidas: list[OrientacoesConcluidas] = field(
        default_factory=list,
        metadata={
            "name": "ORIENTACOES-CONCLUIDAS",
            "type": "Element",
        },
    )
    demais_trabalhos: list[DemaisTrabalhos] = field(
        default_factory=list,
        metadata={
            "name": "DEMAIS-TRABALHOS",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ProducaoTecnica:
    class Meta:
        name = "PRODUCAO-TECNICA"

    cultivar_registrada: list[CultivarRegistrada] = field(
        default_factory=list,
        metadata={
            "name": "CULTIVAR-REGISTRADA",
            "type": "Element",
        },
    )
    software: list[Software] = field(
        default_factory=list,
        metadata={
            "name": "SOFTWARE",
            "type": "Element",
        },
    )
    patente: list[Patente] = field(
        default_factory=list,
        metadata={
            "name": "PATENTE",
            "type": "Element",
        },
    )
    cultivar_protegida: list[CultivarProtegida] = field(
        default_factory=list,
        metadata={
            "name": "CULTIVAR-PROTEGIDA",
            "type": "Element",
        },
    )
    desenho_industrial: list[DesenhoIndustrial] = field(
        default_factory=list,
        metadata={
            "name": "DESENHO-INDUSTRIAL",
            "type": "Element",
        },
    )
    marca: list[Marca] = field(
        default_factory=list,
        metadata={
            "name": "MARCA",
            "type": "Element",
        },
    )
    topografia_de_circuito_integrado: list[TopografiaDeCircuitoIntegrado] = (
        field(
            default_factory=list,
            metadata={
                "name": "TOPOGRAFIA-DE-CIRCUITO-INTEGRADO",
                "type": "Element",
            },
        )
    )
    produto_tecnologico: list[ProdutoTecnologico] = field(
        default_factory=list,
        metadata={
            "name": "PRODUTO-TECNOLOGICO",
            "type": "Element",
        },
    )
    processos_ou_tecnicas: list[ProcessosOuTecnicas] = field(
        default_factory=list,
        metadata={
            "name": "PROCESSOS-OU-TECNICAS",
            "type": "Element",
        },
    )
    trabalho_tecnico: list[TrabalhoTecnico] = field(
        default_factory=list,
        metadata={
            "name": "TRABALHO-TECNICO",
            "type": "Element",
        },
    )
    demais_tipos_de_producao_tecnica: list[DemaisTiposDeProducaoTecnica] = (
        field(
            default_factory=list,
            metadata={
                "name": "DEMAIS-TIPOS-DE-PRODUCAO-TECNICA",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class AtuacaoProfissional:
    class Meta:
        name = "ATUACAO-PROFISSIONAL"

    vinculos: list[Vinculos] = field(
        default_factory=list,
        metadata={
            "name": "VINCULOS",
            "type": "Element",
        },
    )
    atividades_de_direcao_e_administracao: (
        None | AtividadesDeDirecaoEAdministracao
    ) = field(
        default=None,
        metadata={
            "name": "ATIVIDADES-DE-DIRECAO-E-ADMINISTRACAO",
            "type": "Element",
        },
    )
    atividades_de_pesquisa_e_desenvolvimento: (
        None | AtividadesDePesquisaEDesenvolvimento
    ) = field(
        default=None,
        metadata={
            "name": "ATIVIDADES-DE-PESQUISA-E-DESENVOLVIMENTO",
            "type": "Element",
        },
    )
    atividades_de_ensino: None | AtividadesDeEnsino = field(
        default=None,
        metadata={
            "name": "ATIVIDADES-DE-ENSINO",
            "type": "Element",
        },
    )
    atividades_de_estagio: None | AtividadesDeEstagio = field(
        default=None,
        metadata={
            "name": "ATIVIDADES-DE-ESTAGIO",
            "type": "Element",
        },
    )
    atividades_de_servico_tecnico_especializado: (
        None | AtividadesDeServicoTecnicoEspecializado
    ) = field(
        default=None,
        metadata={
            "name": "ATIVIDADES-DE-SERVICO-TECNICO-ESPECIALIZADO",
            "type": "Element",
        },
    )
    atividades_de_extensao_universitaria: (
        None | AtividadesDeExtensaoUniversitaria
    ) = field(
        default=None,
        metadata={
            "name": "ATIVIDADES-DE-EXTENSAO-UNIVERSITARIA",
            "type": "Element",
        },
    )
    atividades_de_treinamento_ministrado: (
        None | AtividadesDeTreinamentoMinistrado
    ) = field(
        default=None,
        metadata={
            "name": "ATIVIDADES-DE-TREINAMENTO-MINISTRADO",
            "type": "Element",
        },
    )
    outras_atividades_tecnico_cientifica: (
        None | OutrasAtividadesTecnicoCientifica
    ) = field(
        default=None,
        metadata={
            "name": "OUTRAS-ATIVIDADES-TECNICO-CIENTIFICA",
            "type": "Element",
        },
    )
    atividades_de_conselho_comissao_e_consultoria: (
        None | AtividadesDeConselhoComissaoEConsultoria
    ) = field(
        default=None,
        metadata={
            "name": "ATIVIDADES-DE-CONSELHO-COMISSAO-E-CONSULTORIA",
            "type": "Element",
        },
    )
    atividades_de_participacao_em_projeto: (
        None | AtividadesDeParticipacaoEmProjeto
    ) = field(
        default=None,
        metadata={
            "name": "ATIVIDADES-DE-PARTICIPACAO-EM-PROJETO",
            "type": "Element",
        },
    )
    codigo_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "CODIGO-INSTITUICAO",
            "type": "Attribute",
        },
    )
    nome_instituicao: None | object = field(
        default=None,
        metadata={
            "name": "NOME-INSTITUICAO",
            "type": "Attribute",
        },
    )
    sequencia_atividade: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-ATIVIDADE",
            "type": "Attribute",
        },
    )
    sequencia_importancia: None | object = field(
        default=None,
        metadata={
            "name": "SEQUENCIA-IMPORTANCIA",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ProducaoBibliografica:
    class Meta:
        name = "PRODUCAO-BIBLIOGRAFICA"

    trabalhos_em_eventos: None | TrabalhosEmEventos = field(
        default=None,
        metadata={
            "name": "TRABALHOS-EM-EVENTOS",
            "type": "Element",
        },
    )
    artigos_publicados: None | ArtigosPublicados = field(
        default=None,
        metadata={
            "name": "ARTIGOS-PUBLICADOS",
            "type": "Element",
        },
    )
    livros_e_capitulos: None | LivrosECapitulos = field(
        default=None,
        metadata={
            "name": "LIVROS-E-CAPITULOS",
            "type": "Element",
        },
    )
    textos_em_jornais_ou_revistas: None | TextosEmJornaisOuRevistas = field(
        default=None,
        metadata={
            "name": "TEXTOS-EM-JORNAIS-OU-REVISTAS",
            "type": "Element",
        },
    )
    demais_tipos_de_producao_bibliografica: (
        None | DemaisTiposDeProducaoBibliografica
    ) = field(
        default=None,
        metadata={
            "name": "DEMAIS-TIPOS-DE-PRODUCAO-BIBLIOGRAFICA",
            "type": "Element",
        },
    )
    artigos_aceitos_para_publicacao: None | ArtigosAceitosParaPublicacao = (
        field(
            default=None,
            metadata={
                "name": "ARTIGOS-ACEITOS-PARA-PUBLICACAO",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class AtuacoesProfissionais:
    class Meta:
        name = "ATUACOES-PROFISSIONAIS"

    atuacao_profissional: list[AtuacaoProfissional] = field(
        default_factory=list,
        metadata={
            "name": "ATUACAO-PROFISSIONAL",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DadosGerais:
    class Meta:
        name = "DADOS-GERAIS"

    resumo_cv: None | ResumoCv = field(
        default=None,
        metadata={
            "name": "RESUMO-CV",
            "type": "Element",
        },
    )
    outras_informacoes_relevantes: None | OutrasInformacoesRelevantes = field(
        default=None,
        metadata={
            "name": "OUTRAS-INFORMACOES-RELEVANTES",
            "type": "Element",
        },
    )
    endereco: None | Endereco = field(
        default=None,
        metadata={
            "name": "ENDERECO",
            "type": "Element",
        },
    )
    formacao_academica_titulacao: None | FormacaoAcademicaTitulacao = field(
        default=None,
        metadata={
            "name": "FORMACAO-ACADEMICA-TITULACAO",
            "type": "Element",
        },
    )
    atuacoes_profissionais: None | AtuacoesProfissionais = field(
        default=None,
        metadata={
            "name": "ATUACOES-PROFISSIONAIS",
            "type": "Element",
        },
    )
    areas_de_atuacao: None | AreasDeAtuacao = field(
        default=None,
        metadata={
            "name": "AREAS-DE-ATUACAO",
            "type": "Element",
        },
    )
    idiomas: None | Idiomas = field(
        default=None,
        metadata={
            "name": "IDIOMAS",
            "type": "Element",
        },
    )
    premios_titulos: None | PremiosTitulos = field(
        default=None,
        metadata={
            "name": "PREMIOS-TITULOS",
            "type": "Element",
        },
    )
    licencas: None | Licencas = field(
        default=None,
        metadata={
            "name": "LICENCAS",
            "type": "Element",
        },
    )
    nome_completo: object = field(
        metadata={
            "name": "NOME-COMPLETO",
            "type": "Attribute",
        }
    )
    nome_em_citacoes_bibliograficas: object = field(
        metadata={
            "name": "NOME-EM-CITACOES-BIBLIOGRAFICAS",
            "type": "Attribute",
        }
    )
    nacionalidade: object = field(
        metadata={
            "name": "NACIONALIDADE",
            "type": "Attribute",
        }
    )
    cpf: None | object = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Attribute",
        },
    )
    numero_do_passaporte: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-DO-PASSAPORTE",
            "type": "Attribute",
        },
    )
    pais_de_nascimento: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DE-NASCIMENTO",
            "type": "Attribute",
        },
    )
    uf_nascimento: None | object = field(
        default=None,
        metadata={
            "name": "UF-NASCIMENTO",
            "type": "Attribute",
        },
    )
    cidade_nascimento: None | object = field(
        default=None,
        metadata={
            "name": "CIDADE-NASCIMENTO",
            "type": "Attribute",
        },
    )
    formato_data_de_nascimento: DadosGeraisFormatoDataDeNascimento = field(
        default=DadosGeraisFormatoDataDeNascimento.DDMMAAAA,
        metadata={
            "name": "FORMATO-DATA-DE-NASCIMENTO",
            "type": "Attribute",
        },
    )
    data_nascimento: None | object = field(
        default=None,
        metadata={
            "name": "DATA-NASCIMENTO",
            "type": "Attribute",
        },
    )
    sexo: None | DadosGeraisSexo = field(
        default=None,
        metadata={
            "name": "SEXO",
            "type": "Attribute",
        },
    )
    numero_identidade: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-IDENTIDADE",
            "type": "Attribute",
        },
    )
    orgao_emissor: None | object = field(
        default=None,
        metadata={
            "name": "ORGAO-EMISSOR",
            "type": "Attribute",
        },
    )
    uf_orgao_emissor: None | object = field(
        default=None,
        metadata={
            "name": "UF-ORGAO-EMISSOR",
            "type": "Attribute",
        },
    )
    formato_data_de_emissao: DadosGeraisFormatoDataDeEmissao = field(
        default=DadosGeraisFormatoDataDeEmissao.DDMMAAAA,
        metadata={
            "name": "FORMATO-DATA-DE-EMISSAO",
            "type": "Attribute",
        },
    )
    data_de_emissao: None | object = field(
        default=None,
        metadata={
            "name": "DATA-DE-EMISSAO",
            "type": "Attribute",
        },
    )
    nome_do_pai: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-PAI",
            "type": "Attribute",
        },
    )
    nome_da_mae: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DA-MAE",
            "type": "Attribute",
        },
    )
    permissao_de_divulgacao: DadosGeraisPermissaoDeDivulgacao = field(
        metadata={
            "name": "PERMISSAO-DE-DIVULGACAO",
            "type": "Attribute",
        }
    )
    nome_do_arquivo_de_foto: None | object = field(
        default=None,
        metadata={
            "name": "NOME-DO-ARQUIVO-DE-FOTO",
            "type": "Attribute",
        },
    )
    texto_resumo_cv_rh: None | object = field(
        default=None,
        metadata={
            "name": "TEXTO-RESUMO-CV-RH",
            "type": "Attribute",
        },
    )
    outras_informacoes_relevantes_attribute: None | object = field(
        default=None,
        metadata={
            "name": "OUTRAS-INFORMACOES-RELEVANTES",
            "type": "Attribute",
        },
    )
    data_falecimento: None | object = field(
        default=None,
        metadata={
            "name": "DATA-FALECIMENTO",
            "type": "Attribute",
        },
    )
    sigla_pais_nacionalidade: None | object = field(
        default=None,
        metadata={
            "name": "SIGLA-PAIS-NACIONALIDADE",
            "type": "Attribute",
        },
    )
    pais_de_nacionalidade: None | object = field(
        default=None,
        metadata={
            "name": "PAIS-DE-NACIONALIDADE",
            "type": "Attribute",
        },
    )
    raca_ou_cor: None | object = field(
        default=None,
        metadata={
            "name": "RACA-OU-COR",
            "type": "Attribute",
        },
    )
    orcid_id: None | object = field(
        default=None,
        metadata={
            "name": "ORCID-ID",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CurriculoVitae:
    class Meta:
        name = "CURRICULO-VITAE"

    dados_gerais: DadosGerais = field(
        metadata={
            "name": "DADOS-GERAIS",
            "type": "Element",
        }
    )
    producao_bibliografica: None | ProducaoBibliografica = field(
        default=None,
        metadata={
            "name": "PRODUCAO-BIBLIOGRAFICA",
            "type": "Element",
        },
    )
    producao_tecnica: None | ProducaoTecnica = field(
        default=None,
        metadata={
            "name": "PRODUCAO-TECNICA",
            "type": "Element",
        },
    )
    outra_producao: None | OutraProducao = field(
        default=None,
        metadata={
            "name": "OUTRA-PRODUCAO",
            "type": "Element",
        },
    )
    dados_complementares: None | DadosComplementares = field(
        default=None,
        metadata={
            "name": "DADOS-COMPLEMENTARES",
            "type": "Element",
        },
    )
    sistema_origem_xml: object = field(
        metadata={
            "name": "SISTEMA-ORIGEM-XML",
            "type": "Attribute",
        }
    )
    numero_identificador: None | object = field(
        default=None,
        metadata={
            "name": "NUMERO-IDENTIFICADOR",
            "type": "Attribute",
        },
    )
    formato_data_atualizacao: CurriculoVitaeFormatoDataAtualizacao = field(
        default=CurriculoVitaeFormatoDataAtualizacao.DDMMAAAA,
        metadata={
            "name": "FORMATO-DATA-ATUALIZACAO",
            "type": "Attribute",
        },
    )
    data_atualizacao: None | object = field(
        default=None,
        metadata={
            "name": "DATA-ATUALIZACAO",
            "type": "Attribute",
        },
    )
    formato_hora_atualizacao: CurriculoVitaeFormatoHoraAtualizacao = field(
        default=CurriculoVitaeFormatoHoraAtualizacao.HHMMSS,
        metadata={
            "name": "FORMATO-HORA-ATUALIZACAO",
            "type": "Attribute",
        },
    )
    hora_atualizacao: None | object = field(
        default=None,
        metadata={
            "name": "HORA-ATUALIZACAO",
            "type": "Attribute",
        },
    )
