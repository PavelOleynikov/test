import csv
from typing import Any, Dict, Hashable

import pandas as pd


def read_csv(file_path: str) -> list[Dict[str, str]]:
    """Чтение csv файла и возврат списка словарей"""

    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")

        operations = [row for row in reader]

    return operations


def read_xlsx(file_path: str) -> list[Dict[Hashable, Any]]:
    """Чтение xlsx файла и возврат списка словарей"""

    df = pd.read_excel(file_path)
    dict_list = df.to_dict(orient="records")  # преобразование df в список словарей

    return dict_list
