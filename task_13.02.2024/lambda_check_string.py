

# Write a Python program to find if a given string starts with a given character using Lambda.


check = lambda string, char: string.startswith(char)

string = input("Enter the Word :")
char = input("Enter the character : ")
if check(string, char):
    print(f"The Word '{string}' starts with the character '{char}'.")
else:
    print(f"The Word '{string}' does not start with the character '{char}'.")
