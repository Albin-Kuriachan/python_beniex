"""Write a Python program to find the repeated items of a tuple"""



def repated_item(tup):
    result=[]
    for i in tup:
        if tup.count(i) > 1 and i not in result:
            result.append(i)

    return result

tup = (1,2, 3, 4, 5,1,2, 3, 4, 5,5,6,7,8)
result = repated_item(tup)
print("Result:", result)


