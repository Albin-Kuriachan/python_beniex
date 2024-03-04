"""Write a Python function that takes a list of strings as input and returns a new list with the strings
 sorted in descending order of their lengths"""


def sotred_list(input_list):
    sorted_strings=sorted(input_list,key=len,reverse=True)
    return sorted_strings


input_list=[x for x in input("Enter the words :").split(",") ]
result=sotred_list(input_list)

print(result)