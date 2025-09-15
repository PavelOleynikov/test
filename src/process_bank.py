import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """функция возвращает список операций по заданной строке поиска"""

    if not data:
        raise ValueError("пустой список транзакций")
    else:
        result_list = []
        pattern = re.compile(
            search, re.IGNORECASE
        )  # компилированный (регистронезависимый) шаблон для поиска

        for operation in data:
            description = operation.get("description", "")
            if pattern.search(description):
                result_list.append(operation)
        return result_list


# print(
#     process_bank_search(
#         [
#             {
#                 "id": 441945886,
#                 "state": "EXECUTED",
#                 "date": "2019-08-26T10:50:58.294041",
#                 "operationAmount": {
#                     "amount": "31957.58",
#                     "currency": {"name": "руб.", "code": "RUB"},
#                 },
#                 "description": "Перевод организации",
#                 "from": "Maestro 1596837868705199",
#                 "to": "Счет 64686473678894779589",
#             },
#             {
#                 "id": 594226727,
#                 "state": "CANCELED",
#                 "date": "2018-09-12T21:27:25.241689",
#                 "operationAmount": {
#                     "amount": "67314.70",
#                     "currency": {"name": "руб.", "code": "RUB"},
#                 },
#                 "description": "Перевод с карты на карту",
#                 "from": "Visa Gold 7305799447374042",
#                 "to": "Maestro 3364923093037194",
#             },
#         ],
#         "перевод о",
#     )
# )
def process_bank_operations(data: list[dict], categories: list) -> dict:
    """функция возвращает словарь с количеством операций в каждой категории"""

    if not data:
        raise ValueError("пустой список транзакций")
    elif not categories:
        raise ValueError("пустой список категорий")

    result_list = []

    for operation in data:
        description = operation.get("description", "")
        if description in categories:
            result_list.append(description)

    counted = Counter(result_list)
    return counted


# print(
#     process_bank_operations(
#         [
#             {
#                 "id": 441945886,
#                 "state": "EXECUTED",
#                 "date": "2019-08-26T10:50:58.294041",
#                 "operationAmount": {
#                     "amount": "31957.58",
#                     "currency": {"name": "руб.", "code": "RUB"},
#                 },
#                 "description": "Перевод организации",
#                 "from": "Maestro 1596837868705199",
#                 "to": "Счет 64686473678894779589",
#             },
#             {
#                 "id": 594226727,
#                 "state": "CANCELED",
#                 "date": "2018-09-12T21:27:25.241689",
#                 "operationAmount": {
#                     "amount": "67314.70",
#                     "currency": {"name": "руб.", "code": "RUB"},
#                 },
#                 "description": "Перевод с карты на карту",
#                 "from": "Visa Gold 7305799447374042",
#                 "to": "Maestro 3364923093037194",
#             },
#             {
#                 "id": 633268359,
#                 "state": "EXECUTED",
#                 "date": "2019-07-12T08:11:47.735774",
#                 "operationAmount": {
#                     "amount": "2631.44",
#                     "currency": {"name": "руб.", "code": "RUB"},
#                 },
#                 "description": "Перевод организации",
#                 "from": "Visa Gold 3589276410671603",
#                 "to": "Счет 96292138399386853355",
#             },
#         ],
#         ["Перевод организации", "Перевод с карты на карту"],
#     )
# )
