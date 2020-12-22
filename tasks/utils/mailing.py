from typing import Union, Optional

from asyncio import sleep

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.exceptions import RetryAfter, Unauthorized, BotKicked, BadRequest

from loader import bot


def make_text(title: str, text: str) -> str:
    return f'*{title or ""}*' + '\n\n' + f'{text or ""}'


async def send_message(to: Union[str, int], title: Optional[str] = None, text: Optional[str] = None,
                       message: Optional[str] = None, image_id: Optional[str] = None, video_id: Optional[str] = None,
                       parse_mode: Optional[str] = None, reply_markup: Optional[InlineKeyboardMarkup] = None,
                       disable_notification: Optional[bool] = True, tries: int = 0, max_tries: int = 5) -> bool:
    """
    :param to:
    :param title:
    :param text:
    :param message:
    :param image_id:
    :param video_id:
    :param parse_mode:
    :param reply_markup:
    :param disable_notification: отключаем звук
    :param tries: `n` совершенных проб
    :param max_tries: пробуем отправить сообщение максимум `n` раз
    :return:
    """
    if tries > max_tries:
        return False
    try:
        if not message:
            message = make_text(title, text)
        if image_id:
            await bot.send_photo(to, image_id, message, parse_mode=parse_mode, reply_markup=reply_markup,
                                 disable_notification=disable_notification)
        elif video_id:
            await bot.send_video(to, video_id, caption=message, parse_mode=parse_mode, reply_markup=reply_markup,
                                 disable_notification=disable_notification)
        else:
            await bot.send_message(to, text, parse_mode=parse_mode, reply_markup=reply_markup,
                                   disable_notification=disable_notification)
    except RetryAfter as e:
        error = f'{e}'
        time = error[error.find('Retry in ') + len('Retry in '):error.find(' seconds')]  # сколько нужно ждать
        await sleep(float(time))
        return await send_message(to, title, text, message, image_id, video_id, parse_mode, reply_markup,
                                  disable_notification, tries + 1, max_tries)
    except BotKicked:
        pass
    except Unauthorized:
        pass
    except BadRequest:
        pass
    return True
