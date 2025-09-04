import os
import requests
from dotenv import load_dotenv

load_dotenv()  # загрузка переменных из .env-файла

def convert_currency(transaction: dict) -> float:
    """функция возвращает сумму транзакции в рублях, иначе конвертирует в рубли через внешний API"""

    api_key = os.getenv('API_KEY')

    if not api_key:
        raise Exception("API_KEY не найден в переменных окружения")

    currency = transaction['operationAmount']['currency']['code']
    amount = float(transaction['operationAmount']['amount'])
    headers = {'apikey': api_key}  # Получение значения переменной API_KEY из .env-файла

    if currency == 'RUB':
        return amount

    url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}'

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f'API error: {response.status_code}')

    return float(response.json()['result'])

try:
    result = convert_currency({
      "operationAmount": {
      "amount": "100",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }})

    print(f"Результат: {result} руб.")

except Exception as e:

    print(f"Ошибка: {e}")
