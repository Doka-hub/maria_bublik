from typing import Optional

from keyboards.inline.user.mail import get_mail_message_buttons_inline_keyboard

from utils.db_api.user.user import get_user_list

from .utils.mailing import send_message


async def mail(mail_data: dict):
    group_id = mail_data.get('group_id')
    image_id = mail_data.get('image_id')
    video_id = mail_data.get('video_id')
    document = mail_data.get('document')
    title = mail_data.get('title')
    text = mail_data.get('text')
    button = mail_data.get('button1')
    button2 = mail_data.get('button2')
    button3 = mail_data.get('button3')
    button4 = mail_data.get('button4')
    mail_message_buttons_inline_keyboard = get_mail_message_buttons_inline_keyboard(
        [button, button2, button3, button4]) or None
    user_list = await get_user_list()
    for user in user_list:
        to = user.user_id
        await send_message(to, title, text, None, image_id, video_id, document, 'markdown',
                           mail_message_buttons_inline_keyboard)
