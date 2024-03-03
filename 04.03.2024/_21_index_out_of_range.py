"""".Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range."""


def list_operation(input_list, index):
    try:
        result = input_list[index]
        print(f"'{result}' is in the index number  {index} ")
    except IndexError:
        print("Index is out of range!")


my_list = [1, 2, 3, 4, 5]
index =int(input("Enther the index value to check the availability:"))
list_operation(my_list, index)

