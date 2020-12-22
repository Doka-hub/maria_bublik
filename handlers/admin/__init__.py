from aiogram import Dispatcher

from .whitelist import add_to_whitelist, remove_from_whitelist


def setup(dp: Dispatcher):
    dp.register_message_handler(add_to_whitelist, commands='add', is_admin=True)
    dp.register_message_handler(remove_from_whitelist, commands='remove', is_admin=True)
