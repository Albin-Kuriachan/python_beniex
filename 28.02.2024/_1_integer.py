"""Write a Python program that prompts the user to enter an integer and handles the ValueError exception if the user enters a non-integer value.
"""

def integer():
    user_input = input("Enter an integer value: ")

    try:
        number = int(user_input)
        print(f'{number}  is an integer')

    except ValueError:
        print(f'"{user_input}" Enter the number is not integer')

    finally:
        print('Completed')


integer()