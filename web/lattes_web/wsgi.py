"""WSGI config for lattes_web project."""
import os
import sys
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lattes_web.settings")

# Garante que os módulos do projeto raiz são importáveis
root_dir = Path(__file__).resolve().parent.parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))
defs_dir = root_dir / "definitions" / "curriculo_lattes"
if str(defs_dir) not in sys.path:
    sys.path.insert(0, str(defs_dir))

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
