
"""Write a Python program that simulates a banking system. Implement a class called BankAccount with methods to
initialize an account with a starting balance, withdraw funds, and handle a custom exception called NegativeBalanceError
when the account balance goes below zero."""

class NegativeBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}")
            self.display_balance()
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}")
                self.display_balance()
            else:
                raise NegativeBalanceError("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"New balance: {self.balance}")

if __name__ == "__main__":
    account = BankAccount(10000)
    try:
        account.deposit(1000)
        account.withdraw(2000)
        account.withdraw(5000)
        account.withdraw(5000)
    except NegativeBalanceError as e:
        print("Error:", e)
