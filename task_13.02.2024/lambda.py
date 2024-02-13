
"""Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
 also create a lambda function that multiplies argument x with argument y and prints the result. """

add = lambda x: x + 15
multiply = lambda x, y: x*y

number = int(input("Enter the number :"))
print("Adding 15 to", number, "results in:", add(number))

num1 = 5
num2 = 6

print("Multiplying", num1, "and", num2,":",multiply(num1, num2))
