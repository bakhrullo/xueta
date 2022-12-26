from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.inline.main_inline import *
from keyboards.inline.menu_button import *
from utils.db_api import database as commands
from loader import dp, bot
from utils.db_api.database import *
import datetime
from aiogram.types import ReplyKeyboardRemove
from geopy.geocoders import Nominatim
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultPhoto, InputMediaPhoto, InlineQueryResultArticle
from aiogram.utils.deep_linking import decode_payload, get_start_link
import re
import requests


def isValid(s):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)


username = "zoneagency"
password = "j2e4AEFs84"

def send_sms(otp, phone):
    username = 'foodline'
    password = 'JvYkp44)-J&9'
    sms_data = {
        "messages":[{"recipient":f"{phone}","message-id":"abc000000003","sms":{"originator": "3700","content": {"text": f"Ваш код подтверждения для DARGAH EDU BOT: {otp}"}}}]}
    url = "http://91.204.239.44/broker-api/send"
    res = requests.post(url=url, headers={}, auth=(username, password), json=sms_data)
    print(res)



def generateOTP():
    return random.randint(111111, 999999)


@dp.message_handler(lambda message: message.text in ["🏠 Asosiy menyu", "🏠 Main menu", "🏠 Главное меню"], state='*')
async def go_home(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    markup = await user_menu(lang)
    if lang == "uz":
        await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
    elif lang == "ru":
        await message.answer("Добро пожаловать в наш бот. Выберите нужный раздел👇", reply_markup=markup)
    elif lang == "en":
        await message.answer("Welcome to our bot. Please select the desired section 👇", reply_markup=markup)
    await state.set_state("get_category")
 

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    user = await get_user(message.from_id)
    if user is not None:
        if user.lang:
            lang = await get_lang(message.from_user.id)
            if user.name:
                markup = await user_menu(lang)
                if lang == "uz":
                    await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
                elif lang == "ru":
                    await message.answer("Добро пожаловать в наш бот. Выберите нужный раздел👇", reply_markup=markup)
                elif lang == "en":
                    await message.answer("Welcome to our bot. Please select the desired section 👇", reply_markup=markup)
                await state.set_state("get_category")
            else:
                markup = await back_keyboard(lang)
                if lang == "uz":
                    await message.answer("Iltimos ismingizni kiriting 👇", reply_markup=markup)
                elif lang == "ru":
                    await message.answer("Пожалуйста, введите ваше имя 👇", reply_markup=markup)
                elif lang == "en":
                    await message.answer("Please enter your name 👇", reply_markup=markup)
                await state.set_state("get_name")
                
        else:
            markup =await language_keyboard()
            await message.answer(f"Assalomu alaykum, {message.from_user.first_name}👋. \nKerakli tilni tanlang 👇\n\nHello, {message.from_user.first_name}👋. \nChoose the language you need 👇\n\nЗдравствуйте, {message.from_user.first_name}👋. \nВыберите нужный язык 👇", 
                                reply_markup=markup)
            await state.set_state("get_lang")
            
    else:
        args = message.get_args()
        payload = decode_payload(args)
        if payload != '':
            await add_user(user_id=message.from_user.id, referal_user=payload)
        else:
            await add_user(user_id=message.from_user.id, referal_user="no_referal")
        markup =await language_keyboard()
        await message.answer(f"Assalomu alaykum, {message.from_user.first_name}👋. \nKerakli tilni tanlang 👇\n\nHello, {message.from_user.first_name}👋. \nChoose the language you need 👇\n\nЗдравствуйте, {message.from_user.first_name}👋. \nВыберите нужный язык 👇", 
                            reply_markup=markup)
        await state.set_state("get_lang")


@dp.message_handler(state="get_lang")
async def get_language(message: types.Message, state: FSMContext):
    if message.text in ["🇺🇿 O'zbek tili", "🇺🇸 English", "🇷🇺 Русский язык"]:
        if message.text == "🇺🇿 O'zbek tili":
            data = "uz"
        elif message.text == "🇺🇸 English":
            data = "en"
        elif message.text == "🇷🇺 Русский язык":
            data = "ru"
        user = await get_user(message.from_user.id)
        user.lang = data
        user.save()
        lang = await get_lang(message.from_user.id)

        markup = await back_keyboard(lang)
        if lang == "uz":
            await message.answer("Iltimos ismingizni kiriting 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Пожалуйста, введите ваше имя 👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Please enter your name 👇", reply_markup=markup)
        await state.set_state("get_name")
    else:
        markup =await language_keyboard()
        await message.answer(f"Kerakli tilni tanlang 👇\nChoose the language you need 👇\nВыберите нужный язык 👇", 
                            reply_markup=markup)
        await state.set_state("get_lang")


@dp.message_handler(state="get_name", content_types=types.ContentTypes.TEXT)
async def get_name(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)            
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup =await language_keyboard()
        await message.answer(f"Kerakli tilni tanlang 👇\nChoose the language you need 👇\nВыберите нужный язык 👇", 
                            reply_markup=markup)
        await state.set_state("get_lang")
    else:         
        user = await get_user(message.from_user.id)
        user.name = message.text
        user.save()
        markup = await phone_keyboard(lang)
        if lang == "uz":
            await message.answer("Telefon raqamininfizni xalqaro formatda(<b>998YYXXXXXXX</b>) kiriting. Yoki raqamni ulashing 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Введите свой номер телефона в международном формате (<b>998YYXXXXXX</b>). Или поделитесь номером 👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Enter your phone number in international format (<b>998YYXXXXXX</b>). Or share the number 👇", reply_markup=markup)
        await state.set_state("get_phone_number")


@dp.message_handler(content_types=types.ContentTypes.CONTACT, state="get_phone_number")
async def get_phone(message: types.Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number[1:]
        user = await get_user(message.from_user.id)
        user.new_phone = phone
        otp = generateOTP()
        send_sms(otp=otp, phone=phone)
        user.otp = otp
        user.save()
        print(user.otp)
        lang = await get_lang(message.from_user.id)
        keyboard = await back_keyboard(lang)
        if lang == "uz":
            await message.answer(text=f"<b>{user.new_phone}</b> raqamiga yuborilgan tasdiqlash kodini kiriting", parse_mode='HTML', reply_markup=keyboard)
        if lang == "ru":
            await message.answer(text=f"Введите код подтверждения, отправленный на номер <b>{user.new_phone}</b>.", parse_mode='HTML', reply_markup=keyboard)
        if lang == "en":
            await message.answer(text=f"Enter the verification code sent to <b>{user.new_phone}</b>", parse_mode='HTML', reply_markup=keyboard)
        await state.set_state("get_otp")
    

@dp.message_handler(content_types=types.ContentTypes.TEXT, state="get_phone_number")
async def get_phone(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if "⬅️️" in message.text:
        user = await get_user(message.from_id)
        if user is not None:
            lang = await get_lang(message.from_user.id)
            if user.phone is not None:
                markup = await user_menu(lang)
                if lang == "uz":
                    await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
                elif lang == "en":
                    await message.answer("Welcome to our bot. Choose the section you want 👇", reply_markup=markup)
                elif lang == "ru":
                    await message.answer("Добро пожаловать в наш бот. Пожалуйста, выберите нужный раздел 👇", reply_markup=markup)
                await state.set_state("get_category")
            else:
                markup = await phone_keyboard(lang)
                if lang == "uz":
                    await message.answer("Telefon raqamininfizni xalqaro formatda(<b>998YYXXXXXXX</b>) kiriting. Yoki raqamni ulashing👇", reply_markup=markup)
                elif lang == "en":
                    await message.answer("Enter your phone number in international format (<b>998YYXXXXXX</b>). Or share the number 👇", reply_markup=markup)
                elif lang == "ru":
                    await message.answer("Введите свой номер телефона в международном формате (<b>998YYXXXXXX</b>). Или поделитесь номером👇", reply_markup=markup)
                await state.set_state("get_phone_number")            
        else:
            markup =await language_keyboard()
            await message.answer(f"Assalomu alaykum, {message.from_user.first_name}👋. \nKerakli tilni tanlang 👇\n\nHello, {message.from_user.first_name}👋. \nChoose the language you need 👇\n\nЗдравствуйте, {message.from_user.first_name}👋. \nВыберите нужный язык 👇", 
                                reply_markup=markup)
            await state.set_state("get_lang")
    else:
        if isValid(message.text):
            phone = message.text
            user = await get_user(message.from_user.id)
            user.new_phone = phone
            otp = generateOTP()
            send_sms(otp=otp, phone=phone)
            user.otp = otp
            user.save()
            print(user.otp)
            keyboard = await back_keyboard(lang)
            if lang == "uz":
                await message.answer(text=f"<b>{user.new_phone}</b> raqamiga yuborilgan tasdiqlash kodini kiriting", parse_mode='HTML', reply_markup=keyboard)
            if lang == "en":
                await message.answer(text=f"Введите код подтверждения, отправленный на номер <b>{user.new_phone}</b>.", parse_mode='HTML', reply_markup=keyboard)
            if lang == "ru":
                await message.answer(text=f"Enter the verification code sent to <b>{user.new_phone}</b>", parse_mode='HTML', reply_markup=keyboard)
            await state.set_state("get_otp")
        else:
            markup = await phone_keyboard(lang)
            if lang == "uz":
                await message.answer("Telefon raqamininfizni xalqaro formatda(<b>998YYXXXXXXX</b>) kiriting. Yoki raqamni ulashing👇", reply_markup=markup)
            elif lang == "en":
                await message.answer("Enter your phone number in international format (<b>998YYXXXXXX</b>). Or share the number 👇", reply_markup=markup)
            elif lang == "ru":
                await message.answer("Введите свой номер телефона в международном формате (<b>998YYXXXXXX</b>). Или поделитесь номером👇", reply_markup=markup)
            await state.set_state("get_phone_number")            
        

@dp.message_handler(content_types=types.ContentTypes.TEXT, state="get_otp")
async def get_phone(message: types.Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    lang = user.lang
    if "⬅️️" in message.text: 
        markup = await phone_keyboard(lang)
        if lang == "uz":
            await message.answer("Telefon raqamininfizni xalqaro formatda(<b>998YYXXXXXXX</b>) kiriting. Yoki raqamni ulashing👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Enter your phone number in international format (<b>998YYXXXXXX</b>). Or share the number 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Введите свой номер телефона в международном формате (<b>998YYXXXXXX</b>). Или поделитесь номером👇", reply_markup=markup)
        await state.set_state("get_phone_number")            
    else:
        if message.text == user.otp:
            user.phone = user.new_phone
            user.save()
            markup = await user_menu(lang)
            if lang == "uz":
                await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
            elif lang == "en":
                await message.answer("Welcome to our bot. Choose the section you want 👇", reply_markup=markup)
            elif lang == "ru":
                await message.answer("Добро пожаловать в наш бот. Пожалуйста, выберите нужный раздел 👇", reply_markup=markup)
            await state.set_state("get_category")
        else:
            lang = await get_lang(message.from_user.id)
            markup = await back_keyboard(lang)
            if lang == "uz":
                await message.answer("⚠️ Yuborilgan tasdiqlash kodi xato. Qayta urinib ko'ring", reply_markup=markup)
            elif lang == "en":
                await message.answer("⚠️ The verification code sent is incorrect. Try again", reply_markup=markup)
            elif lang == "ru":
                await message.answer("⚠️ Присланный проверочный код неверный. Попробуйте еще раз", reply_markup=markup)
            await state.set_state("get_otp")


@dp.message_handler(state="get_category", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    back_key = await back_keyboard(lang)
    user = await get_user(message.from_user.id)
    if user.full:
        if message.text in ["Import", "Импорт"]:
            if lang == "uz":
                await message.answer("Tovar nomini kiriting 👇", reply_markup=back_key)
            if lang == "en":
                await message.answer("Enter the product name 👇", reply_markup=back_key)
            if lang == "ru":
                await message.answer("Введите название продукта 👇", reply_markup=back_key)
            await state.set_state("import_product_name")
        if message.text in ["Export", "Импорт"]:
            if lang == "uz":
                await message.answer("Tovar nomini kiriting 👇", reply_markup=back_key)
            if lang == "en":
                await message.answer("Enter the product name 👇", reply_markup=back_key)
            if lang == "ru":
                await message.answer("Введите название продукта 👇", reply_markup=back_key)
            await state.set_state("export_product_name")   
        if message.text in ["Contract", "Kontrakt", "Контракт"]:
            markup = await kontrakt_keyboard(lang)
            if lang == "uz":
                await message.answer("Kerakli xizmat turini tanlang 👇", reply_markup=markup)
            if lang == "en":
                await message.answer("Choose the type of service you need 👇", reply_markup=markup)
            if lang == "ru":
                await message.answer("Выберите нужный вам вид услуги 👇", reply_markup=markup)
            await state.set_state("get_contract_service")
        if message.text in ["Tif bojxona ro'yxati", "Tif customs list", "Тифозный таможенный список"]:
            back_key = await back_to_keyboard(lang)
            markup = await customs_keyboard(lang)
            if lang == "uz":
                await message.answer("Tif bojxona ro'yxati:", reply_markup=back_key)
                await message.answer("Kerakli bo'limni tanlang 👇", reply_markup=markup)
            if lang == "en":
                await message.answer("Tif customs list:", reply_markup=back_key)
                await message.answer("Select the desired section 👇", reply_markup=markup)
            if lang == "ru":
                await message.answer("Таможенный список брюшного тифа:", reply_markup=markup)
                await message.answer("Выберите нужный раздел 👇", reply_markup=back_key)
            await state.set_state("get_tif") 
        if message.text in ["Yuk xizmatlari", "Freight services", "Грузовые услуги"]:
            markup = await freight_keyboard(lang)
            back_key = await back_to_keyboard(lang)
            if lang == "uz":
                await message.answer(".", reply_markup=back_key)
                await message.answer("Kerakli xizmat turini tanlang 👇", reply_markup=markup)
            if lang == "en":
                await message.answer(".", reply_markup=back_key)
                await message.answer("Choose the type of service you need 👇", reply_markup=markup)
            if lang == "ru":
                await message.answer(".", reply_markup=back_key)
                await message.answer("Выберите нужный вам вид услуги 👇", reply_markup=markup)
            await state.set_state("get_freight_service")
        if message.text in ["Omborlar ro'yxati", "Warehouse list", "Список складов"]:
            back_key = await back_to_keyboard(lang)
            markup = await region_keyboard(lang)
            if lang == "uz":
                await message.answer(".", reply_markup=back_key)
                await message.answer("Kerakli viloyatni tanlang 👇", reply_markup=markup)
            if lang == "en":
                await message.answer(".", reply_markup=back_key)
                await message.answer("Select the desired region 👇", reply_markup=markup)
            if lang == "ru":
                await message.answer(".", reply_markup=back_key)
                await message.answer("Выберите нужный регион 👇", reply_markup=markup)
            await state.set_state("get_region")                                      
        if message.text in ["Eng yaqin manzillar", "Nearest addresses", "Самые близкие адреса"]:
            markup = await location_send(lang)
            if lang == "uz":
                await message.answer("Joylashuv manzilingizni jo'nating 👇", reply_markup=markup)
            if lang == "en":
                await message.answer("Please send your location address 👇", reply_markup=markup)
            if lang == "ru":
                await message.answer("Отправьте свое местоположение 👇", reply_markup=markup)
            await state.set_state("get_location")
    else:
        if lang == "uz":
            await message.answer("Firmangiz nomini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter your company name 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите название вашей компании 👇", reply_markup=back_key)
        await state.set_state("get_company_name")


@dp.callback_query_handler(state="get_tif")
async def get_tif(call: types.CallbackQuery, state: FSMContext):
    lang = await get_lang(call.from_user.id)
    command = call.data
    if command == "back":
        await call.message.delete()
        markup = await user_menu(lang)
        if lang == "uz":
            await bot.send_message(chat_id=call.from_user.id, text="Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await bot.send_message(chat_id=call.from_user.id, text="Choose the section you want 👇", reply_markup=markup)
        elif lang == "ru":
            await bot.send_message(chat_id=call.from_user.id, text="Пожалуйста, выберите нужный раздел 👇", reply_markup=markup)
        await state.set_state('get_category')
    else:
        customs = await get_one_customs(call.data)
        if lang == "uz":
            await call.message.edit_text(customs.description_uz)
        if lang == "en":
            await call.message.edit_text(customs.description_en)
        if lang == "ru":
            await call.message.edit_text(customs.description_ru)


@dp.callback_query_handler(state="get_region")
async def get_tif(call: types.CallbackQuery, state: FSMContext):
    lang = await get_lang(call.from_user.id)
    command = call.data
    if command == "back":
        await call.message.delete()
        markup = await user_menu(lang)
        if lang == "uz":
            await bot.send_message(chat_id=call.from_user.id, text="Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await bot.send_message(chat_id=call.from_user.id, text="Choose the section you want 👇", reply_markup=markup)
        elif lang == "ru":
            await bot.send_message(chat_id=call.from_user.id, text="Пожалуйста, выберите нужный раздел 👇", reply_markup=markup)
        await state.set_state('get_category')
    else:
        counts = await get_region_wearhouses(call.data)
        await state.update_data(region_id=call.data)
        text = ""
        markup = await wearhouses_keyboard(region_id=call.data, lang=lang)
        region = await get_region(call.data)
        if lang == "uz":
            text += f"{region.name_uz} viloyatida {counts} ta omborxona mavjud. Ular:"
        if lang == "en":
            text += f"There are {counts} warehouses in {region.name_en}. They are:"
        if lang == "ru":
            text += f"В регионе {region.name_ru} есть {counts} складов. Они есть:"
        await call.message.edit_text(text=text, reply_markup=markup)
        await state.set_state("get_wearhouse")


@dp.callback_query_handler(state="get_wearhouse")
async def get_tif(call: types.CallbackQuery, state: FSMContext):
    lang = await get_lang(call.from_user.id)
    command = call.data
    if command == "back":
        markup = await region_keyboard(lang)
        if lang == "uz":
            await call.message.edit_text(text="Kerakli viloyatni tanlang 👇", reply_markup=markup)
        if lang == "en":
            await call.message.edit_text(text="Select the desired region 👇", reply_markup=markup)
        if lang == "ru":
            await call.message.edit_text(text="Выберите нужный регион 👇", reply_markup=markup)
        await state.set_state("get_region") 
    else:
        await call.message.delete()
        wearhouse = await get_wearhouse(call.data)
        await bot.send_location(chat_id=call.from_user.id, longitude=wearhouse.longitude, latitude=wearhouse.latitude)
        text = ""
        if lang == "uz":
            await bot.send_message(chat_id=call.from_user.id, text=f"{wearhouse.name_uz}\n\n{wearhouse.description_uz}", reply_markup=None)
        if lang == "en":
            await bot.send_message(chat_id=call.from_user.id, text=f"{wearhouse.name_en}\n\n{wearhouse.description_en}", reply_markup=None)
        if lang == "ru":
            await bot.send_message(chat_id=call.from_user.id, text=f"{wearhouse.name_ru}\n\n{wearhouse.description_ru}", reply_markup=None)
        await state.set_state("wearhouse")


@dp.message_handler(state="wearhouse", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await user_menu(lang)
        data = await state.get_data()
        region_id = data["region_id"]
        counts = await get_region_wearhouses(region_id)
        await state.update_data(region_id=region_id)
        text = ""
        markup = await wearhouses_keyboard(region_id=region_id, lang=lang)
        region = await get_region(region_id)
        if lang == "uz":
            text += f"{region.name_uz} viloyatida {counts} ta omborxona mavjud. Ular:"
        if lang == "en":
            text += f"There are {counts} warehouses in {region.name_en}. They are:"
        if lang == "ru":
            text += f"В регионе {region.name_ru} есть {counts} складов. Они есть:"
        await message.answer(text=text, reply_markup=markup)
        await state.set_state("get_wearhouse")
                                                     

@dp.message_handler(state="get_freight_service", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await user_menu(lang)
        if lang == "uz":
            await message.answer("Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Choose the section you want 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Пожалуйста, выберите нужный раздел 👇", reply_markup=markup)
        await state.set_state('get_category')


@dp.message_handler(state="get_location", content_types=types.ContentTypes.LOCATION)
async def get_locations(message: types.Message, state: FSMContext):
    location = message.location
    lang = await get_lang(message.from_user.id)
    user_location = {"lon": location.longitude, "lat": location.latitude}
    data = await get_adresses()
    closect_wearhouse = closest(data=data, location=user_location)
    wearhouse = await get_wearhouse(closect_wearhouse['id'])
    await message.answer_location(longitude=wearhouse.longitude, latitude=wearhouse.latitude)
    if lang == "uz":
        await message.answer(text=f"{wearhouse.name_uz}\n\n{wearhouse.description_uz}")
    if lang == "en":
        await message.answer(text=f"{wearhouse.name_en}\n\n{wearhouse.description_en}")
    if lang == "ru":
        await message.answer(text=f"{wearhouse.name_ru}\n\n{wearhouse.description_ru}")


@dp.message_handler(state="get_location", content_types=types.ContentTypes.TEXT)
async def get_location(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await user_menu(lang)
        if lang == "uz":
            await message.answer("Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Choose the section you want 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Пожалуйста, выберите нужный раздел 👇", reply_markup=markup)
        await state.set_state('get_category')


@dp.message_handler(state="get_region", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await user_menu(lang)
        if lang == "uz":
            await message.answer("Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Choose the section you want 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Пожалуйста, выберите нужный раздел 👇", reply_markup=markup)
        await state.set_state('get_category')


@dp.message_handler(state="get_wearhouse", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await region_keyboard(lang)
        if lang == "uz":
            await message.answer("Kerakli viloyatni tanlang 👇", reply_markup=markup)
        if lang == "en":
            await message.answer("Select the desired region 👇", reply_markup=markup)
        if lang == "ru":
            await message.answer("Выберите нужный регион 👇", reply_markup=markup)
        await state.set_state("get_region")                                      


@dp.callback_query_handler(state="get_freight_service")
async def get_tif(call: types.CallbackQuery, state: FSMContext):
    lang = await get_lang(call.from_user.id)
    command = call.data
    if command == "back":
        await call.message.delete()
        markup = await user_menu(lang)
        if lang == "uz":
            await bot.send_message(chat_id=call.from_user.id, text="Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await bot.send_message(chat_id=call.from_user.id, text="Choose the section you want 👇", reply_markup=markup)
        elif lang == "ru":
            await bot.send_message(chat_id=call.from_user.id, text="Пожалуйста, выберите нужный раздел 👇", reply_markup=markup)
        await state.set_state('get_category')
    if command == "loader_equipment":
        markup = await loader_equipment_keyboard(lang)
        if lang == "uz":
            await call.message.edit_text(text="Iltimos xizmat turini tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await call.message.edit_text(text="Please select the type of service 👇", reply_markup=markup)
        elif lang == "ru":
            await call.message.edit_text(text="Пожалуйста, выберите тип услуги 👇", reply_markup=markup)
        await state.set_state('get_equipment_type')
    if command == "loader_service":
        text = ""
        loaders = await get_loaders()
        for loader in loaders:
            if lang == 'uz':
                text += f"Ismi <b>{loader.name_uz}</b>\n\n{loader.description_uz}"
            if lang == 'en':
                text += f"Name <b>{loader.name_en}</b>\n\n{loader.description_en}"
            if lang == 'ru':
                text += f"Имя <b>{loader.name_ru}</b>\n\n{loader.description_uz}"
        await call.message.delete()
        markup = await back_keyboard(lang)
        await bot.send_message(call.from_user.id, text=text, reply_markup=markup)
        await state.set_state("loader_service")


@dp.message_handler(state="loader_service", content_types=types.ContentTypes.TEXT)
async def loader_service(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        back_key = await back_to_keyboard(lang)
        markup = await freight_keyboard(lang)
        if lang == "uz":
            await message.answer(".", reply_markup=back_key)
            await message.answer("Kerakli xizmat turini tanlang 👇", reply_markup=markup)
        if lang == "en":
            await message.answer(".", reply_markup=back_key)
            await message.answer("Choose the type of service you need 👇", reply_markup=markup)
        if lang == "ru":
            await message.answer(".", reply_markup=back_key)
            await message.answer("Выберите нужный вам вид услуги 👇", reply_markup=markup)
        await state.set_state("get_freight_service")
    
        
@dp.callback_query_handler(state="get_equipment_type")
async def get_tif(call: types.CallbackQuery, state: FSMContext):
    lang = await get_lang(call.from_user.id)
    command = call.data
    if command == "back":
        markup = await freight_keyboard(lang)
        if lang == "uz":
            await call.message.edit_text("Kerakli xizmat turini tanlang 👇", reply_markup=markup)
        if lang == "en":
            await call.message.edit_text("Choose the type of service you need 👇", reply_markup=markup)
        if lang == "ru":
            await call.message.edit_text("Выберите нужный вам вид услуги 👇", reply_markup=markup)
        await state.set_state("get_freight_service")
    else:
        pass

@dp.message_handler(state="get_tif", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await user_menu(lang)
        if lang == "uz":
            await message.answer("Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Choose the section you want 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Пожалуйста, выберите нужный раздел 👇", reply_markup=markup)
        await state.set_state('get_category')
 
 
@dp.message_handler(state="get_contract_service", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    get_phone = await get_phone_keyboard(lang)
    if message.text in  ["Conclusion of an import/export contract", "Registration under EGISOA", "Solving contract problems", "Заключение импортно-экспортного контракта", "Регистрация в ЕГИСОА", "Решение проблем с контрактами", "Import/eksport shartnoma tuzish", "EGISOA bo'yicha ro'yxatdan o'tish", "Kontraktdagi muammolarni hal qilish"]:
        await state.update_data(contract_type=message.text)
        if lang == "uz":
            await message.answer(f"{message.text} bo'yicha sizga qanday yordam bera olamiz? 1 knopka yordamida qo'ng'iroq buyurtma qiling.👇", reply_markup=get_phone)
        if lang == "en":
            await message.answer(f"How can we help you with {message.text}? Order a call using 1 button.👇", reply_markup=get_phone)
        if lang == "ru":
            await message.answer(f"Как мы можем помочь вам с {message.text}? Заказать звонок с помощью 1 кнопки.👇", reply_markup=get_phone)
        await state.set_state("get_phone_order")


@dp.message_handler(state="get_phone_order", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await kontrakt_keyboard(lang)
        if lang == "uz":
            await message.answer("Kerakli xizmat turini tanlang 👇", reply_markup=markup)
        if lang == "en":
            await message.answer("Choose the type of service you need 👇", reply_markup=markup)
        if lang == "ru":
            await message.answer("Выберите нужный вам вид услуги 👇", reply_markup=markup)
        await state.set_state("get_contract_service")
    if message.text in ["Qo'ng'iroq buyurtma qilish", "Order a call", "Заказ звонка"]:
        data = await state.get_data()
        service = data["contract_type"]
        markup = await user_menu(lang)
        if lang == "uz":
            await message.answer(f"Siz {service} uchun qo'ng'iroq buyurtma qildingiz. Kerakli bo'limni tanlang 👇", reply_markup=markup)
        if lang == "en":
            await message.answer(f"You have booked a call for {service}. Select the desired section 👇", reply_markup=markup)
        if lang == "ru":
            await message.answer(f"Вы забронировали звонок для {service}. Выберите нужный раздел 👇", reply_markup=markup)
        await state.set_state("get_category")


@dp.message_handler(state="get_company_name", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await user_menu(lang)
        if lang == "uz":
            await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Welcome to our bot. Choose the section you want 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Добро пожаловать в наш бот. Пожалуйста, выберите нужный раздел 👇", reply_markup=markup)
        await state.set_state('get_category')
    else:
        markup = await product_categories(lang)
        user = await get_user(message.from_user.id)
        user.company = message.text
        user.save()
        if lang == "uz":
            await message.answer("Firmangiz kategoriyasini tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Select the category of your company 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Выберите категорию вашей компании 👇", reply_markup=markup)
        await state.set_state('get_product_category')


@dp.message_handler(state="get_product_category", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    back_key = await back_keyboard(lang)
    user = await get_user(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        if lang == "uz":
            await message.answer("Firmangiz nomini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter your company name 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите название вашей компании 👇", reply_markup=back_key)
        await state.set_state("get_company_name")
    else:
        category = await get_product_category_by_name(message.text)
        if category is not None:
            user.product_cateogry = category
            user.save()
            if lang == "uz":
                await message.answer("Firmangiz oylik aylanmasini kiriting 👇", reply_markup=back_key)
            if lang == "en":
                await message.answer("Enter the monthly turnover of your company 👇", reply_markup=back_key)
            if lang == "ru":
                await message.answer("Введите месячный оборот вашей компании 👇", reply_markup=back_key)
            await state.set_state("get_company_monthly")
        else:
            markup = await product_categories(lang)
            if lang == "uz":
                await message.answer("Firmangiz kategoriyasini tanlang 👇", reply_markup=markup)
            elif lang == "en":
                await message.answer("Select the category of your company 👇", reply_markup=markup)
            elif lang == "ru":
                await message.answer("Выберите категорию вашей компании 👇", reply_markup=markup)
            await state.set_state('get_product_category')
                          

@dp.message_handler(state="get_company_monthly", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    back_key = await back_keyboard(lang)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await product_categories(lang)
        if lang == "uz":
            await message.answer("Firmangiz kategoriyasini tanlang 👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Select the category of your company 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Выберите категорию вашей компании 👇", reply_markup=markup)
        await state.set_state('get_product_category')
    else:
        if message.text.isdigit():
            user = await get_user(message.from_user.id)
            user.monthly = int(message.text)
            user.full = True
            user.save()
            markup = await user_menu(lang)
            if lang == "uz":
                await message.answer("Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
            elif lang == "ru":
                await message.answer("Выберите нужный раздел👇", reply_markup=markup)
            elif lang == "en":
                await message.answer("Please select the desired section 👇", reply_markup=markup)
            await state.set_state("get_category")
        else:
            if lang == "uz":
                await message.answer("Firmangiz oylik aylanmasini raqamlarda kiriting 👇", reply_markup=back_key)
            if lang == "en":
                await message.answer("Enter the monthly turnover of your company in numbers 👇", reply_markup=back_key)
            if lang == "ru":
                await message.answer("Введите месячный оборот вашей компании в цифрах 👇", reply_markup=back_key)
            await state.set_state("get_company_monthly")


@dp.message_handler(state="import_product_name", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await user_menu(lang)
        if lang == "uz":
            await message.answer("Botimizga xush kelibsiz. Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Добро пожаловать в наш бот. Выберите нужный раздел👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Welcome to our bot. Please select the desired section 👇", reply_markup=markup)
        await state.set_state("get_category")
    else:
        await state.update_data(import_product_name=message.text)
        back_key = await back_keyboard(lang)
        if lang == "uz":
            await message.answer("Tovar tn acd kodini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter the product tn acd code 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите код продукта tn acd 👇", reply_markup=back_key)
        await state.set_state("import_product_acd")   
        
    
@dp.message_handler(state="import_product_acd", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    back_key = await back_keyboard(lang)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        if lang == "uz":
            await message.answer("Tovar nomini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter the product name 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите название продукта 👇", reply_markup=back_key)
        await state.set_state("import_product_name")   
    else:
        await state.update_data(import_product_acd=message.text)
        if lang == "uz":
            await message.answer("Import qilinayotgan davlat nomini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter the name of the exporting country 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите название страны-экспортера 👇", reply_markup=back_key)
        await state.set_state("import_country")   
        

@dp.message_handler(state="import_country", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    back_key = await back_keyboard(lang)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        if lang == "uz":
            await message.answer("Tovar tn acd kodini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter the product tn acd code 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите код продукта tn acd 👇", reply_markup=back_key)
        await state.set_state("import_product_acd")   
    else:
        markup = await user_menu(lang)
        await state.update_data(import_country=message.text)
        if lang == "uz":
            await message.answer("Tovarning import narxini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter the import price of the product 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите импортную цену товара 👇", reply_markup=back_key)
        await state.set_state("get_import_price")   


@dp.message_handler(state="get_import_price", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    back_key = await back_keyboard(lang)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        if lang == "uz":
            await message.answer("Import qilinayotgan davlat nomini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter the name of the exporting country 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите название страны-экспортера 👇", reply_markup=back_key)
        await state.set_state("import_country")
    else:
        if message.text.isdigit():
            markup = await user_menu(lang)
            if lang == "uz":
                await state.update_data(import_price=message.text)
                await message.answer("Tez orada xodimimiz siz bilan bog'lanadi. Kerakli bo'limni tanlang 👇", reply_markup=markup)
            if lang == "en":
                await message.answer("Our staff will contact you shortly. Select the desired section 👇", reply_markup=markup)
            if lang == "ru":
                await message.answer("Наши сотрудники свяжутся с вами в ближайшее время. Выберите нужный раздел 👇", reply_markup=markup)
            await state.set_state("get_category")
        else:
            if lang == "uz":
                await message.answer("Tovarning import narxini raqamlarda kiriting 👇", reply_markup=back_key)
            if lang == "en":
                await message.answer("Enter the import price of the product in numbers 👇", reply_markup=back_key)
            if lang == "ru":
                await message.answer("Введите импортную цену товара цифрами 👇", reply_markup=back_key)
            await state.set_state("get_import_price")   
            
            
@dp.message_handler(state="export_product_name", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        markup = await user_menu(lang)
        if lang == "uz":
            await message.answer("Iltimos kerakli bo'limni tanlang 👇", reply_markup=markup)
        elif lang == "ru":
            await message.answer("Выберите нужный раздел👇", reply_markup=markup)
        elif lang == "en":
            await message.answer("Please select the desired section 👇", reply_markup=markup)
        await state.set_state("get_category")
    else:
        await state.update_data(export_product_name=message.text)
        back_key = await back_keyboard(lang)
        if lang == "uz":
            await message.answer("Tovar tn acd kodini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter the product tn acd code 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите код продукта tn acd 👇", reply_markup=back_key)
        await state.set_state("export_product_acd")   


@dp.message_handler(state="export_product_acd", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    back_key = await back_keyboard(lang)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        if lang == "uz":
            await message.answer("Tovar nomini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter the product name 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите название продукта 👇", reply_markup=back_key)
        await state.set_state("export_product_name")   
    else:
        await state.update_data(export_product_acd=message.text)
        if lang == "uz":
            await message.answer("Import qilinayotgan davlat nomini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter the name of the exporting country 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите название страны-экспортера 👇", reply_markup=back_key)
        await state.set_state("export_country")   


@dp.message_handler(state="export_country", content_types=types.ContentTypes.TEXT)
async def get_service_category(message: types.Message, state: FSMContext):
    lang = await get_lang(message.from_user.id)
    back_key = await back_keyboard(lang)
    if message.text in ["⬅️ Orqaga", "⬅️ Back", "⬅️ Назад"]:
        if lang == "uz":
            await message.answer("Tovar tn acd kodini kiriting 👇", reply_markup=back_key)
        if lang == "en":
            await message.answer("Enter the product tn acd code 👇", reply_markup=back_key)
        if lang == "ru":
            await message.answer("Введите код продукта tn acd 👇", reply_markup=back_key)
        await state.set_state("export_product_acd")
    else:
        markup = await user_menu(lang)
        if lang == "uz":
            await state.update_data(export_country=message.text)
            await message.answer("Tez orada xodimimiz siz bilan bog'lanadi. Kerakli bo'limni tanlang 👇", reply_markup=markup)
        if lang == "en":
            await message.answer("Our staff will contact you shortly. Select the desired section 👇", reply_markup=markup)
        if lang == "ru":
            await message.answer("Наши сотрудники свяжутся с вами в ближайшее время. Выберите нужный раздел 👇", reply_markup=markup)
        await state.set_state("get_category")
           

