def filter_by_state(list_operations: list, state='EXECUTED') -> list:
    """функция вывода списка словарей по ключу state"""

    new_list = []

    for element in list_operations:
        for value in element.values():
            if value == state:
                new_list.append(element)

    return new_list


def sort_by_date(list_operations: list, reverse=True) -> list:
    """функция сортировки списка словарей по дате"""

    return sorted(list_operations, key=lambda x: x['date'], reverse = reverse)

print(filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

print(sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))



