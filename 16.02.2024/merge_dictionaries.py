
# Write a Python program to merge two Python dictionaries.

def dic(dict1, dict2):
    dict1.update(dict2)
    return dict1


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print("Dictionary 1 :",dict1)
print("Dictionary 2 :",dict2)
result = dic(dict1, dict2)
print("Merged Dictionary:", result)