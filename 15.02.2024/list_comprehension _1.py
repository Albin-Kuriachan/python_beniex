"""Use list comprehension to contruct a new list but add 6 to each item.
	list = [24,34,54,45]"""

original_list = [24, 34, 54, 45]
add_list = [num + 6 for num in original_list]

print("Result",add_list)
