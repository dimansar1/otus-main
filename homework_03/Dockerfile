
FROM python:3.9-buster

WORKDIR /app

RUN pip install --upgrade pip setuptools "poetry==1.5.1"
RUN poetry config virtualenvs.create false
RUN pip install fastapi
RUN pip install uvicorn[standart]

COPY requirements.txt ./
RUN pip install install --only main,view

COPY . . 

CMD uvicorn view:app --host 0.0.0.0 --port 8000
