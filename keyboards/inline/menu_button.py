from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from backend.models import *


async def settings_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Raqamni o'zgartirish", "Tilni o'zgartirish", "Orqaga"]
    elif lang == "ru":
        texts = ["Изменить номер телефона", "Изменить язык", "Назад"]
    else:
        texts = ["Change phone number", "Change language", "Back"]
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"📞 {texts[0]}")
    key2 = KeyboardButton(text=f"🔄 {texts[1]}")
    key_back = KeyboardButton(text=f"⬅️️ {texts[2]}")
    keyboard.add(key1, key2)
    keyboard.add(key_back)
    keyboard.resize_keyboard = True
    return keyboard


async def language_keyboard():
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text="🇺🇿 O'zbek tili")
    key2 = KeyboardButton(text="🇺🇸 English")
    key3 = KeyboardButton(text="🇷🇺 Русский язык")
    keyboard.add(key1, key2, key3)
    keyboard.resize_keyboard = True
    return keyboard

async def phone_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Raqamni ulashish", "Orqaga"]
    elif lang == "ru":
        texts = ["Отправить номер телефона", "Назад"]
    elif lang == "en":
        texts = ["Send phone number", "Back"]
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"📞 {texts[0]}", request_contact=True)
    key2 = KeyboardButton(text=f"⬅️ {texts[1]}")
    keyboard.add(key1)
    keyboard.add(key2)
    keyboard.resize_keyboard = True
    return keyboard


async def user_menu(lang):
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    categories = Category.objects.all()
    text = []
    for category in categories:
        if lang == "uz":
            if category.name_uz == "Kontrakt 🗂":
                keyboard.row_width(1, KeyboardButton(text=category.name_uz))
            else:
                keyboard.insert(KeyboardButton(text=category.name_uz))
        if lang == "en":
            if category.name_uz == "Kontrakt 🗂":
                keyboard.row_width(1, KeyboardButton(text=category.name_en))
            else:
                keyboard.insert(KeyboardButton(text=category.name_en))
        if lang == "ru":
            if category.name_uz == "Kontrakt 🗂":
                keyboard.row_width(1, KeyboardButton(text=category.name_ru))
            else:
                keyboard.insert(KeyboardButton(text=category.name_ru))
    if lang == "uz":
        text = ["Eng yaqin manzillar", "Sozlamalar ⚙️", "Valyutalar kursi 💳", "Kutubxona 📚"]
    if lang == "en":
        text = ["Nearest addresses", "Settings ⚙️", "Exchange rates 💳", "Library 📚"]
    if lang == "ru":
        text = ["Самые близкие адреса", "Настройки ⚙️", "Курсы обмена валюты 💳", "Библиотека 📚"]
    key1 = KeyboardButton(text=f"{text[0]}")
    key2 = KeyboardButton(text=f"{text[2]}")
    key4 = KeyboardButton(text=f"{text[3]}")
    key3 = KeyboardButton(text=f"{text[1]}")
    keyboard.row(key1, key2)
    keyboard.row(key4, key3)
    return keyboard

async def back_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga", "Asosiy menyu"]
    elif lang == "en":
        texts = ["Back", "Main menu"]
    elif lang == "ru":
        texts = ["Назад", "Главное меню"]

    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"🏠 {texts[1]}")
    key2 = KeyboardButton(text=f"⬅️ {texts[0]}")
    keyboard.add(key1, key2)
    keyboard.resize_keyboard = True
    return keyboard


async def asd_back_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga", "Asosiy menyu", "Tashlab ketish"]
    elif lang == "en":
        texts = ["Back", "Main menu", "Skip"]
    elif lang == "ru":
        texts = ["Назад", "Главное меню", "Пропустить"]

    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"🏠 {texts[1]}")
    key2 = KeyboardButton(text=f"⬅️ {texts[0]}")
    key3 = KeyboardButton(text=f"{texts[2]} ➡️")
    keyboard.add(key2, key3)
    keyboard.add(key1)
    keyboard.resize_keyboard = True
    return keyboard


async def back_to_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga", "Asosiy menyu"]
    elif lang == "en":
        texts = ["Back", "Main menu"]
    elif lang == "ru":
        texts = ["Назад", "Главное меню"]

    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
    key2 = KeyboardButton(text=f"⬅️ {texts[0]}")
    keyboard.add(key2)
    keyboard.resize_keyboard = True
    return keyboard


