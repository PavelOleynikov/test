import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_no_number():
    with pytest.raises(TypeError):
        get_mask_card_number()


def test_get_mask_card_number_incor_len():
    with pytest.raises(ValueError):
        get_mask_card_number("123456")


def test_get_mask_account_no_number():
    with pytest.raises(TypeError):
        get_mask_account()


def test_get_mask_account_incor_len():
    with pytest.raises(ValueError):
        get_mask_account("123456")
