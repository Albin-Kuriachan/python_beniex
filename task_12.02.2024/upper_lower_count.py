
# Write a Python function that accepts a string and counts the number of upper and lower case letters.
def upper_lower_count(word):
    u = 0
    l = 0
    for i in word:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
    return u, l


words = "Hello World"
upper_count, lower_count = upper_lower_count(words)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
