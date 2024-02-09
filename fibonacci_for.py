def fibonacci_with_for_loop():
    fib1, fib2 = 0, 1

    print("First 10 Fibonacci numbers using for loop:")
    print(fib1)
    print(fib2)

    for _ in range(8):
        fib_next = fib1 + fib2
        print(fib_next)
        fib1, fib2 = fib2, fib_next


fibonacci_with_for_loop()
