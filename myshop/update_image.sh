#!/bin/bash

export DJANGO_SETTINGS_MODULE=myshop.settings_dev

python manage.py migrate_product_images