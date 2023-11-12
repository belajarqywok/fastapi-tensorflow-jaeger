run:
	uvicorn --host 0.0.0.0 --port 3000 --reload --workers 10 main:REST

alembic_init:
	python -m alembic init alembic

migrate:
	alembic revision --autogenerate -m "migrate"
	alembic upgrade head

postgres:
	psql --host=localhost --port=5432 --username=postgres --password

jaeger-test:
	uvicorn --host 0.0.0.0 --port 3000 --reload --workers 10 jaeger_test:app

load_test:
	locust --headless --run-time 10s --users 100 --spawn-rate 10 -H http://192.168.137.1:3000 --locustfile locust/configuration.py
	