from typing import Optional

import asyncio

from celery import Celery

from data import config


app = Celery('app', broker=config.REDIS['host'])
app.conf.timezone = config.TIMEZONE


# example
# @app.task(name='mail')
# def task_mail(group_id: int, text: str, image_id: Optional[str] = None):
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete("""some_task""")
