import asyncio
import os

from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.types import ChatType
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

from tools import save_results, start_checker_email
from bot.keyboards import get_admin_keyboard
from core.redis_api import redis_api

dotenv_path = ('.env')
load_dotenv(dotenv_path)

bot = Bot(token=os.getenv("TOKEN"), parse_mode='HTML')
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, storage=MemoryStorage(), loop=loop)


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, "Parse email bot ready", reply_markup=await get_admin_keyboard())


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), text="GET REPORT")
async def cancel_currency(message: types.Message):
    if save_results():
        await bot.send_document(message.chat.id, open('files/report.txt', 'rb'))


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), text="CLEAR QUEUE")
async def cancel_currency(message: types.Message):
    if redis_api.clear_db():
        await bot.send_message(message.chat.id, "Queue cleared, parsing stopped",
                               reply_markup=await get_admin_keyboard())


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), text="GET LENGTH QUEUE")
async def cancel_currency(message: types.Message):
    await message.answer(f"Tasks in the queue -> {redis_api.get_len_queue()}\n", reply_markup=await get_admin_keyboard())


@dp.message_handler(content_types=['document'])
async def add_table_file(message: types.Message):
    try:
        file_name = message.document.file_name
        type_file = file_name.split('.')[-1]

        if type_file != 'txt':
            await message.answer("This file format is not supported, supported file type -> *.txt\n",
                                 reply_markup=await get_admin_keyboard())
        elif redis_api.get_len_queue() > 0:
            await message.answer(f"Parsing is currently working, there are still emails to process\n"
                                 f"Tasks in the queue -> {redis_api.get_len_queue()}\n"
                                 f"You can stop parsing by pressing the button -> CLEAR QUEUE",
                                 reply_markup=await get_admin_keyboard())
        elif redis_api.get_len_queue() == 0:
            src = f'files/db.txt'
            await message.document.download(destination_file=src)
            await message.answer("Parsing started", reply_markup=await get_admin_keyboard())
            start_checker_email()

    except Exception as e:
        text = "Something went wrong\nError\n" + str(e)
        await bot.send_message(message.from_user.id, text, reply_markup=await get_admin_keyboard())
        print(e)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
