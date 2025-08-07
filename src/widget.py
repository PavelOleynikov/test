from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """функция маскировки номера банковской карты или счета"""

    list_account_card = account_card.split()  # делим строку в список
    new_list = []

    for el in list_account_card:
        if el.isalpha():
            new_list.append(el)
        elif len(el) == 20:
            new_list.append(get_mask_account(list_account_card[-1]))
        else:
            new_list.append(get_mask_card_number(list_account_card[-1]))
    return " ".join(new_list)  # соединяем список в строку


print(mask_account_card("Maestro 1596837868705199"))


def get_date(date: str) -> str:
    """функция извлечения даты"""

    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
