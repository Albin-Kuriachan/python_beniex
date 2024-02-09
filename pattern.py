def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()
print()

print_pattern(4)


def print_pattern(rows):
    a=0
    for i in range(1, rows + 1):
        for j in range(rows):
            print(" ", end="")
        for k in range(i):
            print(a," ", end="")
            a+=1
        print()
print()
print_pattern(4)


def print_pattern(rows):
    a=0
    for i in range(1, rows + 1):
        for j in range(rows):
            print(" ", end="")
        for k in range(i):
            print(a," ", end="")
        print()
        a += 1


print()


print_pattern(4)


def print_pattern(rows):
    a=0
    for i in range(1, rows + 1):
        for j in range(rows):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()

print_pattern(4)

