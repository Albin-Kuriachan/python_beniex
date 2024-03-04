"""Create a Python library with the function to input the values with expectation handling and demonstrate with the example."""

def lib_fun(age):

    try:
        return int(input(age))

    except ValueError:
        print("Integer value only allowed")

