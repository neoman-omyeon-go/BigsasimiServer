## psql 접속
```
psql -U myuser -d mydb -W
1q2w3e4r
\l & \c mydb
\d
```

## docker local test 방법
docker network create test_net       
docker build --tag [username]/bigsasimi-django:v0.1 .  
docker run --name django -p 8000:8000 -d rlawlgh001028/bigsasimi-django:v0.1