import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot
from data.currency import get_all_currencies
from keyboards.default.menu import markup


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    text = f"Xush kelibsiz! {name}\n\n💱 Valyuta hisoblagich Botiga xush kelibsiz.\n\nBot yordamida valyuta narxlarini bilishingiz va hisob kitob qilishingiz mumkin.\n\n"
    text += get_all_currencies()
    
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(text, reply_markup=markup)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(text, reply_markup=markup)
