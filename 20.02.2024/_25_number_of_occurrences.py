
" Write a Python program to count the number of occurrences of each element in a tuple"

def count_element(args):
    count = {}
    for i in args:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

input_tuple = (3,1, 2, 2, 3, 3, 3, 4, 4, 4,1,3)
result = count_element(input_tuple)
print("Occurrences of each element in the tuple:",result)

