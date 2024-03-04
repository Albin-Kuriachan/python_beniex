"""Write a function that takes a list of numbers as input and returns the second-largest number."""


def second_largest_number(input_list):
    try:
        largest = float('-inf')
        second = float('-inf')
        for i in input_list:

            if i > largest:
                second = largest
                largest = i

            elif i > second and i != largest:
                second = i
        print(f'Second largest in the list is {second}')
    except Exception as e:
        print("An error occurred:", e)


try:
    input_list = [int(x) for x in input("Enter the integers (Separated by commas): ").split(",")]
    if len(input_list) >= 2:
        second_largest_number(input_list)

    else:
        print("Input  at least 2 numbers.")

except ValueError:
    print('Only numbers are allowed')
