from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.user import get_material_format_list
from utils.keyboards.inline import get_inline_keyboard

from loader import _


async def get_material_format_list_inline_keyboard() -> InlineKeyboardMarkup:
    material_format_list = [
        [
            InlineKeyboardButton(material_format.name,
                                 callback_data=f'mail_create {material_format.id}'),
        ] for material_format in await get_material_format_list()
    ]
    material_format_list_inline_keyboard = get_inline_keyboard(
        [
            [
                InlineKeyboardButton(_('Всем'), callback_data='mail_users')
            ]
        ] + material_format_list
    )
    return material_format_list_inline_keyboard


async def get_material_format_choose_list_inline_keyboard() -> InlineKeyboardMarkup:
    material_format_list_inline_keyboard = get_inline_keyboard([
        [
            InlineKeyboardButton(material_format.name,
                                 callback_data=f'material_format_choose {material_format.id}'),
        ] for material_format in await get_material_format_list()
    ])
    return material_format_list_inline_keyboard
