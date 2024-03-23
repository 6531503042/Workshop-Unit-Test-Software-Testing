import unittest
from unittest.mock import patch

from Account import Account
from MoneyTransfer import MoneyTransfer


class AccountTestCase(unittest.TestCase):
    def setUp(self):
        self.account1 = Account(123456, 1000)
        self.account2 = Account(789012)


class MoneyTransferTestCase(unittest.TestCase):
    def setUp(self):
        self.account1 = Account(123456, 1000)
        self.account2 = Account(789012, 500)
        self.money_transfer = MoneyTransfer(self.account1, self.account2, 300)

    def test_create_account(self):
        new_account = self.money_transfer.create_account(987654, 2000)
        self.assertIn(new_account, self.money_transfer.accounts)

    def test_find_account(self):
        self.assertIsNone(self.money_transfer.find_account(999999))

    def test_update_account(self):
        with self.assertRaises(Exception) as context:
            self.money_transfer.update_account(789012, 800)
        self.assertEqual(str(context.exception), "Account with number 789012 not found.")

    @patch('datetime.datetime')
    def test_transfer_money(self, mock_datetime):
        with self.assertRaises(Exception) as context:
            self.money_transfer.transfer_money(123456, 789012, 300)
        self.assertEqual(str(context.exception), "One or both accounts not found.")


if __name__ == '__main__':
    unittest.main()
