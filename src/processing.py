def filter_by_state(list_operations: list, state="EXECUTED") -> list:
    """функция вывода списка словарей по ключу state"""

    new_list = []

    for element in list_operations:
        for value in element.values():
            if value == state:
                new_list.append(element)

    return new_list


def sort_by_date(list_operations: list, reverse=True) -> list:
    """функция сортировки списка словарей по дате"""

    return sorted(list_operations, key=lambda x: x["date"], reverse=reverse)
