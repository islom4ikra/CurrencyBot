from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.state import CurrencyState


@dp.message_handler(text="USD($)", state="*")
async def get_usd(message: types.Message, state: FSMContext):
    await state.update_data({
        "currency": "usd"
    })
    text = "🇺🇸 Hisoblamoqchi boʻlgan AQSH dollorini  kiriting.\n\nMasalan: 100"
    await message.answer(text)
    await CurrencyState.amount.set()

@dp.message_handler(text="RUB(₽)", state="*")
async def get_usd(message: types.Message, state: FSMContext):
    await state.update_data({
        "currency": "rub"
    })
    text = "🇷🇺 Hisoblamoqchi boʻlgan Rossiya Rublini kiriting.\n\nMasalan: 100"
    await message.answer(text)
    await CurrencyState.amount.set()

@dp.message_handler(text="UZS(so'm)", state="*")
async def get_usd(message: types.Message, state: FSMContext):
    await state.update_data({
        "currency": "uzs"
    })
    text = "🇺🇿 Hisoblamoqchi boʻlgan Oʻzbek soʻmini kiriting.\n\nMasalan: 100"
    await message.answer(text)
    await CurrencyState.amount.set()

@dp.message_handler(text="EUR(€)", state="*")
async def get_usd(message: types.Message, state: FSMContext):
    await state.update_data({
        "currency": "eur"
    })
    text = "🇪🇺 Hisoblamoqchi boʻlgan EUROni kiriting.\n\nMasalan: 100"
    await message.answer(text)
    await CurrencyState.amount.set()
