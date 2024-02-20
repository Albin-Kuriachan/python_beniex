
'Write a Python program to check if a string is an anagram of another string.("listen", "silent")'

def anagram(str1,str2):

    if sorted(str1) == sorted(str2):
        print(f'{string1} and {string2} are anagram')
    else:
        print(f'{string1} and {string2} is not anagram')


string1 = input("Enter your sentence :").lower()
string2= input("Enter your sentence :").lower()

anagram(string1,string2)
