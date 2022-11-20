"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile

API_TOKEN = ""

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    keyboard_list = [
        [types.KeyboardButton('Profile'), types.KeyboardButton(text='Документ')],
        [types.KeyboardButton('Search'), types.KeyboardButton('Support')],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard_list)

    await message.reply("Welcome to the Menu!", reply=False)
    await message.reply("Choose the button:", reply_markup=keyboard, reply=False)


@dp.message_handler(lambda message: message.text == 'Документ')
async def document_button(message: types.Message):
    # 1
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Продать/Купить товар', callback_data='Retail')
    button2 = types.InlineKeyboardButton(text='Сдать/взять в аренду', callback_data='Lease')
    button3 = types.InlineKeyboardButton(text='Выполнение работ', callback_data='Agreement')
    button4 = types.InlineKeyboardButton(text='⬅Назад', callback_data='Menu')
    button5 = types.InlineKeyboardButton(text='ℹМеню', callback_data='Menu')

    keyboard.row(button1)
    keyboard.row(button2)
    keyboard.row(button3)
    keyboard.row(button4)
    keyboard.insert(button5)

    await message.reply("Выберите документ:", reply_markup=keyboard, reply=False)


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Lease')
async def update_lease(callback_query: types.CallbackQuery):
    # 1.1
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Возмездное оказание услуги', callback_data='L1')
    button2 = types.InlineKeyboardButton(text='Доверительное управление', callback_data='L2')
    button3 = types.InlineKeyboardButton(text='Заём/кредит', callback_data='L3')
    button4 = types.InlineKeyboardButton(text='Поручение', callback_data='L4')
    button5 = types.InlineKeyboardButton(text='Перевозка', callback_data='L5')
    button6 = types.InlineKeyboardButton(text='Хранение', callback_data='L6')
    button7 = types.InlineKeyboardButton(text='Подряд', callback_data='L7')
    button8 = types.InlineKeyboardButton(text='⬅Назад', callback_data='DBack')
    button9 = types.InlineKeyboardButton(text='ℹМеню', callback_data='Menu')

    keyboard.row(button1)
    keyboard.row(button2)
    keyboard.row(button3)

    keyboard.row(button4)
    keyboard.insert(button5)

    keyboard.row(button6)
    keyboard.insert(button7)

    keyboard.row(button8)
    keyboard.insert(button9)

    await callback_query.message.edit_text('Выберите договор:', reply_markup=keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Agreement')
async def update_agreement(callback_query: types.CallbackQuery):
    # 1.1
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Договор ренты', callback_data='A1')
    button2 = types.InlineKeyboardButton(text='Договор аренды', callback_data='A2')
    button3 = types.InlineKeyboardButton(text='Договор поручения', callback_data='A3')
    button8 = types.InlineKeyboardButton(text='⬅Назад', callback_data='DBack')
    button9 = types.InlineKeyboardButton(text='ℹМеню', callback_data='Menu')

    keyboard.row(button1)
    keyboard.row(button2)
    keyboard.row(button3)

    keyboard.row(button8)
    keyboard.insert(button9)

    await callback_query.message.edit_text('Выберите договор:', reply_markup=keyboard)


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'DBack')
async def goto_document(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await document_button(callback_query.message)


# MENU
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'Menu')
async def goto_menu(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await send_welcome(callback_query.message)


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'L7')
async def update_db(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer_document(
        InputFile("doc1.pdf"),
    )


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'L6')
async def send_hello(message: types.Message):
    await message.reply("Введите имя и фамилию", reply=False)



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


# OlD FUNCTIONALITY TESTS:
# @dp.message_handler(commands=['hello'])
# async def send_hello(message: types.Message):
#     keyboard = types.InlineKeyboardMarkup()
#     button = types.InlineKeyboardButton(text='Jason', callback_data='Jasoon')
#     keyboard.insert(button)
#
#     await message.reply("Hello!\nMy name is Alexander_sleep_bot!", reply_markup=keyboard)
#
#
# @dp.callback_query_handler(lambda callback_query: callback_query.data == 'Jasoon')
# async def update_db(callback_query: types.CallbackQuery):
#     await callback_query.message.reply('Okay')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

