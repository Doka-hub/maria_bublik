from aiogram import types

from filters.is_admin import AdminFilter


def set_commands(func):
    async def wrapper(message: types.Message):
        commands = [types.BotCommand('start', 'Начать')]
        if await AdminFilter(True).check(message):
            commands.extend(
                [
                    types.BotCommand('add', 'Добавить в whitelist'),
                    types.BotCommand('remove', 'Удалить из whitelist')
                ]
            )
        await message.bot.set_my_commands(commands)
        return await func(message)
    return wrapper

