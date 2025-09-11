import pytest

from src.decorators import log, my_function


def test_log_error_consol(capsys) -> None:  # тест на ошибку типов

    with pytest.raises(TypeError):
        my_function("1", 2)
    captured = capsys.readouterr()  # фикстура на вывод ошибки в консоль
    assert (
        "my_function error: <class 'TypeError'>. Inputs: ('1', 2), {}\n" == captured.out
    )


file_name = "testlog.txt"


@log(filename=file_name)
def test_file() -> int:
    result = my_function(1, 2)
    assert result == 3


def test_log_right_file() -> None:
    test_file()

    with open(file_name, "r", encoding="utf-8") as f:
        read_file = f.readlines()  # запись в файл построчно
        assert read_file[-1] == "test_file ok\n"
