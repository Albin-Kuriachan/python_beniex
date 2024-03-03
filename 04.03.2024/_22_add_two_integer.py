"Write a Python program input and add two integers only and handle the exceptions"


def add_integer():
    try:
        number = input("Enter the first value :")
        number2 = input("Enter the second value :")

        if int(number) and int(number2):
            total = int(number) + int(number2)
            print(f"{total} ")

    except ValueError:
        print("Invalid input...Please enter integer value only.")


add_integer()
