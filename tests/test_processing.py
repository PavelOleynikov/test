import pytest

from src.processing import filter_by_state, sort_by_date

def test_filter_by_state():
    # Фильтрация по EXECUTED
    test_data_1 = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]
    result_1 = filter_by_state(test_data_1)
    assert len(result_1) == 2, "Неверное количество EXECUTED операций"

    # Фильтрация по CANCELED
    test_data_2 = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'CANCELED'}
    ]
    result_2 = filter_by_state(test_data_2, 'CANCELED')
    assert len(result_2) == 2, "Неверное количество CANCELED операций"

    # Пустой входной список
    assert filter_by_state([]) == [], "Пустой список должен возвращать пустой список"


def test_sort_by_date():
    # сортировка по убыванию
    test_data = [
        {'id': 1, 'date': '2023-01-15T12:00:00.000000'},
        {'id': 2, 'date': '2022-05-20T08:30:00.000000'},
        {'id': 3, 'date': '2023-03-10T15:45:00.000000'},
    ]
    result = sort_by_date(test_data)
    assert [x['id'] for x in result] == [3, 1, 2], "Неверная сортировка по убыванию"

    # Сортировка по возрастанию
    result = sort_by_date(test_data, reverse=False)
    assert [x['id'] for x in result] == [2, 1, 3], "Неверная сортировка по возрастанию"

    # Пустой список
    assert sort_by_date([]) == [], "Пустой список должен возвращаться без изменений"
