
class BankAccount:
    def __init__(self, account_id, balance):
        self.__account_id = account_id
        self.__balance = balance
        self.__transaction_list = []

    @property
    def account_id(self):
        return self.__account_id

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: float):
        if not isinstance(amount, (float, int)):
            raise TypeError('Deposit amount must be numeric')
        if amount < 0:
            return False
        else:
            self.__balance += amount
            return True

    def withdraw(self, amount):
        if not isinstance(amount, (float, int)):
            raise TypeError('Withdraw amount must be numeric')
        if amount < 0 or (self.balance - amount) < 0:
            return False
        else:
            self.__balance -= amount
            return True


def main():

    bank_1 = BankAccount("001", 2000.00, [])
    print(bank_1.deposit(1000.00))
    print(bank_1.withdraw(4000))


if __name__ == "__main__":
    main()
