'Write a Python program to find the intersection of two lists.'


def intersection(arr1, arr2):
    return [x for x in arr1 if x in arr2]


list1 = [x for x in input("Enter the list of numbers separated by comma ,: ").split(",")]
list2 = [x for x in input("Enter the list of numbers separated by comma ,: ").split(",")]

print(intersection(list1, list2))
