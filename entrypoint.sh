#!/bin/bash

# Wait for PostgreSQL to be ready
sleep 7
echo "DB is ready?????" 


echo "python3 manage.py makemigrations" && 
python manage.py makemigrations &&
echo "python3 manage.py migrate" && 
python manage.py migrate --no-input &&
echo "gunicorn -b 0.0.0.0:8000 config.wsgi:application" &&
gunicorn -b 0.0.0.0:8000 config.wsgi:application
