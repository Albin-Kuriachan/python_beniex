
# Write a Python function that calculates the factorial of a given integer. Demonstrate how to call this function with an example.
def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = int(input("Enter a number : "))
factorial_result = factorial(number)
print(f"The factorial of {number} is {factorial_result}")
