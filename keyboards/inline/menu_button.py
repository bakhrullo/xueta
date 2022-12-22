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
    for category in categories:
        if lang == "uz":
            keyboard.insert(KeyboardButton(text=category.name_uz))
        if lang == "en":
            keyboard.insert(KeyboardButton(text=category.name_en))
        if lang == "ru":
            keyboard.insert(KeyboardButton(text=category.name_ru))
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

async def back_to_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga", "Asosiy menyu"]
    elif lang == "en":
        texts = ["Back", "Main menu"]
    elif lang == "ru":
        texts = ["Назад", "Главное меню"]

    keyboard = ReplyKeyboardMarkup()
    key2 = KeyboardButton(text=f"⬅️ {texts[0]}")
    keyboard.add(key2)
    keyboard.resize_keyboard = True
    return keyboard


async def get_phone_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga", "Asosiy menyu", "Qo'ng'iroq buyurtma qilish"]
    elif lang == "en":
        texts = ["Back", "Main menu", "Order a call"]
    elif lang == "ru":
        texts = ["Назад", "Главное меню", "Заказ звонка"]

    keyboard = ReplyKeyboardMarkup()
    key3 = KeyboardButton(text=f"{texts[2]}")
    key1 = KeyboardButton(text=f"🏠 {texts[1]}")
    key2 = KeyboardButton(text=f"⬅️ {texts[0]}")
    keyboard.add(key3)
    keyboard.add(key1, key2)
    keyboard.resize_keyboard = True
    return keyboard


async def kontrakt_keyboard(lang):
    texts = []
    if lang == "uz":
        texts = ["Orqaga", "Asosiy menyu", "Import/eksport shartnoma tuzish", "EGISOA bo'yicha ro'yxatdan o'tish", "Kontraktdagi muammolarni hal qilish"]
    elif lang == "en":
        texts = ["Back", "Main menu", "Conclusion of an import/export contract", "Registration under EGISOA", "Solving contract problems"]
    elif lang == "ru":
        texts = ["Назад", "Главное меню", "Заключение импортно-экспортного контракта", "Регистрация в ЕГИСОА", "Решение проблем с контрактами"]

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
    key2 = KeyboardButton(text=f"⬅️ {texts[0]}")
    keyboard.add(key1, key2)
    return keyboard