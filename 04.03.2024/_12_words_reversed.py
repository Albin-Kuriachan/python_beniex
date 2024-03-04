"""Write a function that takes a sentence as input and returns a new sentence with the words reversed, while keeping the order of the
words in the sentence.
"""


def reverse_words(string):
    reversed_words = []
    for i in string.split():
        reversed_words.append(i[::-1])
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence


string = "function that takes a"
print("Original sentence:", string)
print("Reversed sentence:", reverse_words(string))
