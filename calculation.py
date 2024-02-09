# Addition
def addition(num1, num2):
    return num1 + num2

# Subtraction
def subtraction(num1, num2):
    return num1 - num2

# Multiplication
def multiplication(num1, num2):
    return num1 * num2

# Division
def division(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2

# Modulus
def modulus(num1, num2):
    if num2 == 0:
        return "Error: Cannot perform modulus with zero"
    return num1 % num2

# Exponentiation
def exponentiation(num1, num2):
    return num1 ** num2

# Floor Division
def floor_division(num1, num2):
    if num2 == 0:
        return "Error: Cannot perform floor division with zero"
    return num1 // num2

# Input for the function
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {addition(num1, num2)}")
print(f"Subtraction: {subtraction(num1, num2)}")
print(f"Multiplication: {multiplication(num1, num2)}")
print(f"Division: {division(num1, num2)}")
print(f"Modulus: {modulus(num1, num2)}")
print(f"Exponentiation: {exponentiation(num1, num2)}")
print(f"Floor Division: {floor_division(num1, num2)}")
