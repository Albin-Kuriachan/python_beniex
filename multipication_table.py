def multiplication_table():
    number = int(input("Enter the number : "))
    end_limit = int(input("Enter the end limit of the table: "))
    print(f"Multiplication table for {number} up to {end_limit}:")
    for i in range(1, end_limit + 1):
        print(f"{number} x {i} = {number * i}")


multiplication_table()
