import asyncio

from celery import Celery

from data import config

from .mail import mail


app = Celery('app', broker=config.REDIS['host'])
app.conf.timezone = config.TIMEZONE


# mail
@app.task(name='mail')
def task_mail(data: dict):
    if data.get('mail_data'):
        mail_data = data['mail_data']
        loop = asyncio.get_event_loop()
        loop.run_until_complete(mail(mail_data))
