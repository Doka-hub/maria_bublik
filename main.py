from typing import List

import aiojobs as aiojobs

from aiogram import Bot

from aiohttp import web

from loguru import logger

from data import config

from loader import bot, dp


# noinspection PyUnusedLocal
async def on_startup(app: web.Application):
    import middlewares
    import filters
    import handlers
    import models
    models.setup()
    middlewares.setup(dp)
    filters.setup(dp)
    handlers.errors.setup(dp)
    handlers.admin.setup(dp)
    handlers.user.setup(dp)
    # if config.BOT_PLACE == 'server':
    #     logger.info('Configure Webhook URL to: {url}', url=config.WEBHOOK_URL)
    #     print(config.WEBHOOK_URL)
    #     await dp.bot.delete_webhook()
    #     await dp.bot.set_webhook(config.WEBHOOK_URL)
    # elif config.BOT_PLACE == 'locale':
    #     await dp.start_polling()


async def on_shutdown(app: web.Application):
    app_bot: Bot = app['bot']
    await app_bot.close()


async def init() -> web.Application:
    from utils.misc import logging
    import web_handlers
    logging.setup()
    scheduler = await aiojobs.create_scheduler()
    app = web.Application()
    subapps: List[str, web.Application] = [
        ('/health/', web_handlers.health_app),
        ('/tg/webhooks/', web_handlers.tg_updates_app),
    ]
    for prefix, subapp in subapps:
        subapp['bot'] = bot
        subapp['dp'] = dp
        subapp['scheduler'] = scheduler
        app.add_subapp(prefix, subapp)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app


if __name__ == '__main__':
    web.run_app(init())
