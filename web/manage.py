#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lattes_web.settings")

    # Adiciona a raiz do projeto (lattes/) ao sys.path para que os módulos
    # existentes (baremas_config, json_barema, etc.) sejam importáveis.
    root_dir = Path(__file__).resolve().parent.parent
    if str(root_dir) not in sys.path:
        sys.path.insert(0, str(root_dir))

    # Também adiciona o diretório do modelo xsdata do currículo
    defs_dir = root_dir / "definitions" / "curriculo_lattes"
    if str(defs_dir) not in sys.path:
        sys.path.insert(0, str(defs_dir))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django não encontrado. Instale com: pip install django"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
