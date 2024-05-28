echo compose stop
docker compose stop

echo delete was
docker rm -f was

echo pull container
docker pull rlawlgh001028/bigsasimi-django:latest

echo docker compose up -d
docker compose up -d
