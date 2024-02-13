

"""Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result: 4 8 12 18 22 """

original_list = [2, 4, 6, 9, 11]
number=2
multiplies =lambda x: x * number
result = list(map(multiplies, original_list))
print("Result:",result)
