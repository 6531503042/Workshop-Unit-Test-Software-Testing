from Account import Account
import pytest

class TestAccount:
    def setup_method(self):
        self.account1 = Account(123456, 1000)
        self.account2 = Account(789012, 0)  # Provide a balance value here

    def test_deposit(self):
        self.account1.deposit(500)
        assert self.account1.balance == 1500

    def test_withdraw_sufficient_balance(self):
        self.account1.withdraw(300)
        assert self.account1.balance == 700

    def test_withdraw_insufficient_balance(self):
        with pytest.raises(Exception) as context:
            self.account1.withdraw(1500)
        assert str(context.value) == "Insufficient balance"

    def test_transfer(self):
        recipient = Account(654321, 500)
        self.account1.transfer(recipient, 200)
        assert self.account1.balance == 800
        assert recipient.balance == 700
