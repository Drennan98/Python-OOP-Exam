import unittest

from bank_account import BankAccount, SavingsAccount, CurrentAccount

class TestBankAccounts(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount("A001", 1000)
        account.deposit(500)
        self.assertEqual(account.check_balance(), 1500)