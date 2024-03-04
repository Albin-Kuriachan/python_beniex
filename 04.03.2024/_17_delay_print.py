"""Python program to delay printing of line from a file using sleep function """

import time
def delay_print(filename,delay):
    try:
        with open(filename, 'r') as file:
            for i in file:
                print(i.strip())
                time.sleep(delay)




    except FileNotFoundError:
        print(f"The file '{filename}' not found")

path = input("Enter the path of the file to read:")
delay= int(input("Enter delay in seconds :"))
delay_print(path,delay)