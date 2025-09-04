from src.external_api import convert_currency
from unittest.mock import patch


@patch('requests.get')
def test_convert_currency(mock_get):
    """Тест на успешную конвертацию валюты"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 8120.1736}

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }}

    result = convert_currency(transaction)
    assert result == 8120.1736


@patch('requests.get')
def test_convert_rub(mock_get):
    """Тест когда валюта в рублях"""

    mock_get.return_value = 'test_api_key'

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        }}

    result = convert_currency(transaction)
    assert result == 100
    # запроса к API не было
    mock_get.assert_not_called()
