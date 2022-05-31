# syntax=docker/dockerfile:1
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/orders_system

RUN pip install --upgrade pip

COPY creds.json .
COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["sh", "/usr/src/orders_system/entrypoint.sh"]