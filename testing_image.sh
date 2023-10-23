#!/bin/bash
echo "[-  Build Container  -]"
docker build --tag ml_service:1.0 \
        --file deployment/development.dockerfile .

echo "[-  Tagging ml_service Container  -]"
docker tag ml_service:1.0 \
        gcr.io/petdoc-capstone-project/ml_service:1.0-ip

echo "[-  Push Container to Registry  -]"
docker push \
        gcr.io/petdoc-capstone-project/ml_service:1.0-ip

echo "[-  Create Postgres Container  -]"
docker container create \
        --name pgserver \
        -p 5432:5432 \
        -e POSTGRES_USER=postgres \
        -e POSTGRES_PASSWORD=admin \
        -e POSTGRES_DB=coba_capstone \
        postgres:11

echo "[-  Create ml_service Container  -]"
docker container create --name ml_service \
        -p 80:80 \
        -e VERSION=v1 \
        -e JWT_ACCESS_TOKEN_SECRET=AHBiadbiaeud92uedb9ub9wue92 \
        -e JWT_REFRESH_TOKEN_SECRET=eu92uidbsAHBiadbiauedb9ub9wue92eu \
        -e JWT_ALGORITHM=HS512 \
        -e JWT_ACCESS_TOKEN_EXPIRE=1 \
        -e JWT_REFRESH_TOKEN_EXPIRE=7 \
        -e POSTGRES_HOST=172.17.0.1 \
        -e POSTGRES_PORT=5432 \
        -e POSTGRES_USER=postgres \
        -e POSTGRES_PASS=admin \
        -e POSTGRES_DB=coba_capstone \
        ml_service:1.0

echo "[-  Start Container  -]"
docker container start pgserver
echo "[-  WAIT... (5 seconds)  -]"
sleep 5
docker container start ml_service

echo "[-  WAIT... (5 seconds)  -]"
sleep 5
docker logs ml_service
docker container ls

echo "[-  Installing Ngrok  -]"
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
        sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
        echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
        sudo tee /etc/apt/sources.list.d/ngrok.list && \
        sudo apt update && sudo apt install -y ngrok