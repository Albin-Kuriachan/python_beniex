
'print the following patterns:'

"""
0
0 0
0 0 0
0 0 0 0

"""

for i in range(5):
    for j in range(i):
        print("0",end=' ')
    print()


"""
       *
     * * *
   * * * * *
 * * * * * * *
"""

print()
for i in range(4):
    for j in range(4 - i - 1):
        print(" ", end=" ")

    for k in range(2 * i + 1):
        print("*", end=" ")
    print()




"""
0
1 1
2 2 2
3 3 3 3
4 4 4 4 4
5 5 5 5 5 5
"""

print()

for i in range(6):
    for j in range(i + 1):
        print(i, end=" ")
    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

print()
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print()

"""
* * * * * *
* * * * *
* * * *
* * *
* *
*

"""

for i in range(6):
    for j in range(i,6):
        print("*",end=' ')
    print()



print()
"""
@ @ @ @ @ @ @
@ @ @ @ @ @ @
@ @ @ @ @ @ @
@ @ @ @ @ @ @
"""

for i in range(4):
    for j in range(7):
        print("@",end=" ")
    print()


    