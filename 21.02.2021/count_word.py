

"""Write a Python program that takes a text file as input and returns the number of words of a given text file.
Note: Some words can be separated by a comma with no space. """


def word_count(path):
    try:
        with open(path, 'r') as file:
            text = file.read()
            text = text.replace(',', ' ')
            words = text.split()
            word_count = len(words)
            print(f"The number of words in the file '{path}' is: {word_count}")
    except FileNotFoundError:
        print(f"The file '{path}' does not exist.")
    
path = input("Enter the path of the text file: ")
word_count(path)
