import builtins
from unittest.mock import patch, mock_open

from src.read_files import read_csv, read_xlsx


def test_read_csv() -> None:
    """тест успешного чтения csv файла"""
    with patch("builtins.open", mock_open(read_data="id;state\n650703;EXECUTED")):
        assert read_csv("") == [{"id": "650703", "state": "EXECUTED"}]


@patch("pandas.read_excel")
def test_read_xlx(mock_get) -> None:
    """тест успешного открытия xlsx файла"""
    mock_get.return_value.to_dict.return_value = [{"id": "650703", "state": "EXECUTED"}]
    assert read_xlsx("") == [{"id": "650703", "state": "EXECUTED"}]
