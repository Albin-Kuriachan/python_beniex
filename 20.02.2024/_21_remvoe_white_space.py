'Write a Python program to remove all whitespace characters from a string.'


def whitespace(string):
    return string.replace(" ", "")


string = input("Enter your sentence :")
print(whitespace(string))
