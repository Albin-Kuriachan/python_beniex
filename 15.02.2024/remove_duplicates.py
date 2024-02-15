
# Write a Python program to remove duplicates from a list.

def remove_dup(lst):
    result=[]
    for i in lst:
        if i not in result:
            result.append(i)
    return result




my_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_dup(my_list)
print("Result:", result)
