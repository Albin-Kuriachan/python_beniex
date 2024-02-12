
"""Define a function that accepts 2 values and return its sum, subtraction and multiplication.
Using 4 types of functions based on arguments and return type."""


# With argument with return type
def calculation(a, b):
    print("With argument with return type")

    return a + b, a - b, a * b


sum_result, subtraction_result, multiplication_result = calculation(10, 5)
print("Sum:", sum_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print()



# With argument without return type
def calculation(a, b):
    print("With argument without return type")

    sum_result = a + b
    subtraction_result = a - b
    multiplication_result = a * b

    print("Sum:", sum_result)
    print("Subtraction:", subtraction_result)
    print("Multiplication:", multiplication_result)
    print()

calculation(5, 3)



# Without argument with return type

def calculation():
    print("Without argument with return type")

    a = 4
    b = 2
    sum_result = a + b
    subtraction_result = a - b
    multiplication_result = a * b

    return sum_result, subtraction_result, multiplication_result

result = calculation()
print("Sum:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])
print()



# Without argument without return type
def calculation():
    print("Without argument without return type")

    a = 6
    b = 3
    sum_result = a + b
    subtraction_result = a - b
    multiplication_result = a * b

    print("Sum:", sum_result)
    print("Subtraction:", subtraction_result)
    print("Multiplication:", multiplication_result)


calculation()

