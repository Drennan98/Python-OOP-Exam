# Impirt unittest framework
import unittest

# Import classes we are testing from the bank_account.py file
from bank_account import BankAccount, SavingsAccount, CurrentAccount

class TestBankAccounts(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount("A001", 1000)
        account.deposit(500)
        self.assertEqual(account.check_balance(), 1500)

    def test_withdraw_current_account(self):
        account = CurrentAccount("C001", 1000, 2.50)
        account.withdraw(100)
        self.assertEqual(account.check_balance(), 897.50)

    def test_calculate_interest(self):
        account = SavingsAccount("S001", 1000, 0.05)
        self.assertEqual(account.calculate_interest(), 50)

# This allows the tests to run where the file is executed directly
if __name__== "__main__":
    unittest.main()