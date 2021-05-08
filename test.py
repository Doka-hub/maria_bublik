import asyncio
from loader import bot


print(
    asyncio.run(bot.get_webhook_info())
)
