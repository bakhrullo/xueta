from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminState(StatesGroup):
    get_msg = State()
    conf_msg = State()
