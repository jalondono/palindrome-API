#!/bin/sh
python manage.py makemigrations --settings=grupo_d.settings.dev_sqlite
python manage.py migrate --settings=grupo_d.settings.dev_sqlite
python manage.py runserver 0.0.0.0:8000 --settings=grupo_d.settings.dev_sqlite