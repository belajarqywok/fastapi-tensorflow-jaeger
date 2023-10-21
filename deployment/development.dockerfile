FROM python:3.9

LABEL team="cloud-computing-team"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /etc/bangkit_capstone

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN cat << EOF >> entrypoint.sh \
    #!/bin/bash \
    alembic upgrade head \
    uvicorn --host 0.0.0.0 --port 3000 --workers 10 main:REST \
EOF

RUN chmod r+x entrypoint.sh
COPY . .

EXPOSE 3000
CMD [ "/bin/bash", "-c", "./entrypoint.sh" ]
