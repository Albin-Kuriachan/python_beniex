
"""Write a Python program to check whether a given string is a number or not using Lambda. """

number_or_not=lambda x: x.isdigit()

string = input("Enter the Word :")
if number_or_not(string):
    print(f"{string} is a number")
else:
    print(f"{string} is not a number")