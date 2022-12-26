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


async def region_keyboard(lang):
    regions = await get_regions()
    markup = InlineKeyboardMarkup(row_width=2)
    text_back = ''
    for i in regions:
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


async def wearhouses_keyboard(lang, region_id):
    regions = await get_wearhouse_by_region(region_id)
    markup = InlineKeyboardMarkup(row_width=1)
    text_back = ''
    for i in regions:
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


async def freight_keyboard(lang):
    markup = InlineKeyboardMarkup(row_width=2)
    texts = ['']
    if lang == "uz":
        texts = ["Ortga", "Yuklovchi xizmati", "Yuklovchi texnika", "Yuk tashish"]
    if lang == "en":
        texts = ["Back", "Loader service", "Loader equipment", "Shipping"]
    if lang == "ru":
        texts = ["Назад", "Услуги грузчика", "Погрузочная техника", "Перевозки"]
    markup.row(InlineKeyboardButton(text=f"{texts[1]}", callback_data=f"loader_service"))
    markup.row(InlineKeyboardButton(text=f"{texts[2]}", callback_data=f"loader_equipment"))
    markup.row(InlineKeyboardButton(text=f"{texts[3]}", callback_data=f"shipping"))
    markup.row(InlineKeyboardButton(text=f"🔙 {texts[0]}", callback_data=f"back"))
    return markup

async def loader_equipment_keyboard(lang):
    markup = InlineKeyboardMarkup(row_width=2)
    texts = ['']
    if lang == "uz":
        texts = ["Ortga", "Kara", "Manipulyator", "Evakuvator"]
    if lang == "en":
        texts = ["Back", "Cara", "Manipulator", "Evacuator"]
    if lang == "ru":
        texts = ["Назад", "Кара", "Манипулятор", "Эвакуатор"]
    markup.row(InlineKeyboardButton(text=f"{texts[1]}", callback_data=f"cara"))
    markup.row(InlineKeyboardButton(text=f"{texts[2]}", callback_data=f"manipulator"))
    markup.row(InlineKeyboardButton(text=f"{texts[3]}", callback_data=f"evacuator"))
    markup.row(InlineKeyboardButton(text=f"🔙 {texts[0]}", callback_data=f"back"))
    return markup
