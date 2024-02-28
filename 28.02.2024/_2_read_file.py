"""Create a program that opens a file and reads its contents. Use a try-except block to handle
 the FileNotFoundError exception and display a custom error message if the file does not exist."""


def file_reader(filename):

    try:
        with open(filename, 'r') as file:
            print(file.read())
            file.close()

    except FileNotFoundError:
        print(f"The file '{path}' not found")

path = input("Enter the path of the file to read:")
file_reader(path)