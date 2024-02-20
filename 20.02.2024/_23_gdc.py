
'Write a Python program to count the occurrences of an element in a list.'


def count_elements(args,letter):
    count=0
    for i in args:
        if i == letter:
            count+=1

    return count



input_list= [x for x in input("Enter the list of numbers separated by comma ,: ").split(",")]
letter=input("Enter the letter to count the occurrences :")
result=count_elements(input_list,letter)
print(f'{letter} occurrences {result} times in the list')
