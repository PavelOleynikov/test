import logging
import os

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
log_file = os.path.join(log_dir, "masks.log")

logger = logging.getLogger("masks")  # создаем логер с именем модуля
logger.setLevel(logging.DEBUG)  # устанавливаем уровень логирования
file_handler = logging.FileHandler(
    log_file, mode="w", encoding="utf-8"
)  # путь записи логов
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)  # устанавливаем формат вывода логов
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """функция маскировки номера банковской карты"""

    if not card_number:
        logger.error("нет номера карты")
        return "None"

    if len(card_number) != 16:
        logger.error("Некорректное число знаков")
        raise ValueError("Некорректное число знаков")

    mask_number = (
        card_number[:4]
        + " "
        + card_number[4:6]
        + "**"
        + " "
        + "****"
        + " "
        + card_number[-4:]
    )
    logger.info("маскировка номера карты")
    return mask_number


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""

    if not account_number:
        logger.error("нет номера счета")
        return "None"

    if len(account_number) != 20:
        logger.error("Некорректное число знаков")
        raise ValueError("Некорректное число знаков")

    mask_account = "**" + account_number[-4:]
    logger.info("маскировка номера счета")
    return mask_account
