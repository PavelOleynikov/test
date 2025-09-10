import csv
from typing import Any, Dict, Hashable

import pandas as pd


def read_csv(file_path: str) -> list[Dict[str, str]]:
    """Чтение csv файла и возврат списка словарей"""

    try:
        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            operations = [row for row in reader]

        if isinstance(operations, list):
            return operations
        else:
            print("файл не является списком")
            return []

    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


read_csv("./data/transactions.csv")


def read_xlsx(file_path: str) -> list[Dict[Hashable, Any]]:
    """Чтение xlsx файла и возврат списка словарей"""

    try:
        df = pd.read_excel(file_path)
        dict_list = df.to_dict(orient="records")  # преобразование df в список словарей

        if isinstance(dict_list, list):
            return dict_list
        else:
            print("файл не является списком")
            return []

    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return []

    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


read_xlsx("./data/transactions_excel.xlsx")
