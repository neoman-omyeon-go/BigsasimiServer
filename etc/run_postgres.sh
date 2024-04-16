#!/bin/bash

NETWORK_NAME="test_net"

if [ ! "$(docker network ls -q -f name=$NETWORK_NAME)" ]; then
    echo "도커 네트워크 생성: $NETWORK_NAME"
    docker network create $NETWORK_NAME
else
    echo "도커 네트워크 '$NETWORK_NAME' 이미 존재합니다."
fi

POSTGRESQL_DIR=$(pwd)/data/postgres13a
echo "PostgreSQL 데이터 디렉토리 경로: $POSTGRESQL_DIR"

docker run -d \
  --name postgres \
  --network test_net \
  -e POSTGRES_DB=mydb \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=1q2w3e4r \
  -p 5432:5432 \
  -v $POSTGRESQL_DIR/data/postgres13a:/var/lib/postgres/data \
  postgres:13-alpine

cd ..

# docker build --tag bigsasimi-django:v0.1 .  
# docker run -d --name django -p 8000:8000 --network test_net bigsasimi-django:v0.1