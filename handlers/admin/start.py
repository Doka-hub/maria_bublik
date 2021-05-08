import os

import mimetypes

from uuid import uuid4

import pandas as pd

from aiogram import types

from utils.db_api.user import get_user_list
from utils.misc.set_commands import set_commands

from keyboards.inline.user import get_menu_inline_keyboard

from loader import _


@set_commands
async def bot_start(message: types.Message):
    menu_inline_keyboard = get_menu_inline_keyboard()
    await message.answer(_('Меню'), reply_markup=menu_inline_keyboard)
    print('есть')


async def download_bd_users(callback: types.CallbackQuery):
    db_users = {
        'user_id': [],
        'user_username': [],
        'user_name': [],
        'user_format': [],
    }
    for user in await get_user_list():
        db_users['user_id'].append(user.user_id)
        db_users['user_username'].append(user.username)
        db_users['user_name'].append(user.name)
        db_users['user_format'].append(user.material_format)
    excel_file_path = f'data/'
    if not os.path.exists(excel_file_path):
        os.makedirs(excel_file_path, exist_ok=True)
    excel_file_name = excel_file_path + f'{uuid4()}.xlsx'
    print(db_users)
    df = pd.DataFrame(db_users)
    df.to_excel(excel_file_name)
    await callback.message.answer_document(types.InputFile(excel_file_name, 'users.xlsx'))
    os.remove(excel_file_name)

