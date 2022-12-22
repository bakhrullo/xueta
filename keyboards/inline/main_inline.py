from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from backend.models import *
from utils.db_api.database import *


async def customs_keyboard(lang):
    customs = await get_all_customs()
    markup = InlineKeyboardMarkup(row_width=2)
    text_back = ''
    for i in customs:
        if lang == "uz":
            text_back = "Ortga"
            markup.insert(InlineKeyboardButton(text=f"{i.name_uz}", callback_data=i.id))
        if lang == "en":
            text_back = "Back"
            markup.insert(InlineKeyboardButton(text=f"{i.name_en}", callback_data=i.id))
        if lang == "ru":
            text_back = "Назад"
            markup.insert(InlineKeyboardButton(text=f"{i.name_ru}", callback_data=i.id))
    if lang == "uz":
        text_back = "Ortga"
        markup.add(InlineKeyboardButton(text=f"🔙 {text_back}", callback_data=f"back"))
    if lang == "en":
        text_back = "Back"
        markup.add(InlineKeyboardButton(text=f"🔙 {text_back}", callback_data=f"back"))
    if lang == "ru":
        text_back = "Назад"
        markup.add(InlineKeyboardButton(text=f"🔙 {text_back}", callback_data=f"back"))
    return markup
