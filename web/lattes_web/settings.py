"""
Django settings for lattes_web — interface do Barema PROPESQ.

Configurado para uso LOCAL sem banco de dados.
Sessões são armazenadas em arquivos temporários.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent   # web/
ROOT_DIR = BASE_DIR.parent                           # lattes/

SECRET_KEY = "django-insecure-propesq-local-dev-key-troque-em-producao"

DEBUG = True

ALLOWED_HOSTS = ["*"]

# --- Apps -------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "barema_app",
]

# --- Middleware -------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

# --- URLs / WSGI ------------------------------------------------------------
ROOT_URLCONF = "lattes_web.urls"
WSGI_APPLICATION = "lattes_web.wsgi.application"

# --- Templates --------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

# --- Database: nenhuma (sem modelos) ----------------------------------------
DATABASES = {}

# --- Sessões em arquivo (sem DB) --------------------------------------------
SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_FILE_PATH = BASE_DIR / "session_data"
os.makedirs(SESSION_FILE_PATH, exist_ok=True)

SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"

# --- Static files -----------------------------------------------------------
STATIC_URL = "/static/"

# --- Upload: aceita currículos de até 10 MB ---------------------------------
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024

# --- Localização ------------------------------------------------------------
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Cuiaba"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
