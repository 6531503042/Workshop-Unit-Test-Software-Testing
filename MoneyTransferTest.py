from MoneyTransfer import MoneyTransfer
from Account import Account
import pytest

class TestMoneyTransfer:
    def setup_method(self):
        self.account1 = Account(123456, 1000)
        self.account2 = Account(789012, 500)
        self.money_transfer = MoneyTransfer(self.account1, self.account2, 300)

    def test_create_account(self):
        new_account = self.money_transfer.create_account(987654, 2000)
        assert new_account in self.money_transfer.accounts

    def test_find_account(self):
        assert self.money_transfer.find_account(999999) is None

    def test_update_account(self):
        with pytest.raises(Exception) as context:
            self.money_transfer.update_account(789012, 800)
        assert str(context.value) == "Account with number 789012 not found."

    def test_transfer_money(self):
        with pytest.raises(Exception) as context:
            self.money_transfer.transfer_money(123456, 789012, 300)
        assert str(context.value) == "One or both accounts not found."
