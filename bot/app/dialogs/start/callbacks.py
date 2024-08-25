from aiogram.types import CallbackQuery

from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import DialogManager

from app.dialogs.hometask.states import HometaskMenu
from app.dialogs.schedule.states import ScheduleMenu
from app.dialogs.settings.states import SettingsMenu


async def on_chosen_hometask(c: CallbackQuery, widget: Button, manager: DialogManager):
    await manager.start(HometaskMenu.select_hometask)


async def on_chosen_schedule(c: CallbackQuery, widget: Button, manager: DialogManager):
    await manager.start(ScheduleMenu.select_schedule)


async def on_chosen_settings(c: CallbackQuery, widget: Button, manager: DialogManager):
    await manager.start(SettingsMenu.settings)
