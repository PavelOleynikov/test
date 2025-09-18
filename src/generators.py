def filter_by_currency(transactions, currency):
    """функция фильтра транзакций по валюте операции"""

    if transactions and "operationAmount" in transactions[0]:
        # Фильтрация для структуры JSON

        return [
            transaction
            for transaction in transactions
            if transaction["operationAmount"]["currency"]["code"] == currency
        ]
    else:
        # Фильтрация для структуры CSV, XLSX
        return [
            transaction
            for transaction in transactions
            if transaction["currency_code"] == currency
        ]

    # return filtered_currency

    # for transaction in filtered_currency:
    #     yield transaction


# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     next(usd_transactions)


def transaction_descriptions(transactions):
    """функция описания каждой операции"""

    for transaction in transactions:
        yield transaction["description"]


# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     next(descriptions)


def card_number_generator(start, stop):
    """генератор номеров банковских карт"""

    for number in range(start, stop):
        card_number = str(number).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"


# for card_number in card_number_generator(1, 5):
#     print(card_number)
