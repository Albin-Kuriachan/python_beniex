"""Print even length words in a string.
Sample String : ''I love coding"
Expected Result : “love, coding” """


def find_length(s):

    words = s.split(' ')
    even_words=[]

    for i in words:
        if len(i) % 2 == 0:
            even_words.append(i)

    even_words=", ".join(even_words)


    return even_words


string = "I love coding"
length = find_length(string)
print(f"Result: {length}")

