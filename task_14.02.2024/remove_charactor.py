"""Write a Python code to remove all characters except a
Sample String : 'exercises'
Expected Result : 'eee' (Removed all characters except special character : e) """


def remove_char(s):
    result =""
    for i in s:
        if i=="e":
            result +=i

    return result


string = "exercises"
length = remove_char(string)
print(f"Result: {length}")