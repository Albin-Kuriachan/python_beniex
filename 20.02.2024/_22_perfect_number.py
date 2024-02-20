'Write a Python program to check if a given number is a perfect number.'


def perfect_number(number):
    result = 0
    for i in range(1,number//2+1):
        if number % i == 0:
            result += i

    if result==number:
        print(f'{number} is a perfect number')
    else:
        print(f'{number} is not a perfect number')


num_input = int(input("Enter a number: "))
perfect_number(num_input)
