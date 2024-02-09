
def odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Taking input from the user
try:
    num = int(input("Enter a number: "))
    odd_even(num)
except ValueError:
    print("Invalid input. Please enter an number.")
