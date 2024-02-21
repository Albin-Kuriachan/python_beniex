"""Write a Python program to create a file where all letters of English alphabet are listed
 by specified number of letters on each line."""


def alphabet_list(path, letters_per_line=5):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    try:
        with open(path, 'w') as file:
            for i in range(0, len(alphabet), letters_per_line):
                line = alphabet[i:i + letters_per_line]
                file.write(line + '\n')
        print(f"The file '{path}' has been created successfully.")
        new_list = open(path, 'r')
        print(new_list.read())


    except Exception as e:
        print(f"An error occurred: {e}")


path = input("Enter the path of the file to create: ")
letters_per_line = int(input("Enter the number of letters per line: "))
alphabet_list(path, letters_per_line)
