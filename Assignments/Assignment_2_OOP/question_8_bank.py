from dataclasses import dataclass


@dataclass
class BankAccount:
    __account_id: str
    __balance: float
    transaction_list: []

    @property
    def account(self):
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
