from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from .start import bot_start
from .menu import menu
from .group import (
    # CRUD
    group_list, group_detail, group_create, group_delete,

    # States
    GroupState,

    # Обработчик данных
    group_create__name_handler, group_create__cancel
)
from .channel import (
    # CRUD
    channel_list, channel_create, channel_create_by_list, channel_delete,

    # States
    ChannelState,

    # Обработчик данных
    channel_create__username_handler, channel_create__forward_message_handler, channel_create__cancel,
    channel_create__username_list_handler
)
from .mail import (
    # Выбор группы для рассылки
    group_list_to_mail, channel_list_to_mail,

    # States
    MailState,

    # Создание письма
    mail_create, mail_create__cancel,
    mail_create__image, mail_create__title, mail_create__text, mail_create__button,

    # Обработчик данных
    mail_create__data_cancel,
    mail_create__image_handler, mail_create__title_handler, mail_create__text_handler, mail_create__button_handler,

    # Отправка сообщения
    mail_send
)
from .language import choose_language, change_language


def setup(dp: Dispatcher):
    # Старт
    dp.register_message_handler(bot_start, CommandStart(), in_whitelist=True)

    # Меню
    dp.register_callback_query_handler(menu, lambda callback: callback.data == 'menu', in_whitelist=True)

    # Язык
    dp.register_callback_query_handler(choose_language, lambda callback: callback.data.startswith('choose_language '),
                                       in_whitelist=True)
    dp.register_callback_query_handler(change_language, lambda callback: callback.data == 'change_language',
                                       in_whitelist=True)

    # Группа
    dp.register_callback_query_handler(group_list, lambda callback: callback.data == 'group_list', in_whitelist=True)
    dp.register_callback_query_handler(group_detail, lambda callback: callback.data.startswith('group_detail '))
    dp.register_callback_query_handler(group_create, lambda callback: callback.data == 'group_create')
    dp.register_callback_query_handler(group_delete, lambda callback: callback.data.startswith('group_delete '))

    # Группа - обработчик данных
    dp.register_message_handler(group_create__name_handler, state=GroupState.name)
    dp.register_callback_query_handler(group_create__cancel, lambda callback: callback.data == 'group_create__cancel',
                                       state=GroupState.name)

    # Канал
    dp.register_callback_query_handler(channel_list, lambda callback: callback.data.startswith('channel_list '))
    dp.register_callback_query_handler(channel_create, lambda callback: callback.data.startswith('channel_create '))
    dp.register_callback_query_handler(channel_create_by_list,
                                       lambda callback: callback.data.startswith('channel_create_by_list '))
    dp.register_callback_query_handler(channel_delete, lambda callback: callback.data.startswith('channel_delete '))

    # Канал - обработчик данных
    dp.register_message_handler(channel_create__forward_message_handler, lambda m: m.forward_from_chat,
                                state=ChannelState.username, )
    dp.register_message_handler(channel_create__username_handler, state=ChannelState.username, )
    dp.register_message_handler(channel_create__username_list_handler, state=ChannelState.username_list, )
    dp.register_callback_query_handler(channel_create__cancel,
                                       lambda callback: callback.data.startswith('channel_create__cancel '),
                                       state=ChannelState.username, )
    dp.register_callback_query_handler(channel_create__cancel,
                                       lambda callback: callback.data.startswith('channel_create__cancel '),
                                       state=ChannelState.username_list, )

    # Рассылка
    dp.register_callback_query_handler(group_list_to_mail, lambda callback: callback.data == 'group_list_to_mail',
                                       )
    dp.register_callback_query_handler(channel_list_to_mail,
                                       lambda callback: callback.data.startswith('channel_list_to_mail '),
                                       )
    # Рассылка - создание
    dp.register_callback_query_handler(mail_create, lambda callback: callback.data.startswith('mail_create '),
                                       )

    # Создание рассылки - картинка
    dp.register_callback_query_handler(mail_create__image, lambda callback: callback.data == 'mail_create__image')
    dp.register_callback_query_handler(mail_create__image, lambda callback: callback.data == 'mail_update__image')
    dp.register_message_handler(mail_create__image_handler, state=MailState.image_id,
                                content_types=types.ContentTypes.ANY)
    dp.register_callback_query_handler(mail_create__data_cancel,
                                       lambda callback: callback.data == 'mail_create__data_cancel',
                                       state=MailState.image_id)

    # Создание рассылки - заголовок
    dp.register_callback_query_handler(mail_create__title, lambda callback: callback.data == 'mail_create__title')
    dp.register_callback_query_handler(mail_create__title, lambda callback: callback.data == 'mail_update__title')
    dp.register_message_handler(mail_create__title_handler,
                                state=MailState.title, content_types=types.ContentTypes.TEXT)
    dp.register_callback_query_handler(mail_create__data_cancel,
                                       lambda callback: callback.data == 'mail_create__data_cancel',
                                       state=MailState.title)

    # Создание рассылки - текст
    dp.register_callback_query_handler(mail_create__text, lambda callback: callback.data == 'mail_create__text')
    dp.register_callback_query_handler(mail_create__text, lambda callback: callback.data == 'mail_update__text')
    dp.register_message_handler(mail_create__text_handler,
                                state=MailState.text, content_types=types.ContentTypes.TEXT)
    dp.register_callback_query_handler(mail_create__data_cancel,
                                       lambda callback: callback.data == 'mail_create__data_cancel',
                                       state=MailState.text)

    # Создание рассылки - кнопка
    dp.register_callback_query_handler(mail_create__button, lambda callback: callback.data == 'mail_create__button1')
    dp.register_callback_query_handler(mail_create__button, lambda callback: callback.data == 'mail_update__button1')
    dp.register_message_handler(mail_create__button_handler,
                                state=MailState.button1, content_types=types.ContentTypes.TEXT)
    dp.register_callback_query_handler(mail_create__data_cancel,
                                       lambda callback: callback.data == 'mail_create__data_cancel',
                                       state=MailState.button1)

    # Создание рассылки - кнопка 2
    dp.register_callback_query_handler(mail_create__button, lambda callback: callback.data == 'mail_create__button2')
    dp.register_callback_query_handler(mail_create__button, lambda callback: callback.data == 'mail_update__button2')
    dp.register_message_handler(mail_create__button_handler,
                                state=MailState.button2, content_types=types.ContentTypes.TEXT)
    dp.register_callback_query_handler(mail_create__data_cancel,
                                       lambda callback: callback.data == 'mail_create__data_cancel',
                                       state=MailState.button2)

    # Создание рассылки - кнопка 3
    dp.register_callback_query_handler(mail_create__button, lambda callback: callback.data == 'mail_create__button3')
    dp.register_callback_query_handler(mail_create__button, lambda callback: callback.data == 'mail_update__button3')
    dp.register_message_handler(mail_create__button_handler,
                                state=MailState.button3, content_types=types.ContentTypes.TEXT)
    dp.register_callback_query_handler(mail_create__data_cancel,
                                       lambda callback: callback.data == 'mail_create__data_cancel',
                                       state=MailState.button3)

    # Создание рассылки - кнопка 4
    dp.register_callback_query_handler(mail_create__button, lambda callback: callback.data == 'mail_create__button4')
    dp.register_callback_query_handler(mail_create__button, lambda callback: callback.data == 'mail_update__button4')
    dp.register_message_handler(mail_create__button_handler,
                                state=MailState.button4, content_types=types.ContentTypes.TEXT)
    dp.register_callback_query_handler(mail_create__data_cancel,
                                       lambda callback: callback.data == 'mail_create__data_cancel',
                                       state=MailState.button4)

    # Рассылка - обработчик данных
    # dp.register_message_handler(mail_create__message_handler, state=MailState.message,
    #                             content_types=types.ContentTypes.ANY, )
    dp.register_callback_query_handler(mail_create__cancel,
                                       lambda callback: callback.data.startswith('mail_create__cancel '), )

    # Рассылка - отправка сообщения
    dp.register_callback_query_handler(mail_send, lambda callback: callback.data == 'mail_send', )
