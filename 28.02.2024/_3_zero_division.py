
"""Write a program that calculates the division of two numbers entered by the user. Use a try-except block to
handle the ZeroDivisionError exception and display an appropriate error message if the user tries to divide by zero."""

def zero_divid():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        result = numerator / denominator
        print(f"Result of division: {result:.2f}")
    except ZeroDivisionError:
        print("Cannot divide by zero.Enter a non-zero denominator.")
    except ValueError:
        print("Invalid input. Enter valid numeric values.")

zero_divid()