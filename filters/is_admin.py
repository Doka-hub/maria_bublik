from aiogram import types
from aiogram.dispatcher.filters import BoundFilter, Command

from data import config

from .callback import CallbackData


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin=True):
        self.is_admin = is_admin

    async def check(self, message: types.Message) -> bool:
        return message.from_user.id in config.ADMINS

    @staticmethod
    def check_by_user_id(user_id: int) -> bool:
        return user_id in config.ADMINS


class BaseAdmin:
    @staticmethod
    async def is_admin(user_id: int):
        return AdminFilter().check_by_user_id(user_id)


class AdminCommand(Command, BaseAdmin):
    async def check(self, message: types.Message):
        if not await self.is_admin(message.from_user.id):
            return False
        return await super().check(message)


class AdminCallbackDataFilter(CallbackData, BaseAdmin):
    key = 'admin_callback_data'

    def __init__(self, admin_callback_data):
        super().__init__(admin_callback_data)

    async def check(self, callback: types.CallbackQuery):
        if not await self.is_admin(callback.from_user.id):
            return False
        return await super().check(callback)
