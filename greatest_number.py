
def greatest_number(num1, num2, num3):
    if num1 == num2 == num3:
        print("equal")
    else:
        max_num = max(num1, num2, num3)
        print("Greatest of the three numbers:", max_num)


# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calling the function
greatest_number(num1, num2, num3)
