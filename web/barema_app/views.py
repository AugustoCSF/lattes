"""
views.py — Views do wizard de cálculo do barema.

Fluxo em 3 passos:
    1. upload_view     — upload do currículo (XML/JSON) + seleção do perfil
    2. configurar_view — customização dos pesos, limites e parâmetros gerais
    3. resultado_view  — cálculo e exibição do resultado

Dados transitam via request.session (file-based, sem banco de dados).
"""
from __future__ import annotations

import json

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .utils import (
    ITENS_G1,
    ITENS_G2,
    ROTULOS,
    calcular_barema_em_memoria,
    carregar_config_padrao,
    converter_xml_para_json,
)


# ---------------------------------------------------------------------------
# Passo 1 — Upload
# ---------------------------------------------------------------------------

def upload_view(request):
    """Upload do currículo Lattes + seleção do perfil base."""
    config = carregar_config_padrao()
    perfis = [
        (cod, info.get("nome", cod))
        for cod, info in config.get("perfis", {}).items()
    ]

    if request.method == "POST":
        arquivo = request.FILES.get("arquivo")
        perfil = request.POST.get("perfil", "H")

        if not arquivo:
            return render(request, "barema_app/upload.html", {
                "perfis": perfis,
                "erro": "Por favor, selecione um arquivo.",
            })

        content = arquivo.read()
        filename = arquivo.name.lower()

        try:
            if filename.endswith(".xml"):
                json_data = converter_xml_para_json(content)
            elif filename.endswith(".json"):
                json_data = json.loads(content)
            else:
                raise ValueError("Formato não suportado. Use .xml ou .json.")
        except Exception as exc:
            return render(request, "barema_app/upload.html", {
                "perfis": perfis,
                "erro": f"Erro ao processar arquivo: {exc}",
            })

        # Armazena na sessão para os próximos passos
        request.session["curriculo_json"] = json_data
        request.session["perfil"] = perfil
        request.session["arquivo_nome"] = arquivo.name

        return redirect("configurar")

    return render(request, "barema_app/upload.html", {"perfis": perfis})


# ---------------------------------------------------------------------------
# Passo 2 — Configuração do Barema
# ---------------------------------------------------------------------------

def configurar_view(request):
    """Formulário de customização dos parâmetros do barema."""
    if "curriculo_json" not in request.session:
        return redirect("upload")

    config = carregar_config_padrao()
    perfil = request.session.get("perfil", "H")

    if request.method == "POST":
        # Reconstrói o config dict a partir dos campos do formulário
        custom_config = {
            "geral": {
                "ano_fim": int(request.POST.get("ano_fim", 2026)),
                "janela": int(request.POST.get("janela", 5)),
            },
            "titulacao": {
                "doutorado": int(request.POST.get("tit_doutorado", 50)),
                "mestrado": int(request.POST.get("tit_mestrado", 30)),
                "bolsista_pq": int(request.POST.get("tit_bolsista_pq", 20)),
            },
            "limites": {},
            "perfis": {
                perfil: {
                    "nome": request.POST.get(
                        "perfil_nome",
                        config.get("perfis", {}).get(perfil, {}).get("nome", perfil),
                    ),
                    "pesos": {},
                },
            },
        }

        # Coleta pesos de todos os itens
        for item in ITENS_G1 + ITENS_G2:
            val = request.POST.get(f"peso_{item}")
            if val is not None and val != "":
                custom_config["perfis"][perfil]["pesos"][item] = int(val)

        # Coleta limites (só inclui se > 0)
        for item in ITENS_G1 + ITENS_G2:
            val = request.POST.get(f"limite_{item}")
            if val is not None and val != "":
                v = int(val)
                if v > 0:
                    custom_config["limites"][item] = v

        request.session["config"] = custom_config
        return redirect("resultado")

    # --- GET: prepara dados do formulário pré-preenchido ---
    perfil_data = config.get("perfis", {}).get(perfil, {})
    pesos = perfil_data.get("pesos", {})
    limites = config.get("limites", {})

    context = {
        "perfil": perfil,
        "perfil_nome": perfil_data.get("nome", perfil),
        "arquivo_nome": request.session.get("arquivo_nome", ""),
        "geral": config.get("geral", {"ano_fim": 2026, "janela": 5}),
        "titulacao": config.get("titulacao", {
            "doutorado": 50, "mestrado": 30, "bolsista_pq": 20,
        }),
        "pesos_g1": [
            (item, ROTULOS.get(item, item), pesos.get(item, 0))
            for item in ITENS_G1
        ],
        "pesos_g2": [
            (item, ROTULOS.get(item, item), pesos.get(item, 0))
            for item in ITENS_G2
        ],
        "limites_items": [
            (item, ROTULOS.get(item, item), limites.get(item, 0))
            for item in ITENS_G1 + ITENS_G2
        ],
    }

    return render(request, "barema_app/configurar.html", context)


# ---------------------------------------------------------------------------
# Passo 3 — Resultado
# ---------------------------------------------------------------------------

def resultado_view(request):
    """Cálculo do barema e exibição do resultado."""
    if "curriculo_json" not in request.session or "config" not in request.session:
        return redirect("upload")

    json_data = request.session["curriculo_json"]
    config_dict = request.session["config"]
    perfil = request.session.get("perfil", "H")

    try:
        pesquisador, html_resultado = calcular_barema_em_memoria(
            json_data, perfil, config_dict,
        )
    except Exception as exc:
        return render(request, "barema_app/resultado.html", {
            "erro": f"Erro no cálculo: {exc}",
        })

    # Guarda o HTML para download posterior
    request.session["html_resultado"] = html_resultado

    context = {
        "nome": pesquisador.nome,
        "perfil": perfil,
        "perfil_nome": config_dict.get("perfis", {}).get(perfil, {}).get("nome", perfil),
        "pontuacao_total": pesquisador.pontuacao_total(),
        "pontuacao_por_ano": list(
            zip(pesquisador.anos, pesquisador.pontuacao_por_ano())
        ),
        "titulacao": (
            "Doutorado" if pesquisador.doutorado
            else ("Mestrado" if pesquisador.mestrado else "Graduação")
        ),
        "bolsista_pq": pesquisador.bolsistaPQ,
        "html_resultado": html_resultado,
    }

    return render(request, "barema_app/resultado.html", context)


# ---------------------------------------------------------------------------
# Download do HTML
# ---------------------------------------------------------------------------

def download_view(request):
    """Retorna o HTML do resultado como arquivo para download."""
    html = request.session.get("html_resultado", "")
    if not html:
        return redirect("resultado")

    nome = request.session.get("arquivo_nome", "resultado").rsplit(".", 1)[0]
    response = HttpResponse(html, content_type="text/html; charset=utf-8")
    response["Content-Disposition"] = f'attachment; filename="{nome}-barema.html"'
    return response
