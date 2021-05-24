FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install nginx gunicorn redis nano python3-dev postgresql musl-dev gcc wkhtmltopdf -y
RUN mkdir /app && mkdir /var/log/nginx/ && touch bot.letsspeak.com.ua.log && touch bot.letsspeak.com.ua.error.log

WORKDIR /app

COPY requirements.txt /app/
RUN python3 -m pip install pip --upgrade && pip install -r /app/requirements.txt
COPY . /app/

CMD gunicorn main:init     --access-logfile acces-log.log     --workers 2     --bind unix:/tmp/maria_bublyk.sock --worker-class aiohttp.GunicornWebWorker --timeout 120