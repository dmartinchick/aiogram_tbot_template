from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

#TODO: Проверить появиться ли позже пункт menu в меню телеграмм бота
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/menu - Главное меню",)
    
    await message.answer("\n".join(text))
