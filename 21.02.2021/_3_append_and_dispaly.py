"Write a Python program to append text to a file and display the text. "


def append_display(args):
    try:
        file = open(args, "a+")
        n = input(f"Enter to add to document :")
        file.write(n + "\n")
        file = open("D:\\Beinex\\sample.txt", "r")
        print(file.read())
        file.close()

    except FileNotFoundError:
        print(f"The file '{path}' not found")


path = input("Enter the path of the file to write the list to: ")
append_display(path)

