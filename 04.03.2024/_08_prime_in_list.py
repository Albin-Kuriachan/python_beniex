"""Write a Python program that takes a list of integers as input and returns a new list with only the numbers that are prime. """


def prime_list(input_list):
    result = []
    for num in input_list:
        if num <= 1:
            pass
        else:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                result.append(num)

    if not result:
        print(f"Prime numbers not in the list ")
    else:
        print(f"Prime numbers in the list : {result}")


try:
    input_list = [int(x) for x in input("Enter the integers (Separated by commas): ").split(",")]
    prime_list(input_list)

except ValueError:
    print('Only numbers are allowed')
