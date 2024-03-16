# ./Dockerfile 
FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /app

## Install packages
COPY requirements.txt /app/
# RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

## Copy all src files
COPY . /app/

## Run the application on the port 8000
EXPOSE 8000

# CMD ["bash", "python3 manage.py makemigrations"]
# CMD ["bash", "python3 manage.py migrate"]

# gunicorn 배포 명령어
# CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
