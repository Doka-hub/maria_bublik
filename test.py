import asyncio

from loader import bot

from data import config


# asyncio.run(bot.delete_webhook())
# asyncio.run(bot.set_webhook(config.WEBHOOK_URL))
print(
    asyncio.run(bot.get_webhook_info())
)
