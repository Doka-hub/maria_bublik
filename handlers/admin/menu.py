from aiogram import types

from keyboards.inline.user import get_menu_inline_keyboard

from loader import _


async def menu(callback: types.CallbackQuery):
    menu_inline_keyboard = get_menu_inline_keyboard()
    await callback.message.answer(_('Меню'), reply_markup=menu_inline_keyboard)
