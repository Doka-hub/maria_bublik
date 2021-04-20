from typing import List, Dict, Optional

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.keyboards.inline import get_inline_keyboard


def get_mail_message_buttons_inline_keyboard(buttons: List[str]) -> Optional[InlineKeyboardMarkup]:
    """
    Получаем клавиатуру для рассылки
    :param buttons:
    :return:
    """
    if not buttons:
        return

    mail_message_buttons_inline_keyboard = [[InlineKeyboardButton(button.split(' - ')[0], url=button.split(' - ')[1])]
                                            for button in buttons if isinstance(button, str)]
    return get_inline_keyboard(mail_message_buttons_inline_keyboard)
