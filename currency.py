import json
import requests
import os
import time

FAVORITE_CURRENCIES = ["USD", "EUR", "GBP", "RUB"]


def get_currency_rates(base: str) -> dict | None:
    url = f"https://open.er-api.com/v6/latest/{base}"

    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")
        return None

    if response.status_code != 200:
        print(f"Ошибка API: {response.status_code}")
        return None

    data = response.json()

    if data.get("result") != "success":
        print("Такой валюты не существует.")
        return None

    return data

def save_to_file(data: dict, path="currency_rate.json"):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def read_from_file(path="currency_rate.json"):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def is_cache_valid(path="currency_rate.json"):
    if not os.path.exists(path):
        return False

    file_time = os.path.getmtime(path)
    current_time = time.time()

    return (current_time - file_time) < 24 * 60 * 60

def convert_currency(data: dict, from_currency: str, to_currency: str, amount: float):
    rates = data["rates"]

    if from_currency not in rates:
        print("Исходная валюта не найдена.")
        return None

    if to_currency not in rates:
        print("Целевая валюта не найдена.")
        return None

    result = amount * rates[to_currency] / rates[from_currency]

    return round(result, 4)



if __name__ == "__main__":
    base = input("Введите базовую валюту: ").upper()

    if is_cache_valid():
        data = read_from_file()

        if data and data["base_code"] == base:
            print("Используется кэш.")
        else:
            print("Кэш для другой валюты. Получаем свежие данные...")
            data = get_currency_rates(base)

            if data:
                save_to_file(data)
    else:
        print("Получаем свежие данные...")
        data = get_currency_rates(base)

        if data:
            save_to_file(data)

    if data:
        print(f"\nБазовая валюта: {data['base_code']}")
        print(f"RUB = {data['rates']['RUB']}")
        print(f"EUR = {data['rates']['EUR']}")
        print(f"GBP = {data['rates']['GBP']}")

        from_currency = input("\nИз какой валюты: ").upper()
        to_currency = input("В какую валюту: ").upper()
        amount = float(input("Введите сумму: "))

        result = convert_currency(data, from_currency, to_currency, amount)

        if result is not None:
            print(f"\n{amount:g} {from_currency} = {result:.4f} {to_currency}")