#!/bin/bash
apt update
python3 -m pip install --upgrade pip
pip3 install -r linux.requirements.txt
alembic upgrade head
uvicorn --host 0.0.0.0 --port 80 --workers 10 main:REST