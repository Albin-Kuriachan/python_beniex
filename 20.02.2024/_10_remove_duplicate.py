"Write a Python program to remove duplicates from a list."


def remove_duplicates(input_list):
    new_list = []

    for i in input_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


list1 = [x for x in input("Enter the list of numbers separated by comma ,: ").split(",")]
result=remove_duplicates(list1)
print(result)