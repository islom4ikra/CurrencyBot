from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.state import CurrencyState
from data.currency import get_currency


@dp.message_handler(state=CurrencyState.amount)
async def get_amount(message:types.Message, state: FSMContext):
    data = await state.get_data()
    currency = data.get('currency')
    amount = message.text
    response = get_currency(currency, "uzs")

    if amount.isdigit():
        amount = float(amount)
        qiymat = response.get('uzs')
        result = round(amount * qiymat, 2)
        text = f"{amount} {currency.upper()} = {result} so'm"
        await message.answer(text)
    else:
        await message.answer("Faqat son kiriting")

