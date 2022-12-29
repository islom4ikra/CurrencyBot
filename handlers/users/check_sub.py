from loader import dp, bot
from aiogram import types
from data.config import CHANNELS
from utils.misc import subscription
from keyboards.default.menu import markup
from data.currency import get_all_currencies
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.callback_query_handler(text="check_sub")
async def checker(call: types.CallbackQuery):
    await call.answer("Obunalar tekshirilmoqda")
    name = call.message.from_user.full_name
    result = ""
    final_status = True
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            final_status *= status
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += (f"❌ <a href='{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lmagansiz.\n\n")

    if final_status:
        await call.message.delete()
        text = f"Xush kelibsiz! {name}\n\n💱 Valyuta hisoblagich Botiga xush kelibsiz.\n\nBot yordamida valyuta narxlarini bilishingiz va hisob kitob qilishingiz mumkin.\n\n"
        text += get_all_currencies()
        await call.message.answer(text, reply_markup=markup)
    else:
        markup_2 = InlineKeyboardMarkup()
        markup_2.add(InlineKeyboardButton(text="✔️ Obunani tekshirish", callback_data="check_sub"))
        await call.message.delete()
        await call.message.answer(result, reply_markup=markup_2, disable_web_page_preview=True)


