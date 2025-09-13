from src.masks import get_mask_card_number, get_mask_account
from src.read_files import read_csv


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))


if __name__ == "__main__":
    print(read_csv("data/transactions.csv"))
