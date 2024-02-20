
'Write a Python program to implement a binary search on a sorted list'


def binary_search(args, value):
    low = 0
    high = len(args) - 1

    while low <= high:
        mid = (low + high) // 2
        if args[mid] == value:
            return mid
        elif args[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return False


input_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,20]
value = 1
index = binary_search(input_list, value)
if index !=-1:
    print(f"Found {value} at index {index}.")
else:
    print(f"{value} not found in the list.")
