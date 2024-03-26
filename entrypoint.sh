#!/bin/bash

echo "a"
python3 manage.py makemigrations
echo "b"
python3 manage.py migrate
echo "c"
gunicorn -b 0.0.0.0:8000 config.wsgi:application
