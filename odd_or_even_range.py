def odd_or_even_range(start, end, even):
    print(f"All {'even' if even else 'odd'} numbers between {start} to {end}:")
    for num in range(start, end + 1):
        if even and num % 2 == 0:
            print(num, end=" ")
        elif not even and num % 2 != 0:
            print(num, end=" ")
    print()


# Taking input from the user for the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Printing odd numbers in the range
odd_or_even_range(start, end, even=False)

# Printing even numbers in the range
odd_or_even_range(start, end, even=True)


