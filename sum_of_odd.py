def sum_of_odd_numbers():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    sum_odd = 0
    num = start
    while num <= end:
        if num % 2 != 0:
            sum_odd += num
        num += 1
    print(f"The sum of odd numbers between {start} and {end} is: {sum_odd}")
sum_of_odd_numbers()
