
def fibonacci():
    fib1 =0
    fib2 = 1
    print("First 10 Fibonacci numbers:")
    print(fib1)
    print(fib2)
    count = 2
    while count < 10:
        fib_next = fib1 + fib2
        print(fib_next)
        fib1, fib2 = fib2, fib_next
        count += 1
fibonacci()
