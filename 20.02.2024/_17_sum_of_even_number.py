"Write a Python program to find the sum of all even numbers in a list."


def sum_even(input_list):
    total = 0
    for i in input_list:
        if i % 2 == 0:
            total += i
    return total


num_list = [int(x) for x in input("Enter the list of numbers separated by ,: ").split(",")]
print("Sum of even numbers:", sum_even(num_list))
