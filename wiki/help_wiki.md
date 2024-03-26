## psql 접속
```
psql -U myuser -d mydb -W
1q2w3e4r
\l & \c mydb
\d
```

## docker local test 방법
cd etc & sh run run_postgres
docker network create test_net       
docker build --tag bigsasimi-django:v0.1 .  
docker run -d --name django -p 8000:8000 --network test_net bigsasimi-django:v0.1
