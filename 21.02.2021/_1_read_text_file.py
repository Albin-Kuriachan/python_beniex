"Write a Python program to read an entire text file"


def raed_file(args):
    try:
        file = open(args, "r")
        print(file.read())
        file.close()

    except FileNotFoundError:
        print(f"The file '{path}' not found")


path = input("Enter the path of the file to write the list to: ")
raed_file(path)