def get_mask_card_number(card_number: str) -> str:
    """функция маскировки номера банковской карты"""

    if not card_number:
        return "None"

    if len(card_number) != 16:
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
    return mask_number


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""

    if not account_number:
        return "None"

    if len(account_number) != 20:
        raise ValueError("Некорректное число знаков")

    mask_account = "**" + account_number[-4:]
    return mask_account


print(get_mask_account("73654108430135874305"))
