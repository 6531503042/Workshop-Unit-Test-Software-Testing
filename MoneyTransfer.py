from datetime import datetime
from Account import Account

class MoneyTransfer:
    def __init__(self, source, sink, amount):
        self.transfers = []
        self.accounts = []
        self.source = source
        self.sink = sink
        self.amount = amount
        self.date = datetime.now()

        # Do transfer
        self.source.withdraw(amount)
        self.sink.deposit(amount)
        self.transfers.append(self)

    @property
    def source(self):
        return self._source

    @property
    def sink(self):
        return self._sink

    @property
    def amount(self):
        return self._amount

    @property
    def date(self):
        return self._date

    @source.setter
    def source(self, value):
        self._source = value

    @sink.setter
    def sink(self, value):
        self._sink = value

    @date.setter
    def date(self, value):
        self._date = value

    @amount.setter
    def amount(self, value):
        self._amount = value

    def create_account(self, account_number, initial_balance=0):
        account = Account(account_number, initial_balance)
        self.accounts.append(account)
        return account

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def update_account(self, account_number, new_balance):
        account = self.find_account(account_number)
        if account:
            account.balance = new_balance
        else:
            raise Exception(f"Account with number {account_number} not found.")

    def transfer_money(self, source_account_number, sink_account_number, amount):
        source = self.find_account(source_account_number)
        sink = self.find_account(sink_account_number)

        if source and sink:
            transfer = MoneyTransfer(source, sink, amount)
        else:
            raise Exception("One or both accounts not found.")