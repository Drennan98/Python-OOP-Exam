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