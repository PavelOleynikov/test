import json
import logging

logger = logging.getLogger("utils")  # создаем логер с именем модуля
logger.setLevel(logging.DEBUG)  # устанавливаем уровень логирования
file_handler = logging.FileHandler(
    "logs/utils.log", mode="w", encoding="utf-8"
)  # путь записи логов
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)  # устанавливаем формат вывода логов
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_data_operations(file_path: str) -> list:
    """получает данные о финансовых транзакциях из json файла"""

    try:
        logger.info(f"получение данных из файла {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info("данные из json файла корректны")
            return data
        else:
            logger.error("файл не является списком")
            return []

    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"произошла ошибка {e}")
        return []
    except Exception as e:
        logger.error(f"произошла ошибка {e}")
        return []
