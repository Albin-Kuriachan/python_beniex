"""Write a Python function that takes a list of numbers as input and returns the sum of all the numbers divisible by 3 or 5"""


def sum_num(input_list):
    result =[x for x in input_list if x % 3 == 0 or x % 5 == 0]
    if not result:
        print(f"Divisible of 3 and 5 not in the list ")
    else:
        print(f"Divisible of 3 and 5 {result} ")
        print(f"Sum is : {sum(result)} ")

try:
    input_list = [int(x) for x in input("Enter the integers (Separated by commas): ").split(",")]
    sum_num(input_list)

except ValueError:
    print('Only numbers are allowed')
