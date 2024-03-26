#!/bin/bash

echo "python3 manage.py makemigrations"
python3 manage.py makemigrations
echo "python3 manage.py migrate"
python3 manage.py migrate
echo "gunicorn -b 0.0.0.0:8000 config.wsgi:application"
gunicorn -b 0.0.0.0:8000 config.wsgi:application
