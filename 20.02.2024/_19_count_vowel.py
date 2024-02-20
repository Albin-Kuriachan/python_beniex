' Write a Python program to count the number of vowels in a string.'


def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count


string = input("Enter your word :")
print(f'Number of  vowels {count_vowels(string)}')
