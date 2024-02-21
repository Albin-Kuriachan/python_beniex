'Write a Python program to read a random line from a file'

import random

file = open("mydata.txt", "r")
lines = file.readlines()
total_lines = len(lines)
random_number=random.randint(1,total_lines-1)
print(lines[random_number])
