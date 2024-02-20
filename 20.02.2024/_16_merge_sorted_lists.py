
"Write a Python program to merge two sorted lists into a single sorted list."


def merge_lists(list1, list2):
    newlist = sorted(list1 + list2)
    return newlist

list1 = [x for x in input("Enter the list of numbers separated by comma ,: ").split(",")]
list2 = [x for x in input("Enter the list of numbers separated by comma ,: ").split(",")]

print("Sorted list:", merge_lists(list1, list2))
