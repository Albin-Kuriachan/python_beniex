"""Write a Python function that takes a list of integers as input and returns a
new list with only the numbers that are perfect squares. """


def perfect_square(input_list):
    result = []
    for i in input_list:
        if i ** .5 % 1 == 0:
            result.append(i)

    if not result:
        print(f"Perfect square are not in the list ")
    else:
        print(f"Perfect square in the list : {result}")


try:
    input_list = [int(x) for x in input("Enter the integers (Separated by commas): ").split(",")]
    perfect_square(input_list)

except ValueError:
    print('Only numbers are allowed')
