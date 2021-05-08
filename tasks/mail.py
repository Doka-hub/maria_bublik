from keyboards.inline.user.mail import get_mail_message_buttons_inline_keyboard

from utils.db_api.user import get_user_list, get_material_format

from .utils.mailing import send_message


async def mail(mail_data: dict):
    material_format_id = mail_data.get('material_format_id')
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

    if material_format_id != 'users':
        material_format = await get_material_format(int(material_format_id))
        print(material_format)
        if material_format:
            for user in material_format.users:
                to = user.user_id
                await send_message(to, title, text, None, image_id, video_id, document, 'markdown',
                                   mail_message_buttons_inline_keyboard)
    else:
        user_list = await get_user_list()
        for user in user_list:
            to = user.user_id
            await send_message(to, title, text, None, image_id, video_id, document, 'markdown',
                               mail_message_buttons_inline_keyboard)
