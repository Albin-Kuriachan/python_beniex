"""Implement a program that reads a text file and counts the occurrences of each word, ignoring case sensitivity."""


def occurrences(filename):
    count = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                for word in line.split():
                    word = word.lower()
                    count[word] = count.get(word, 0) + 1
        return count

    except FileNotFoundError:
        print(f"The file '{filename}' not found")

    finally:
        file.close()

path = input("Enter the path of the file to read:")
result = occurrences(path)

try:
    # print(f"Occurrence of each word in the file '{path}'"
    for key, value in result.items():
        print(f'{key} : {value}')
except Exception:
    pass