from aiogram.fsm.state import StatesGroup, State


class HometaskMenu(StatesGroup):
    select_hometask = State()


class HometaskInfo(StatesGroup):
    info_hometask = State()