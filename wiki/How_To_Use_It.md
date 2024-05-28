# 원클릭 배포 및 실행 방법

**도커 컴포즈 활용**

nginx + postgres + django(gunicorn) 패키징

```shell

git clone https://github.com/neoman-omyeon-go/BigsasimiServer.git

docker compose up -d

```

<hr>

**일반 도커 활용**

postgres, django 따로 업로드

`.\config\settings`의 `local.py` 또는 `prod.py`의 DATABASES 프로퍼티를 적당히 선택

(`DATABASES_SELECT` 항목 참조 요망)

<hr>

**로컬 활용**

django 로컬 테스트

etc의 run_postgres.sh 실행 후 runserver

(`DATABASES_SELECT` 항목 참조 요망)

<hr>

- 정적파일 테스트

  `http://localhost:8080/static/test.png`

- Response 테스트

  GET `http://localhost:8080/test/` or `http://localhost:8080/test/?json=true`
