from typing import Any

from src.utils import get_data_operations


def test_get_data_operations_file_not_found(tmp_path: Any) -> None:
    """Тест с несуществующим файлом"""
    result = get_data_operations("non_file.json")
    assert result == []


def test_get_data_operations_empty_file(tmp_path: Any) -> None:
    """Тест с пустым списком"""

    result = get_data_operations([])
    assert result == []
