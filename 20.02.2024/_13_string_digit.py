'Write a Python program to check if a string contains only digits.("12345" -->True)'


def digits(string):
    result = string.isdigit()
    if result:
        print(f'{string} string contains only digits')
    else:
        print(f'{string} not contains only digits')


string = input("Enter your sentence :")

digits(string)
