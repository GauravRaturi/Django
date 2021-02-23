#!/usr/bin/env bash
pip install -r requirement.txt
cd web_django
python manage.py migrate
python manage.py collectstatic --no-input
