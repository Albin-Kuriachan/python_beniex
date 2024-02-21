"Write a Python program to read a file line by line store it into a variable."


"Write a Python program to read a file line by line store it into a variable."


def read_line_line(args):
    try:
        file = open(args, "r")
        for i in file:
            data=file.readlines()
            print(data)
        file.close()
    except FileNotFoundError:
        print(f"The file '{path}' not found")


path = input("Enter the path of the file to write the list to: ")
read_line_line(path)
