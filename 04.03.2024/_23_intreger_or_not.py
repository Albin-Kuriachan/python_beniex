"""The program takes input from the user and checks if whether the input value is an integer or not,
 if the input value is not an integer then the program will through a Type exception."""

def integer_or_not():
    try:
        number = input("Enter the integer value :")
        integer_value = int(number)
        print(f"{number} is an integer")

    except ValueError:
        print("Invalid input...Please enter integer value only .")

integer_or_not()





