from aiogram.dispatcher.filters.state import State, StatesGroup


class TGUserState(StatesGroup):
    name = State()
    material_format = State()
