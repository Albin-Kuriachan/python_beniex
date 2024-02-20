'Write a Python program to calculate the sum of all elements in a list recursively.'


def list_sum(args):
    if not args:
        return False
    else:
        result=args[0] + list_sum(args[1:])
        return result

num_list = [int(x) for x in input("Enter the list of numbers separated by ,: ").split(",")]
total_sum = list_sum(num_list)
print("The sum of element in the list:", total_sum)
