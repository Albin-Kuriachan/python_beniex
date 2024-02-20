'Write a Python program to remove all occurrences of a given element from a list'


def remove_element(input_list,remove):
    if remove not in input_list:
        return remove," not found in the list."
    else:
        result=[x for x in input_list if x != remove]
        return result


input_list = [1, 2, 3, 4, 2, 5, 6, 2]
remove= int(input("Enter the element you want to remove :"))
output=remove_element(input_list,remove)
print(output)



