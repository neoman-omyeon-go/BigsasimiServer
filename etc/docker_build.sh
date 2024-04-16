#!/bin/bash

cd ..

docker build --tag rlawlgh001028/bigsasimi-django:latest .

docker push rlawlgh001028/bigsasimi-django:latest
