from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_admin_keyboard():
    admin_keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    get_report_btn = KeyboardButton(text="GET REPORT")
    clear_queue_btn = KeyboardButton(text='CLEAR QUEUE')
    get_length_queue_btn = KeyboardButton(text='GET LENGTH QUEUE')
    admin_keyboard_markup.add(get_report_btn)
    admin_keyboard_markup.add(clear_queue_btn)
    admin_keyboard_markup.add(get_length_queue_btn)
    return admin_keyboard_markup
