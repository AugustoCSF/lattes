"""Teste end-to-end do fluxo upload → configurar → resultado."""
import re
import requests

BASE = "http://127.0.0.1:8000"
s = requests.Session()

# 1. GET upload
r = s.get(f"{BASE}/")
print(f"GET upload: {r.status_code}")

csrf_match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', r.text)
if not csrf_match:
    print("CSRF token NOT FOUND")
    exit(1)
token = csrf_match.group(1)
print("CSRF token OK")

# 2. POST upload com currículo JSON
with open("../curriculos-json/VINICIUS CARVALHO PEREIRA.json", "rb") as f:
    r = s.post(
        f"{BASE}/",
        data={"csrfmiddlewaretoken": token, "perfil": "H"},
        files={"arquivo": ("curriculo.json", f, "application/json")},
        allow_redirects=False,
    )
print(f"POST upload: {r.status_code} -> {r.headers.get('Location', '')}")

# 3. GET configurar
r = s.get(f"{BASE}/configurar/")
print(f"GET configurar: {r.status_code}")
has_peso = "peso_qualis_a1" in r.text
has_limite = "limite_" in r.text
has_tit = "tit_doutorado" in r.text
print(f"  Campos — peso: {has_peso}, limite: {has_limite}, titulação: {has_tit}")

# 4. POST configurar (com os valores padrão)
csrf2 = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', r.text)
if not csrf2:
    print("CSRF token 2 NOT FOUND")
    exit(1)

# Extrai todos os campos input do form
fields = re.findall(r'name="([^"]+)"[^>]*value="([^"]*)"', r.text)
data = {}
for name, val in fields:
    if name not in data:  # primeiro valor prevalece (evita duplicatas)
        data[name] = val
data["csrfmiddlewaretoken"] = csrf2.group(1)

r = s.post(f"{BASE}/configurar/", data=data, allow_redirects=False)
print(f"POST configurar: {r.status_code} -> {r.headers.get('Location', '')}")

# 5. GET resultado
r = s.get(f"{BASE}/resultado/")
print(f"GET resultado: {r.status_code}")
if r.status_code == 200:
    has_nome = "VINICIUS" in r.text.upper()
    has_pts = "Pontuação Total" in r.text or "Pontua" in r.text
    has_dl = "download" in r.text.lower()
    print(f"  Nome: {has_nome}, Pontuação: {has_pts}, Download: {has_dl}")

    # Extrair a pontuação total do HTML
    pts_match = re.search(
        r'Pontuação Total.*?<div[^>]*class="value"[^>]*>(\d+)', r.text, re.DOTALL
    )
    if not pts_match:
        pts_match = re.search(
            r'class="value"[^>]*style="[^"]*color: var\(--success\)[^"]*">[\s]*(\d+)',
            r.text, re.DOTALL,
        )
    if pts_match:
        print(f"  PONTUAÇÃO TOTAL: {pts_match.group(1)}")
    else:
        print("  (pontuação não extraída por regex)")
else:
    print(f"  Body (500 chars): {r.text[:500]}")

# 6. GET download
r = s.get(f"{BASE}/download/")
print(f"GET download: {r.status_code}")
if r.status_code == 200:
    cd = r.headers.get("Content-Disposition", "")
    print(f"  Content-Disposition: {cd}")
    print(f"  Tamanho HTML: {len(r.text)} chars")

print("\n✅ Teste completo!")
