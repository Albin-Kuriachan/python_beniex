'''Write a Python program to print the numbers of a specified listafter removing even numbers from it
	list = [24,34,53,65,78,93,23,42]'''


def remove_even(lst):
    result=[]
    for i in lst:
        if i % 2 != 0:
            result.append(i)

    return result

my_list = [24,34,53,65,78,93,23,42]
result = remove_even(my_list)
print("Result:", result)