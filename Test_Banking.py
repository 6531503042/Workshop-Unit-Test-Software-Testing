import pytest
from Account import Account
from MoneyTransfer import MoneyTransfer

class MoneyTransfer:
    def __init__(self, source, target, amount):
        self.source = source
        self.target = target
        self.amount = amount
        self.accounts = [source, target]

    def create_account(self, accountNo, balance):
        new_account = Account(accountNo, balance)
        self.accounts.append(new_account)
        return new_account

    def find_account(self, accountNo):
        for account in self.accounts:
            if account.accountNo == accountNo:
                return account
        raise Exception("Account not found")

    def update_account(self, accountNo, new_balance):
        account = self.find_account(accountNo)
        account.balance = new_balance

    def transfer_money(self, source_accountNo, target_accountNo, amount):
        source_account = self.find_account(source_accountNo)
        target_account = self.find_account(target_accountNo)
        source_account.withdraw(amount)
        target_account.deposit(amount)


class MoneyTransferTestCase(unittest.TestCase):
    def setUp(self):
        self.account1 = Account(6531503042, 1000)
        self.account2 = Account(6531503008, 500)
        self.money_transfer = MoneyTransfer(self.account1, self.account2, 300)

    def test_create_account(self):
        new_account = self.money_transfer.create_account(976531, 2000)
        self.assertIn(new_account, self.money_transfer.accounts)

    def test_find_account(self):
        found_account = self.money_transfer.find_account(6531503042)
        self.assertEqual(found_account, self.account1)

    def test_update_account(self):
        self.money_transfer.update_account(6531503008, 800)
        updated_account = self.money_transfer.find_account(6531503008)
        self.assertEqual(updated_account.balance, 800)

    def test_transfer_money(self):
        self.money_transfer.transfer_money(6531503042, 6531503008, 300)
        self.assertEqual(self.account1.balance, 700)
        self.assertEqual(self.account2.balance, 800)

if __name__ == '__main__':
    pytest.main()
