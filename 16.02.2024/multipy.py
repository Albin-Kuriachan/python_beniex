
# Write a Python program to multiply all the items in a dictionary.

def multiply(dic):
    result =1
    for i in dic.values():
        result *= i
    return result


dict ={'a': 1, 'b': 2, 'c': 3,'d': 4}
print("Result :",multiply(dict))