
# Write a Python program to find palindromes in a given list of strings using Lambda.

palindromes =lambda x: x == x[::-1]

string = input("Enter the Word :")
if palindromes(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")