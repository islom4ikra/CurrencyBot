from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


markup = ReplyKeyboardMarkup(keyboard=
    [
        [KeyboardButton(text="USD($)"), KeyboardButton(text="RUB(₽)")],
        [KeyboardButton(text="UZS(so'm)"), KeyboardButton(text="EUR(€)")],
        [KeyboardButton(text="🔖 Valyuta kurslari")]
    ],
    resize_keyboard=True
)