# Currency Converter

Конвертер валют на Python с использованием API open.er-api.com.

Программа получает актуальные курсы валют, сохраняет их в JSON-файл для кэширования и позволяет выполнять конвертацию между валютами.

## Возможности

- Получение курсов валют через API.
- Сохранение данных в `currency_rate.json`.
- Использование кэша (24 часа).
- Проверка актуальности сохраненных данных.
- Конвертация валют.
- Обработка ошибок API и сетевых ошибок.

## Используемые технологии

- Python 3
- requests
- JSON
- API open.er-api.com

## Установка

Клонировать репозиторий:

```bash
git clone <ссылка_на_репозиторий>
```

Перейти в папку проекта:

```bash
cd currency_converter
```

Создать виртуальное окружение:

```bash
python -m venv venv
```

Активировать виртуальное окружение:

Windows:

```bash
venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск программы

Запуск:

```bash
python currency.py
```

## Пример работы

```
Введите базовую валюту: USD

Используется кэш.

Базовая валюта: USD
RUB = 77.781843
EUR = 0.873482
GBP = 0.741467

Из какой валюты: EUR
В какую валюту: RUB
Введите сумму: 100

100 EUR = 8904.8020 RUB
```

## Структура проекта

```
currency_converter/
│
├── currency.py
├── currency_rate.json
├── requirements.txt
├── README.md
└── .gitignore
```

## API

Используется бесплатный API:

https://open.er-api.com/v6/latest/{currency}

Пример:

```
https://open.er-api.com/v6/latest/USD
```

## Автор

DenisZ