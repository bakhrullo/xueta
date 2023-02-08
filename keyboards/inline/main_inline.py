from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from backend.models import *
from utils.db_api.database import *


async def customs_keyboard(lang, region):
    customs = await get_customs_by_region(region)
    markup = InlineKeyboardMarkup(row_width=1)
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
    if lang == "en":
        text_back = "Back"
    if lang == "ru":
        text_back = "Назад"
    markup.add(InlineKeyboardButton(text=f"🔙 {text_back}", callback_data=f"back"))
    return markup


async def tnved_keyboard(lang):
    kods = TnVed.objects.all()
    markup = InlineKeyboardMarkup(row_width=1)
    text_back = ''
    for i in kods:
        if lang == "uz":
            text_back = "Ortga"
            markup.insert(InlineKeyboardButton(text=f"{i.kod}", callback_data=i.id))
        if lang == "en":
            text_back = "Back"
            markup.insert(InlineKeyboardButton(text=f"{i.kod}", callback_data=i.id))
        if lang == "ru":
            text_back = "Назад"
            markup.insert(InlineKeyboardButton(text=f"{i.kod}", callback_data=i.id))
    if lang == "uz":
        text_back = "Ortga"
    if lang == "en":
        text_back = "Back"
    if lang == "ru":
        text_back = "Назад"
    markup.add(InlineKeyboardButton(text=f"🔙 {text_back}", callback_data=f"back"))
    return markup


async def posts_keyboard(lang, region):
    posts = PostService.objects.filter(region__id=region).all()
    markup = InlineKeyboardMarkup(row_width=2)
    text_back = ''
    for i in posts:
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
        texts = ["Ortga", "Yuklovchi xizmati (Грузчик)", "Yuklovchi texnika", "Yuk tashish"]
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
    markup.row(InlineKeyboardButton(text=f"{texts[1]}", callback_data=f"kara"))
    markup.row(InlineKeyboardButton(text=f"{texts[2]}", callback_data=f"manipulyator"))
    markup.row(InlineKeyboardButton(text=f"{texts[3]}", callback_data=f"evacuator"))
    markup.row(InlineKeyboardButton(text=f"🔙 {texts[0]}", callback_data=f"back"))
    return markup


async def logistics_keyboard(lang):
    markup = InlineKeyboardMarkup(row_width=2)
    texts = ['']
    if lang == "uz":
        texts = ["Ortga", "Ichki", "Tashqi"]
    if lang == "en":
        texts = ["Back", "Internal", "External"]
    if lang == "ru":
        texts = ["Назад", "Внутренний", "Внешний"]
    markup.insert(InlineKeyboardButton(text=f"{texts[1]}", callback_data=f"internal"))
    markup.insert(InlineKeyboardButton(text=f"{texts[2]}", callback_data=f"external"))
    markup.row(InlineKeyboardButton(text=f"🔙 {texts[0]}", callback_data=f"back"))
    return markup


async def tonna_keyboard(lang):
    markup = InlineKeyboardMarkup(row_width=2)
    texts = ['']
    if lang == "uz":
        texts = ["Ortga"]
    if lang == "en":
        texts = ["Back"]
    if lang == "ru":
        texts = ["Назад"]
    markup.insert(InlineKeyboardButton(text=f"0-10", callback_data=f"0-10"))
    markup.insert(InlineKeyboardButton(text=f"11-20", callback_data=f"11-20"))
    markup.insert(InlineKeyboardButton(text=f"21-25", callback_data=f"21-25"))
    markup.insert(InlineKeyboardButton(text=f"26-30", callback_data=f"26-30"))
    markup.insert(InlineKeyboardButton(text=f"30+", callback_data=f"31-10000"))
    markup.row(InlineKeyboardButton(text=f"🔙 {texts[0]}", callback_data=f"back"))
    return markup


async def sertification_keyboard(lang, page):
    serts = Sertification.objects.all()
    
    objects = serts[(int(page)-1) * 10 : int(page) * 10]
    markup = InlineKeyboardMarkup()
    texts = ''
    for i in objects:
        if lang == "uz":
            texts = ["Ortga"]
            markup.add(InlineKeyboardButton(text=f"{i.name_uz}", callback_data=i.id))
        if lang == "en":
            texts = ["Back"]
            markup.add(InlineKeyboardButton(text=f"{i.name_en}", callback_data=i.id))
        if lang == "ru":
            texts = ["Назад"]
            markup.add(InlineKeyboardButton(text=f"{i.name_ru}", callback_data=i.id))
    markup.row(InlineKeyboardButton(text=f"⬅️", callback_data=f"last_page"))
    markup.insert(InlineKeyboardButton(text=f"➡️", callback_data=f"next_page"))
    markup.row(InlineKeyboardButton(text=f"🔙 {texts[0]}", callback_data=f"back"))
    return markup


async def pagination_keyboard(lang):
    markup = InlineKeyboardMarkup()
    texts = ''
    if lang == "uz":
        texts = ["Ortga"]
    if lang == "en":
        texts = ["Back"]
    if lang == "ru":
        texts = ["Назад"]
    markup.row(InlineKeyboardButton(text=f"⬅️", callback_data=f"last_page"))
    markup.insert(InlineKeyboardButton(text=f"➡️", callback_data=f"next_page"))
    markup.row(InlineKeyboardButton(text=f"🔙 {texts[0]}", callback_data=f"back"))
    return markup


async def back(lang):
    markup = InlineKeyboardMarkup(row_width=2)
    texts = ['']
    if lang == "uz":
        texts = ["Ortga", "Yuklovchi xizmati (Грузчик)", "Yuklovchi texnika", "Yuk tashish"]
    if lang == "en":
        texts = ["Back", "Loader service", "Loader equipment", "Shipping"]
    if lang == "ru":
        texts = ["Назад", "Услуги грузчика", "Погрузочная техника", "Перевозки"]
    markup.row(InlineKeyboardButton(text=f"🔙 {texts[0]}", callback_data=f"back"))
    return markup

