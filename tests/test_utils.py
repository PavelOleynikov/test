import pytest
from src.utils import get_data_operations


def test_get_data_operations_file_not_found(tmp_path):
    """Тест с несуществующим файлом"""
    result = get_data_operations("non_file.json")
    assert result == []


def test_get_data_operations_empty_file(tmp_path):
    """Тест с пустым списком"""

    result = get_data_operations([])
    assert result == []
