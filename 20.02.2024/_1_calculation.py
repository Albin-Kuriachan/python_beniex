
""" write a single program to handle the following arithmetic operations for addition, subtraction,
multiplication , division, floor division,modulus and Exponentiation.
"""
def addition(numbers):
    result = sum(numbers)
    print(f"Result of addition: {result}")


def subtraction(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result -= i
    print(f"Result of subtraction: {result}")


def multiplication(numbers):
    result = 1
    for i in numbers:
        result *= i
    print(f"Result of multiplication: {result}")


def division(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result /= i
    print(f"Result of division: {result}")


def modulus(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result %= i
    print(f"Result of modulus: {result}")


def exponentiation(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result **= i
    print(f"Result of exponentiation: {result}")


def floor(numbers):
    result = numbers[0]
    for i in numbers[1:]:
        result //= i
    print(f"Result of floor division: {result}")


print("Select From the List")
print("A for Addition")
print("B for Subtraction")
print("C for Multiplication")
print("D for Division")
print("E for Remainder")
print("F for Floor Division")
print("G for Exponentiation")

operations = {
    'A': addition,
    'B': subtraction,
    'C': multiplication,
    'D': division,
    'E': modulus,
    'F': floor,
    'G': exponentiation
}

operation = input("Enter the operation to perform ( 'A' for Addition): ").upper()

if operation in operations:
    numbers = []
    num_input = float(input("Enter a number "))
    numbers.append(num_input)
    num_input2 = float(input("Enter a number "))
    numbers.append(num_input2)

    while True:
        num_input = input("Enter a number or type '=' to finish: ")
        if num_input.lower() == '=':
            break
        try:
            num = float(num_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid input.")

    if len(numbers) < 2:
        print("Enter at least  two number .")
    else:
        operations[operation](numbers)

else:
    print(f"{operation} is not a valid operation.")



for i in range(200):
    c=(chr(i))
    print(c , end=" - ")
    print(ord(c))

