import asyncio

from loader import bot

from data import config


print(
    # asyncio.run(bot.set_webhook(config.WEBHOOK_URL))
    asyncio.run(bot.get_webhook_info())
)
