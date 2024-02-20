' Write a Python program to implement a queue using a list.(enqueue and dequeue)'




def enqueue():
    input_item = int(input("Enter the number to be inserted:"))
    queue.append(input_item)
    print(input_item, "is inserted")



def dequeue():
    if len(queue) == 0:
        print("List is empty")

    else:
        print(queue[0], "is deleted")
        queue.pop(0)


def display():
    if len(queue) == 0:
        print("List is empty")

    else:
        print("Element in the list")
        for i in queue:
            print(i)


queue = list()
while (1):
    print()
    str = input('Enter 1 to insert 2 to delete  3 to display and any other key to Exit: ')

    if str == '1':
        print()
        print("Enqueue Operation")
        enqueue()

    elif str == '2':
        print()
        print("Dequeue Operation")
        dequeue()
    elif str == '3':
        print()
        print("Display List")
        display()

    else:
        print("Exting program")
        break
