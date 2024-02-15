""".Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
	lst1=[2, 4, 6, 8, 10, 12, 14]"""


original_list = [2, 4, 6, 8, 10, 12, 14]
new_list = [num ** 2 for num in original_list if num ** 2 >50]

print("Result",new_list)
