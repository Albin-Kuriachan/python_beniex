"""Write a Python program to print a dictionary where the keys are numbers between 1 and 15 (both included) and
the values are the square of the keys """


def square_of_key():
    result = {}
    for i in range(1, 16):
        result[i] = i ** 2
    return result


squared_dict = square_of_key()

print(f'Square of the key form 1 to 15 : {squared_dict}')
