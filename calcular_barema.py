"""
calcular_barema.py — CLI para calcular o barema de um currículo Lattes (JSON).

Uso
---
    python calcular_barema.py <curriculo.json> <saida.html> <perfil> [--config barema.toml]

Argumentos posicionais
    curriculo.json  Currículo exportado do Lattes e convertido para JSON via xsdata
    saida.html      Arquivo HTML de saída com o relatório do barema
    perfil          Perfil de avaliação definido no config (ex: A, E ou H)

Opções
    --config PATH   Caminho para o arquivo barema.toml (padrão: config/barema.toml)
    --anos  A B ... Lista de anos a avaliar (sobrescreve o valor do config)
    --lista-perfis  Mostra os perfis disponíveis no config e sai

Exemplos
    python calcular_barema.py curriculo.json relatorio.html H
    python calcular_barema.py curriculo.json relatorio.html E --config meu_barema.toml
    python calcular_barema.py --lista-perfis
    python calcular_barema.py curriculo.json relatorio.html H --anos 2022 2023 2024
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Reutiliza as funções de parsing JSON do json_barema.py já existente
# (records, section, value, normalize_issn, classify_article, populate_researcher)
import json_barema as _jb

import baremas_config as bc


# ---------------------------------------------------------------------------
# Parsing de argumentos
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="calcular_barema",
        description="Calcula o barema de um currículo Lattes (JSON) usando barema.toml.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument(
        "curriculo",
        nargs="?",
        help="Caminho para o arquivo JSON do currículo Lattes",
    )
    p.add_argument(
        "saida",
        nargs="?",
        help="Caminho para o arquivo HTML de saída",
    )
    p.add_argument(
        "perfil",
        nargs="?",
        help="Código do perfil de avaliação (ex: A, E, H)",
    )
    p.add_argument(
        "--config",
        metavar="PATH",
        default=None,
        help="Caminho para barema.toml (padrão: barema.toml ao lado deste script)",
    )
    p.add_argument(
        "--anos",
        nargs="+",
        metavar="ANO",
        default=None,
        help="Anos a avaliar, sobrescreve a janela do config (ex: --anos 2022 2023 2024)",
    )
    p.add_argument(
        "--lista-perfis",
        action="store_true",
        help="Lista os perfis disponíveis no config e sai",
    )
    return p


# ---------------------------------------------------------------------------
# Função principal de cálculo
# ---------------------------------------------------------------------------

def calcular(
    curriculo_path: str | Path,
    saida_path: str | Path,
    perfil: str,
    config_path: str | Path | None = None,
    anos: list[str] | None = None,
) -> bc.PesquisadorConfig:
    """
    Lê o JSON do currículo, calcula o barema e escreve o HTML de saída.

    Retorna o objeto PesquisadorConfig com todos os dados preenchidos.
    """
    # 1. Carrega o config (barema.toml)
    if config_path is not None:
        bc.recarregar_config(config_path)

    # 2. Define a janela de anos
    if anos is None:
        anos = bc.anos_validos_do_config()

    # 3. Valida o perfil
    disponiveis = bc.perfis_disponiveis()
    if perfil not in disponiveis:
        raise ValueError(
            f"Perfil '{perfil}' não encontrado no config. "
            f"Disponíveis: {disponiveis}"
        )

    # 4. Cria o pesquisador com o motor de configuração
    pesquisador = bc.criar_pesquisador(perfil, anos)

    # 5. Lê o JSON e preenche o pesquisador
    #    Reutiliza populate_researcher de json_barema.py — ele só chama
    #    métodos add*() e atribui pesquisador.nome/doutorado/mestrado,
    #    que existem igualmente no PesquisadorConfig.
    data = _jb.load_json(curriculo_path)
    _jb.populate_researcher(data, pesquisador, anos)

    # 6. Gera o HTML usando o geraHTML do baremas_config
    saida_path = Path(saida_path)
    saida_path.parent.mkdir(parents=True, exist_ok=True)
    with open(saida_path, "w", encoding="utf-8") as f:
        f.writelines(linha + "\n" for linha in bc.geraHTML(pesquisador))

    return pesquisador


# ---------------------------------------------------------------------------
# Ponto de entrada CLI
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    # --lista-perfis: só mostra os perfis e sai
    if args.lista_perfis:
        if args.config:
            bc.recarregar_config(args.config)
        perfis = bc.perfis_disponiveis()
        anos = bc.anos_validos_do_config()
        print(f"Config: {bc._CONFIG_PATH}")
        print(f"Anos avaliados: {', '.join(anos)}\n")
        print("Perfis disponíveis:")
        for cod in perfis:
            print(f"  {cod}  —  {bc.nome_perfil(cod)}")
        return 0

    # Valida argumentos obrigatórios
    if not args.curriculo or not args.saida or not args.perfil:
        parser.print_help()
        print("\nErro: curriculo, saida e perfil são obrigatórios.", file=sys.stderr)
        return 2

    try:
        pesquisador = calcular(
            curriculo_path=args.curriculo,
            saida_path=args.saida,
            perfil=args.perfil,
            config_path=args.config,
            anos=args.anos,
        )
    except FileNotFoundError as e:
        print(f"Erro: arquivo não encontrado — {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Erro de configuração — {e}", file=sys.stderr)
        return 1

    # Resumo no terminal
    print(f"Pesquisador : {pesquisador.nome}")
    print(f"Perfil      : {pesquisador.perfil} — {bc.nome_perfil(pesquisador.perfil)}")
    titulacao = "Doutorado" if pesquisador.doutorado else "Mestrado" if pesquisador.mestrado else "Graduacao"
    print(f"Titulacao   : {titulacao}")
    print(f"Bolsista PQ : {'Sim' if pesquisador.bolsistaPQ else 'Nao'}")
    print(f"Anos        : {', '.join(pesquisador.anos)}")
    print()
    print("Pontuacao por ano:")
    for ano, pts in zip(pesquisador.anos, pesquisador.pontuacao_por_ano()):
        print(f"  {ano}: {pts} pts")
    print(f"\nTotal       : {pesquisador.pontuacao_total()} pts")
    print(f"HTML salvo  : {Path(args.saida).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

