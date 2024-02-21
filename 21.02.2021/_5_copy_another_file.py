"Write a Python program to copy the contents of a file to another file"


file = open("mydata.txt", "r")
copy_file = open("copy.txt", "w")

for i in file:
    copy_file.write(i)

print("Copy created")

copy_file = open("copy.txt", "r")
print(copy_file.read())









