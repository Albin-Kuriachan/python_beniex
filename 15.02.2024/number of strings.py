"""Write a Python program to count the number of strings where the string length is 2 or more.
	Sample List : ['abc', 'xyz', 'aba', '1']
	Expected Result : 3
"""


def number_string(lst):
    result = 0
    for i in lst:
        if len(i) >= 2:
            result += 1

    return result


my_list = ['abc', 'xyz', 'aba', '1']
result = number_string(my_list)
print("Result:", result)
