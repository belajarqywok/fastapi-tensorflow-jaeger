run:
	uvicorn --host 0.0.0.0 --port 3000 --reload --workers 10 main:REST

migrate:
	alembic revision --autogenerate -m "migrate"
	alembic upgrade head

postgres:
	psql --host=localhost --port=5432 --username=postgres --password

jaeger-test:
	uvicorn --host 0.0.0.0 --port 3000 --reload --workers 10 jaeger_test:app