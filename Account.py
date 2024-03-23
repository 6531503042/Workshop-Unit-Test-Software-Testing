class Account:
    def __init__(self, accountNo, balance):
        self.accountNo = accountNo
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise Exception("Insufficient balance")
        self.balance -= amount

    def transfer(self, recipient, amount):
        self.withdraw(amount)
        recipient.deposit(amount)