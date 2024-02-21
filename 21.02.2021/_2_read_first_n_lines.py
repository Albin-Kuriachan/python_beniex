"Write a Python program to read first n lines of a file. "


def raed_file(args):
    try:
        file = open(args, "r")
        lines = file.readlines()
        total_lines = len(lines)

        n = int(input(f"Enter the number less than {total_lines} to read: "))

        if n <= total_lines:
            for i in range(n):
                print(lines[i], end='')
        else:
            print(f"This document  only contain {total_lines} lines you given {n}")
        file.close()

    except FileNotFoundError:
        print(f"The file '{path}' not found")

path = input("Enter the path of the file to write the list to: ")
raed_file(path)

