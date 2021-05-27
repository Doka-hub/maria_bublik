from aiogram import types

from utils.db_api.user.user import get_or_create_user
from utils.misc.set_commands import set_commands

from keyboards.inline.user import get_material_format_choose_list_inline_keyboard

from loader import _

from states.user import TGUserState


@set_commands
async def bot_start(message: types.Message):
    user_id, username = message.from_user.id, message.from_user.username or None
    user, user_created = await get_or_create_user(user_id, username)

    if not user.name:
        await message.answer(_('Як Вас звати? 👋🏼'))
        await TGUserState.name.set()
    else:
        if not user.material_format:
            material_format_list_inline_keyboard = await get_material_format_choose_list_inline_keyboard()
            await message.answer(
                _('Супер 🚀 Дякую, {}. Який освітній формат Let’s Speak Вас найбільше цікавить?').format(user.name),
                reply_markup=material_format_list_inline_keyboard)
            await TGUserState.material_format.set()

