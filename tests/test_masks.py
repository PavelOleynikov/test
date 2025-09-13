import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number():
    return ["7000792289606361", "700079228960", ""]


def test_get_mask_card_number_valid(card_number):
    # корректный номер карты
    masked = get_mask_card_number(card_number[0])
    assert masked == "7000 79** **** 6361"


def test_get_mask_card_number_invalid_length(card_number):
    # неправильная длина номера
    with pytest.raises(ValueError):
        get_mask_card_number(card_number[1])


def test_get_mask_card_number_empty(card_number):
    # пустая строка
    assert get_mask_card_number(card_number[2]) == "None"


@pytest.fixture
def account_number():
    return ["73654108430135874305", "7365410843013587", ""]


def test_get_mask_account_valid(account_number):
    # корректный номер счета
    masked = get_mask_account(account_number[0])
    assert masked == "**4305"


def test_get_mask_account_invalid_length(account_number):
    # неправильная длина номера
    with pytest.raises(ValueError):
        get_mask_account(account_number[1])


def test_get_mask_account_empty(account_number):
    # пустая строка
    assert get_mask_account(account_number[2]) == "None"
