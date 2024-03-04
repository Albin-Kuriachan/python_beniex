"""Count the total number of uppercase characters in a file in Python"""


def count_uppercase(filename):
    try:
        count = 0
        with open(filename, 'r') as file:
            for i in file:
                for j in i:
                    if j.isupper():
                        count += 1

            print(f"Total number of uppercase characters in a file : {count}")
    except FileNotFoundError:
        print(f"The file '{filename}' not found")


path = input("Enter the path of the file to read:")
count_uppercase(path)
