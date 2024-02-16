
# Write a Python program to sum all the items in a dictionary.

def sum_items(dic):
    return sum(dic.values())


dict ={'a': 1, 'b': 2, 'c': 3,'d': 4, 'e': 5, 'f': 6}
print("Sum the Values :",sum_items(dict))