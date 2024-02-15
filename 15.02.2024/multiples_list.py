
# Write a Python program to multiples all the items in a list.


def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

my_list = [1,2, 3, 4, 5]
result = multiply_list(my_list)
print("Result:", result)

