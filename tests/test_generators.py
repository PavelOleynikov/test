import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions():
    return ([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ])


def test_filter_by_currency_usd_transactions(transactions):
    # тест фильтрации по usd валюте
    assert next(filter_by_currency(transactions, "USD")) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 3),
    ("RUB", 2),
    ("EUR", 0),
    ("GBP", 0),
])

def test_filter_by_currency_count(transactions, currency, expected_count):
    # Тест количества найденных транзакций по валюте
    filtered = list(filter_by_currency(transactions, currency))
    assert len(filtered) == expected_count


def test_filter_by_currency_another_currency(transactions):
    # Тест фильтрации по несуществующей валюте
    eur_transactions = list(filter_by_currency(transactions, "EUR"))

    assert len(eur_transactions) == 0
    assert eur_transactions == []


def test_filter_by_currency_empty_list():
    # Тест работы с пустым списком транзакций
    empty_transactions = []
    result = list(filter_by_currency(empty_transactions, "USD"))

    assert len(result) == 0
    assert result == []


def test_transaction_descriptions_all_transactions(transactions):
    # Тест получения всех описаний транзакций

    descriptions = list(transaction_descriptions(transactions))

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"]

    assert descriptions == expected_descriptions
    assert len(descriptions) == 5


def test_transaction_descriptions_empty_list():
    # Тест работы с пустым списком транзакций

    empty_transactions = []
    descriptions = list(transaction_descriptions(empty_transactions))

    assert descriptions == []
    assert len(descriptions) == 0


def test_card_number_generator_correct_number_card():
    # Тест на корректность номеров карт

    expected_results = [
        "0000 0000 0000 0000",
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004"
    ]

    results = list(card_number_generator(0, 5))

    assert results == expected_results


def test_card_number_generator_formatting():
    # Тест корректности форматирования номеров карт

    generator = card_number_generator(1234567812345678, 1234567812345679)
    card_number = next(generator)

    parts = card_number.split()
    assert len(parts) == 4
    assert all(len(part) == 4 for part in parts)


def test_card_number_generator_range_limits():
    # Тест обработки крайних значений диапазона

    generator = card_number_generator(0, 1)
    result = next(generator)
    assert result == "0000 0000 0000 0000"

    generator = card_number_generator(9999999999999999, 10000000000000000)
    result = next(generator)
    assert result == "9999 9999 9999 9999"

