from question_8_bank import BankAccount
from question_9_transactions import Transaction


def print_balance(bank_1, bank_2):
    print(f"{bank_1.account_id} Balance: {bank_1.balance}\n{bank_2.account_id} Balance: {bank_2.balance}")


def main():
    bank_1 = BankAccount("001", 1000.50)
    bank_2 = BankAccount("002", 2000.25)
    transaction_1 = Transaction(bank_1, bank_2, 100.00)
    print_balance(bank_1, bank_2)
    transaction_2 = Transaction(bank_2, bank_1, 10500.00)
    print_balance(bank_2, bank_1)


if __name__ == "__main__":
    main()
