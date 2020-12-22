from aiogram import types

from filters.is_admin import AdminFilter


def set_commands(func):
    async def wrapper(message: types.Message):
        await message.bot.set_my_commands([types.BotCommand('start', 'Начать')])
        if await AdminFilter(True).check(message):
            await message.bot.set_my_commands(
                [
                    types.BotCommand('start', 'Начать'),
                    types.BotCommand('add', 'Добавить в whitelist'),
                    types.BotCommand('remove', 'Удалить из whitelist')
                ]
            )
        return await func(message)
    return wrapper

