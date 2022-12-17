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
    texts = []
    if lang == "uz":
        texts = ["Mahsulotlar", "Sozlamalar", "Biz haqimizda", "Aloqa va manzillar", "Keshbeklar haqida ma'lumot", "Bonus"]
    elif lang == "en":
        texts = ["Products", "Settings", "About us", "Contact and addresses", "Information about cashbacks", "Bonus"]
    elif lang == "ru":
        texts = ["Продукты", "Настройки", "О нас", "Контакты и адреса", "Информация о кэшбэках", "Бонус"]

    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"🛍 {texts[0]}")
    key2 = KeyboardButton(text=f"⚙️ {texts[1]}")
    key3 = KeyboardButton(text=f"ℹ️ {texts[2]}")
    key4 = KeyboardButton(text=f"📞 {texts[3]}")
    key5 = KeyboardButton(text=f"💰 {texts[4]}")
    key6 = KeyboardButton(text=f"💎 {texts[5]}")
    keyboard.add(key1)
    keyboard.add(key5, key6, key2)
    keyboard.add(key3, key4)
    keyboard.resize_keyboard = True
    keyboard.one_time_keyboard = True
    return keyboard


async def back_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga"]
    elif lang == "en":
        texts = ["Back"]
    elif lang == "ru":
        texts = ["Назад"]

    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"⬅️ {texts[0]}")
    keyboard.add(key1)
    keyboard.resize_keyboard = True
    return keyboard
