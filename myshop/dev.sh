#!/bin/bash

export DJANGO_SETTINGS_MODULE=myshop.settings_dev

python manage.py migrate
python manage.py loaddata initial.json
python manage.py runserver