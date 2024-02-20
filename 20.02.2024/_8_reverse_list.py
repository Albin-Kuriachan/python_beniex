'Write a Python program to reverse a list.'



def reverse_list(args):
    print(args[::-1])

input_list = [x for x in input("Enter the list of numbers separated by comma ,: ").split(",")]
reverse_list(input_list)