async def library_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga", "Qarorlar", "Qonunlar", "Yangiliklar"]
    elif lang == "en":
        texts = ["Back", "Decisions", "Laws", "News"]
    elif lang == "ru":
        texts = ["Назад", "Указы", "Законы", "Новости"]

    keyboard = ReplyKeyboardMarkup()
    
    key1 = KeyboardButton(text=f"{texts[1]}")
    key2 = KeyboardButton(text=f"{texts[2]}")
    key3 = KeyboardButton(text=f"{texts[3]}")
    key_back = KeyboardButton(text=f"⬅️ {texts[0]}")
    keyboard.add(key1, key2, key3)
    keyboard.add(key_back)
    keyboard.resize_keyboard = True
    return keyboard


async def get_phone_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga", "Asosiy menyu", "Qo'ng'iroq buyurtma qilish", "Savol qoldirish"]
    elif lang == "en":
        texts = ["Back", "Main menu", "Order a call", "Leave a question"]
    elif lang == "ru":
        texts = ["Назад", "Главное меню", "Заказ звонка", "Оставить вопрос"]

    keyboard = ReplyKeyboardMarkup()
    key3 = KeyboardButton(text=f"{texts[2]}")
    key4 = KeyboardButton(text=f"{texts[3]}")
    key1 = KeyboardButton(text=f"🏠 {texts[1]}")
    # key2 = KeyboardButton(text=f"⬅️ {texts[0]}")
    keyboard.add(key3, key4)
    keyboard.add(key1)
    keyboard.resize_keyboard = True
    return keyboard


async def get_company_monthly(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga", "t.",]
    elif lang == "en":
        texts = ["Back", "t."]
    elif lang == "ru":
        texts = ["Назад", "т."]

    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"0-25 {texts[1]}")
    key3 = KeyboardButton(text=f"25-50 {texts[1]}")
    key4 = KeyboardButton(text=f"50-100 {texts[1]}")
    key2 = KeyboardButton(text=f"⬅️ {texts[0]}")
    keyboard.add(key1, key3, key4)
    keyboard.add(key2)
    keyboard.resize_keyboard = True
    return keyboard


async def kontrakt_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga", "Asosiy menyu", "Import/eksport shartnoma tuzish", "YeEISVO bo'yicha ro'yxatdan o'tish", "Kontraktdagi muammolarni hal qilish"]
    elif lang == "en":
        texts = ["Back", "Main menu", "Conclusion of an import/export contract", "Registration under YeEISVO", "Solving contract problems"]
    elif lang == "ru":
        texts = ["Назад", "Главное меню", "Заключение импортно-экспортного контракта", "Регистрация в ЕЭИСВО", "Решение проблем с контрактами"]

    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"🏠 {texts[1]}")
    key2 = KeyboardButton(text=f"{texts[2]}")
    key3 = KeyboardButton(text=f"{texts[3]}")
    key4 = KeyboardButton(text=f"{texts[4]}")
    keyboard.add(key2, key3)
    keyboard.add(key4)
    keyboard.add(key1)
    keyboard.resize_keyboard = True
    return keyboard


async def product_categories(lang):
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False)
    categories = ProductCategory.objects.all()
    keys = []
    for category in categories:
        if lang == "uz":
            texts = ["Orqaga", "Asosiy menyu"]    
            keyboard.insert(KeyboardButton(text=category.name_uz))
        if lang == "en":
            texts = ["Back", "Main menu"]
            keyboard.insert(KeyboardButton(text=category.name_en))
        if lang == "ru":
            keyboard.insert(KeyboardButton(text=category.name_ru))
            texts = ["Назад", "Главное меню"]
    key1 = KeyboardButton(text=f"🏠 {texts[1]}")
    keyboard.add(key1)
    return keyboard


async def location_send(lang):
    text = []
    if lang == 'uz':
        text = ['Joylashuvni ulashish', "Orqaga"]
    elif lang == 'ru':
        text = ['Отправить местоположение', "Назад"]
    elif lang == 'en':
        text = ['Send location',  "Back"]
    mrk = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    bt = KeyboardButton(f'📍 {text[0]}', request_location=True)
    back_key = KeyboardButton(f"⬅️ {text[1]}")
    mrk.add(bt)
    mrk.add(back_key)
    return mrk
