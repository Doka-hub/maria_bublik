from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.keyboards.inline import get_inline_keyboard

from loader import _


def get_menu_inline_keyboard() -> InlineKeyboardMarkup:
    menu_inline_keyboard = get_inline_keyboard([
        [InlineKeyboardButton(_('Скачать БД пользователей'), callback_data='download_bd_users')],
        [InlineKeyboardButton(_('Рассылка'), callback_data='mail')],
    ])
    return menu_inline_keyboard
