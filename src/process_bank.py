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
