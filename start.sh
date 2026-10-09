#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
fi
.venv/bin/python -m pip install --disable-pip-version-check -q -r requirements.txt
.venv/bin/python manage.py migrate --noinput
.venv/bin/python manage.py load_demo_data
exec .venv/bin/python manage.py runserver 0.0.0.0:${PORT:-5000}
