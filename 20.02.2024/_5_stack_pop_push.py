'Write a Python program to implement a stack using a list.(push and pop)'


def push():
    input_item = int(input("Enter the number to be inserted:"))
    if len(stack) == 0:
        stack.append(input_item)

    else:
        stack.insert(0, input_item)
    print(input_item, "is inserted")



def pop():
    if len(stack) == 0:
        print("List is empty")

    else:
        print(stack[0], "is deleted")
        stack.pop(0)


def display():
    if len(stack) == 0:
        print("List is empty")

    else:
        print("Element in the list")
        for i in stack:
            print(i)


stack = list()
while (1):
    print()
    str = input('Enter 1 to insert 2 to delete  3 to display and any other key to Exit: ')

    if str == '1':
        print()
        print("Push Operation")
        push()

    elif str == '2':
        print()
        print("Pop Operation")
        pop()
    elif str == '3':
        print()
        print("Display List")
        display()

    else:
        print("Exting program")
        break
