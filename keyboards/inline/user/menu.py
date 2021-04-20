from typing import Optional

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from filters.is_admin import AdminFilter

from utils.keyboards.inline import get_inline_keyboard

from loader import _


def get_menu_inline_keyboard(locale: Optional[str] = None, user_id: Optional[int] = None) -> InlineKeyboardMarkup:
    menu_inline_keyboard = get_inline_keyboard([
            [
                InlineKeyboardButton(_('Админ панель', locale=locale), callback_data='admin')
            ] if AdminFilter().check_by_user_id(user_id) else [],
            [InlineKeyboardButton(_('Группы', locale=locale), callback_data='group_list')],
            [InlineKeyboardButton(_('Разослать', locale=locale), callback_data='group_list_to_mail')],
            [InlineKeyboardButton(_('Сменить язык', locale=locale), callback_data='change_language')],
    ])
    return menu_inline_keyboard
