from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.keyboards.inline import get_inline_keyboard


def get_language_inline_keyboard() -> InlineKeyboardMarkup:
    language_inline_keyboard = get_inline_keyboard(
        [
            [InlineKeyboardButton('๐ท๐บ ััััะบะธะน', callback_data='choose_language ru')],
            [InlineKeyboardButton('๐บ๐ธ english', callback_data='choose_language en')],
        ]
    )
    return language_inline_keyboard
