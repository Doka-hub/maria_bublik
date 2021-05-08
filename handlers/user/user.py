from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.db_api.user import get_or_create_user, set_user__name, set_user__media_format

from keyboards.inline.user import get_material_format_choose_list_inline_keyboard

from loader import _

from states.user import TGUserState


async def user_name__handler(message: types.Message, state: FSMContext):
    user_id, username = message.from_user.id, message.from_user.username or None
    user, user_created = await get_or_create_user(user_id, username)

    name = message.text

    await state.reset_state()
    await set_user__name(user, name)

    material_format_list_inline_keyboard = await get_material_format_choose_list_inline_keyboard()
    await message.answer(
        _('Супер 🚀 Дякую, {}. Який освітній формат Let’s Speak Вас найбільше цікавить?').format(name),
        reply_markup=material_format_list_inline_keyboard)
    await TGUserState.material_format.set()


async def user_material_format__handler(callback: types.CallbackQuery, state: FSMContext):
    user_id, username = callback.from_user.id, callback.from_user.username or None
    user, created = await get_or_create_user(user_id, username)

    media_format_id = callback.data.replace('material_format_choose ', '')

    await state.reset_state()
    await set_user__media_format(user, media_format_id)

    await callback.message.edit_text(
        _('Amazing! Чекайте від нас новин, корисних освітніх подарунків і запрошень на різноманітні події 🚀')
    )
