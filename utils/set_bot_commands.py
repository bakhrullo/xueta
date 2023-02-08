from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("menu", "Главное меню"),
        types.BotCommand("import", "Импорт"),
        types.BotCommand("export", "Экспорт"),
        types.BotCommand("contract", "Контракт"),
        types.BotCommand("customs", "Таможня"),
        types.BotCommand("cargo", "Грузы"),
        types.BotCommand("warehouse", "Склады"),
        types.BotCommand("postal", "Почта"),
        types.BotCommand("certification", "Сертификация"),
        types.BotCommand("code", "Код ТНВЭД"),
        types.BotCommand("contactus", "Связатся"),
        types.BotCommand("feedback", "Отзыв"),
        types.BotCommand("address", "Близкий адрес"),
        types.BotCommand("exchange", "Обмен валют"),
        types.BotCommand("library", "Библиотека"),
        types.BotCommand("settings", "Настройки"),
])
