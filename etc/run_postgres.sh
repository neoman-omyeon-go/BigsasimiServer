#!/bin/bash

POSTGRESQL_DIR=$(pwd)/data/postgres13a
echo "PostgreSQL 데이터 디렉토리 경로: $POSTGRESQL_DIR"

docker run -d \
  --name dbserver \
  -e POSTGRES_DB=mydb \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=1q2w3e4r \
  -p 5432:5432 \
  -v $POSTGRESQL_DIR/data/postgres13a:/var/lib/postgres/data \
  postgres:13-alpine
