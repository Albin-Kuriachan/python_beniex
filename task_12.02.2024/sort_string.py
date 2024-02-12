""" Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated
 sequence after sorting them alphabetically.
  Sample Items: green-red-yellow-black-white
  Expected Result: black-green-red-white-yellow """


def sort_string(word):
    split = word.split("-")
    sorted_split = sorted(split)
    result = "-".join(sorted_split)
    return result


words = "green-red-yellow-black-white"
result = sort_string(words)
print(f'Sample Items: {words}')
print(f'Expected Result: {result}')
