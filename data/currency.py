import requests


def get_currency(cur1, cur2):

    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{cur1}/{cur2}.json"

    response = requests.get(url).json()

    return response


def get_all_currencies():
    rub = get_currency("rub", "uzs")['uzs']
    usd = get_currency("usd", "uzs")['uzs']
    eur = get_currency("eur", "uzs")['uzs']
    text = f"🇷🇺 1 Rossiya Rubl = 🇺🇿 {round(rub, 2)} so'm\n🇺🇸 1 AQSH Dollar = 🇺🇿 {round(usd,2)} so'm\n🇪🇺 1 EURO = 🇺🇿 {round(eur, 2)} so'm\n"
    return text
