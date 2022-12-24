from aiogram import types
from loader import dp
from data.currency import get_all_currencies

@dp.message_handler(text="🔖 Valyuta kurslari", state="*")
async def main_menu(message: types.Message):
    text = get_all_currencies()
    await message.answer(text)
