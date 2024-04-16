#!/bin/bash

# TARGET=/home/ubuntu/BigsasimiServer/
COMPOSE_NAME=rlawlgh001028/bigsasimi-django:latest
COMPOSE_PATH=C/Users/rlawl/Desktop/Capstone/BigsasimiServer

echo TARGET = $COMPOSE_PATH

echo docker pull
docker pull rlawlgh001028/bigsasimi-django:latest

echo docker compose stop
docker compose stop

echo docker rm was
docker rm was

echo docker compose up
# docker compose -f $COMPOSE_PATH/docker-compose.yml up --build -d
docker compose up -d