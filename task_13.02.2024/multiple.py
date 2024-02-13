"""Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number. """

import random
def multiply(x):
    unknown_number=random.randint(1,1000)
    result = x * unknown_number
    return result


argument = 10
print("Result :", multiply(argument))
