FROM python:3.9-bullseye

LABEL team="cloud-computing-team"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /etc/petdoc_backend_service

COPY linux.requirements.txt /etc/petdoc_backend_service/
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /etc/petdoc_backend_service/

EXPOSE 80
CMD [ "/bin/bash", "-c", "alembic upgrade head && uvicorn --host 0.0.0.0 --port 80 --workers 10 main:REST" ]
