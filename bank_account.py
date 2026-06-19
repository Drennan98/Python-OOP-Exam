class BankAccount:
    """
    Parent class representing typical bank account.
    """
    def __init__(self, account_number, account_balance):
        self.__account_number = account_number
        self.__account_balance = account_balance

    def deposit(self, amount):
        """
        Adds money to the account.
        """
        self.__account_balance += amount

    def withdraw(self, amount):
        """
        Removes money from the account if that balance is available.
        """
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds.")

    def check_balance(self):
        """
        Returns the current account balance.
        """
        return self.__account_balance
    
    def get_account_number(self):
        """
        Returns the account number.
        """
        return self.__account_number
    
class SavingsAccount(BankAccount):
    """
    Represents a savings account with an interest rate.
    """
    def __init__(self, account_number, account_balance, interest_rate):
        super().__init__(account_number, account_balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        """
        Calculates the interest earned.
        """
        return self.check_balance() * self.__interest_rate
    
class CurrentAccount(BankAccount):
    """
    Represents a current acount with transction fees.
    """
    def __init__(self, account_number, account_balance, transaction_fee):
        super().__init__(account_number, account_balance)
        self.__transaction_fee = transaction_fee

    def withdraw(self, amount):
        """
        Withdraws money and applies a transaction fee.
        """
        total_amount = amount + self.__transaction_fee

        if total_amount <= self.check_balance():
            super().withdraw(total_amount)
        else:
            print("Insufficient fees.")