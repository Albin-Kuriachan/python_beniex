
' Write a Python program to flatten a nested list.([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6])'

def nested_list(input_list):
    new_list = []
    for item in input_list:
        if isinstance(item, list):
            new_list.extend(nested_list(item))
        else:
            new_list.append(item)
    return new_list

input_list = [1, [2, 3], [4, [5, 6]]]
result = nested_list(input_list)
print("Flattened list:", result)
