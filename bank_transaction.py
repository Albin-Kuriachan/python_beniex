def withdraw(balance, amount):
    min_balance = 500
    if amount > balance:
        print("Insufficient balance.")
    elif balance - amount < min_balance:
        print(f"Your account balance is {balance - amount}. Please keep your account balance above Rs.500 to avoid charges.")
    else:
        balance -= amount
        print(f"Withdrawal successful. Balance amount: {balance}")
    return balance


# Input for the function
balance = float(input("Enter your current balance: "))
withdraw_amount = float(input("Enter the amount to withdraw: "))
balance = withdraw(balance, withdraw_amount)
