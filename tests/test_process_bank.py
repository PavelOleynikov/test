import pytest

from collections import Counter

from src.process_bank import process_bank_search, process_bank_operations


def test_process_bank_search() -> None:
    """корректная обработка функции"""

    data = [{"description": "Перевод организации"}]
    search = "Перевод организации"
    assert process_bank_search(data, search) == [{"description": "Перевод организации"}]


def test_search_empty_data() -> None:
    """тест на пустой список транзакций"""

    empty_data = []
    search = "Перевод организации"

    with pytest.raises(ValueError) as e:
        process_bank_search(empty_data, search)

    assert str(e.value) == "пустой список транзакций"
    assert e.type == ValueError


def test_process_bank_operations() -> None:
    """корректная обработка функции"""

    data = [{"description": "Перевод организации"}]
    categories = ["Перевод организации"]
    result = process_bank_operations(data, categories)

    assert isinstance(result, Counter)
    assert result["Перевод организации"] == 1


def test_operations_empty_categories() -> None:
    """тест на пустой список категорий"""

    data = [{"description": "Перевод организации"}]
    categories = []

    with pytest.raises(ValueError) as e:
        process_bank_operations(data, categories)

    assert str(e.value) == "пустой список категорий"
    assert e.type == ValueError
