import json


def get_data_operations(path: str) -> list:
    """получает данные о финансовых транзакциях из json файла"""

    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            return data
        else:
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
    except Exception:
        return []


print(get_data_operations('../data/operations.json'))
