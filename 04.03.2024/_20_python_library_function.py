"""Create a Python library with the function to input the values with expectation handling and demonstrate with the example."""


from _20_python_library import lib_fun
def main():
    age = lib_fun("Enter your age: ")
    if age:
         print(f"You age is , {age} ")


main()
