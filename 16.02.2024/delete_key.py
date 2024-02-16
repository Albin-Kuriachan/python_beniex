
# Write a Python program to Delete a list of keys from a dictionary

def delete_keys(dic, keys):
    not_in=[]
    for i in keys:
        if i in dic:
            del dic[i]
        else:
            not_in.append(i)

    return dic ,not_in

print()
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Original Dictionary:", dict)
key_to_delete = input("Enter the keys to delete: ")
result,not_in=delete_keys(dict, key_to_delete)

print(result)
if not_in is not None:
    print(','.join(not_in),"Not in the list ")
