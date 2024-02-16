# Write a Python program to get dictionary keys as a list


def dic_key(dic):
    # result =[]
    # for i in dic:
    #     result.append(i)
    # return result
    return list(dic.keys())


student = {
    "name": "Anu",
    "Age": 10,
    "Class": 5
}

print('Key are :',dic_key(student))