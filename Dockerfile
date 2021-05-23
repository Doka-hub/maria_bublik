FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install redis nano python3-dev postgresql-dev musl-dev gcc wkhtmltopdf -y
RUN mkdir /maria_bublyk_bot

WORKDIR /maria_bublyk_bot

COPY requirements.txt /maria_bublyk_bot/
RUN python -m pip install pip --upgrade && pip install -r /maria_bublyk_bot/requirements.txt
COPY . /maria_bublyk_bot/

CMD python3 /maria_bublyk_bot/main.py