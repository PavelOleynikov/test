from src.generators import filter_by_currency
from src.process_bank import process_bank_operations, process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.read_files import read_csv, read_xlsx
from src.utils import get_data_operations
from src.widget import get_date, mask_account_card


def main():
    """функция запускает пользовательский интерфейс программы"""

    print(
        """
    Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"
    """
    )

    user = int(
        input("Введите соответствующий номер: ").strip()
    )  # удаляем лишние пробелы

    if user == 1:
        print("Для обработки выбран JSON-файл.")
        transactions = get_data_operations("../data/operations.json")
    elif user == 2:
        print("Для обработки выбран CSV-файл.")
        transactions = read_csv("../data/transactions.csv")
    elif user == 3:
        print("Для обработки выбран XLSX-файл.")
        transactions = read_xlsx("../data/transactions_excel.xlsx")

    correct_status = ["EXECUTED", "CANCELED", "PENDING"]

    # сортировка по статусу операций
    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        user = input().upper().strip()  # переводим в верхний регистр и удаляем пробелы

        if user in correct_status:
            print(f'Операции отфильтрованы по статусу "{user}"')
            transactions = filter_by_state(transactions, user)
            break
        else:
            print(f"Статус операции {user} недоступен.")

    # сортировка по дате операции
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user = input().upper().strip()
        if user in ["ДА", "НЕТ"]:
            break
    if user == "ДА":
        while True:
            print("Отсортировать по возрастанию или по убыванию?")
            user = input().lower().strip()
            if user in ["по возрастанию", "по убыванию"]:
                if user == "по возрастанию":
                    transactions = sort_by_date(transactions, reverse=False)
                else:
                    transactions = sort_by_date(transactions, reverse=True)
                break

    # сортировка по валюте операции
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user = input().lower().strip()
        if user in ["да", "нет"]:
            break
    if user == "да":
        transactions = filter_by_currency(transactions, "RUB")

    # сортировка по описанию операции
    while True:
        print(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
        )
        user = input().lower().strip()
        if user in ["да", "нет"]:
            break

    if user == "да":
        print("Введите слово для фильтрации")
        user = input().strip()
        transactions = process_bank_search(transactions, user)
        counted_operations = process_bank_operations(transactions, [user])
    else:
        counted_operations = len(transactions)

    filtered_transactions = []
    for transaction in transactions:
        # маскируем номера карт и счетов для операций "from"
        if "from" in transaction and isinstance(transaction["from"], str):
            get_from = transaction["from"]
            masked_code = mask_account_card(get_from)
            transaction["from"] = masked_code
        if "to" in transaction and isinstance(transaction["to"], str):
            # маскируем номера карт и счетов для операций "to"
            get_to = transaction["to"]
            masked_code = mask_account_card(get_to)
            transaction["to"] = masked_code

        filtered_transactions.append(transaction)

    transactions = filtered_transactions
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {counted_operations}")

    # форматируем вывод информации из полученного списка
    for transaction in transactions:
        date_ = transaction.get("date")  # извлекаем дату
        date_end = get_date(date_)  # получаем дату в нужном формате

        lines = [f"{date_end} {transaction['description']}"]

        # Добавляем from -> to если есть
        if "from" in transaction:
            lines.append(f"{transaction['from']} -> {transaction.get('to', '')}")
        else:
            lines.append(f"{transaction.get('to', '')}")

        # Добавляем сумму для json
        if transactions and "operationAmount" in transaction:
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["name"]
            lines.append(f"Сумма: {amount} {currency}")
        # Добавляем сумму для csv или xlsx
        else:
            amount = transaction["amount"]
            currency = transaction["currency_code"]
            lines.append(f"Сумма: {amount} {currency}")

        print("\n".join(lines))
        print()


if __name__ == "__main__":
    main()
