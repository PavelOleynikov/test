import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        # Тесты для карт (16 цифр)
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),
        # Тесты для счетов (20 цифр)
        ("Счет 12345678901234567890", "Счет **7890"),
        # Крайние случаи и некорректные данные
        ("JustText", "JustText"),  # Нет цифр
        ("", ""),  # Пустая строка
    ],
)
def test_mask_account_card(input_data, expected_output):
    assert mask_account_card(input_data) == expected_output


# Тесты для некорректных входных данных
@pytest.mark.parametrize(
    "invalid_input",
    [
        None,
        12345,
        ["Visa", "1234567890123456"],
        {"card": "1234567890123456"},
    ],
)
def test_non_string_input(invalid_input):
    with pytest.raises(ValueError, match="Input must be a string"):
        mask_account_card(invalid_input)


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),  # формат с временем
        ("2024-03-11", "11.03.2024"),  # Короткий формат
        ("2024-12-31T23:59:59.999999", "31.12.2024"),  # Граничная дата
    ],
)
def test_valid_dates(input_date, expected):
    assert get_date(input_date) == expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        "",  # Пустая строка
        None,  # None вместо строки
        1234567890,  # Число вместо строки
    ],
)
def test_invalid_dates(invalid_input):
    with pytest.raises(ValueError):
        get_date(invalid_input)
