from aiogram.dispatcher.filters.state import State, StatesGroup


class CurrencyState(StatesGroup):
    amount = State()