'Write a Python program to assess if a file is closed or not'


def file_closed(path, a=0):
    try:
        file = open(path, "r")
        print(file.read())

        if a==0:
            print(f"The file '{path}' is still open.")

        else:
            file.close()
            print(f"The file '{path}' has been closed.")

    except FileNotFoundError:
        print(f"The file '{path}' not found")
        exit(1)


path = input("Enter the path of the file: ")
file_closed(path)
close_file = int(input("Close the file , (1 for Yes, 0 for No): "))
file_closed(path, close_file)
