from question_8_bank import BankAccount


class Transaction:
    def __init__(self, from_account: BankAccount, to_account: BankAccount, amount: float):
        self.__from_account = from_account
        self.__to_account = to_account
        self.amount = amount
        transaction_possible = self.__from_account.withdraw(amount)
        if transaction_possible:
            self.__to_account.deposit(amount)
            print(f"{amount} transfered from Bank {from_account.account} to Bank {to_account.account}")
        else:
            raise ValueError("Insufficient funds.")


def main():

    bank_1 = BankAccount("111", 1000.00, [])
    bank_2 = BankAccount("222", 2000.00, [])
    transaction_1 = Transaction(bank_1, bank_2, 1001.00)


if __name__ == "__main__":
    main()
