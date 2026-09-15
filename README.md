# lattes — Avaliação de Currículos Lattes (PROPESQ/UFMT)

Lê currículos no formato XML ou JSON da **Plataforma Lattes (CNPq)**,
classifica as produções com base no **Qualis CAPES** e **JCR 2024**,
e calcula a pontuação do **barema** da PROPESQ — gerando relatórios HTML individuais.

---

## Estrutura do projeto

```
lattes/
│
├── README.md                      ← este arquivo
│
├── config/                        ← parâmetros do barema (edite aqui)
│   ├── barema.toml                ← configuração principal
│   └── barema_teste.toml          ← exemplo de config alternativa
│
├── curriculos/                    ← currículos de entrada (XML)
│   └── humanas/
│       └── *.xml
│
├── curriculos-json/               ← JSONs convertidos dos XMLs (saída do conversor)
│   └── *.json
│
├── definitions/                   ← schema Lattes + conversor XML→JSON
│   ├── *.xsd                      ← schema XSD oficial do Lattes (2022)
│   └── curriculo_lattes/
│       ├── curriculo_model.py     ← modelo de dados gerado pelo xsdata
│       └── processaCurriculoXML.py ← converte XML→JSON (salva em curriculos-json/)
│
├── saida/                         ← relatórios HTML e CSVs gerados (não versionar)
│   └── *.html / *.csv
│
├── baremas.py                     ← motor original (pesos fixos no código)
├── baremas_config.py              ← motor configurável via config/barema.toml
├── calcular_barema.py             ← CLI principal  ← USE ESTE
├── json_barema.py                 ← CLI original (JSON → baremas.py)
├── lerCurriculoXML.py             ← CLI original (XMLs em lote)
├── JCR2024.py                     ← base de dados JCR 2024 (~3.6 MB)
└── relatorioQualis.py             ← base de dados Qualis CAPES (~9.5 MB)
```

---

## Como usar — fluxo novo (configurável)

### 0. Converter XMLs Lattes para JSON (pré-requisito)

Se você tem um `.xml` exportado do Lattes, converta-o primeiro:

```powershell
# Converter um XML
python definitions\curriculo_lattes\processaCurriculoXML.py curriculos\humanas\NOME.xml
# → salva em curriculos-json\NOME.json automaticamente

# Converter um ZIP com vários XMLs de uma vez
python definitions\curriculo_lattes\processaCurriculoXML.py curriculos\humanas\curriculos.zip
# → salva todos os JSONs em curriculos-json\
```

### 1. Ver os perfis disponíveis

```powershell
python calcular_barema.py --lista-perfis
```

### 2. Calcular o barema de um currículo JSON

```powershell
python calcular_barema.py <curriculo.json> <saida.html> <perfil>
```

**Exemplo:**
```powershell
python calcular_barema.py "curriculos-json\VINICIUS CARVALHO PEREIRA.json" saida\resultado.html H
```

Perfis disponíveis por padrão: `A` (Letras), `E` (Exatas), `H` (Humanas).

### 3. Usar um config alternativo

Copie `config\barema.toml`, edite os pesos e passe com `--config`:

```powershell
python calcular_barema.py curriculo.json saida.html H --config config\barema_teste.toml
```

### 4. Definir os anos manualmente

```powershell
python calcular_barema.py curriculo.json saida.html H --anos 2022 2023 2024
```

---

## O que configurar em `config/barema.toml`

| Seção | O que controla |
|---|---|
| `[geral]` | `ano_fim` e `janela` — quais anos entram na avaliação |
| `[titulacao]` | Pontos por doutorado, mestrado e bolsista PQ |
| `[limites]` | Teto máximo de pontuação por item (ex: máx. 5 pts em TCC) |
| `[perfis.X.pesos]` | Peso (pts/unidade) de cada tipo de produção para o perfil X |

Para criar um novo perfil, basta copiar um bloco `[perfis.X]` dentro do `.toml`.

---

## Como usar — fluxo original (XMLs em lote)

```powershell
python lerCurriculoXML.py
```

Lê todos os `.xml` de `curriculos/` e gera CSVs e HTMLs por pasta/área.

```powershell
# Fluxo original com JSON (motor antigo, pesos fixos)
python json_barema.py "definitions\curriculo_lattes\NOME.json" saida.html H
```

---

## Dependências

- Python 3.11+ (usa `tomllib` da biblioteca padrão)
- Sem pacotes externos para o fluxo principal

Para converter XMLs Lattes para JSON (opcional):
```powershell
pip install xsdata
```
