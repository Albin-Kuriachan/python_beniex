
"""Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2: [0, 1]
Fibonacci series upto 5: [0, 1, 1, 2, 3]
Fibonacci series upto 6: [0, 1, 1, 2, 3, 5] """


fibonacci_series = lambda n: [0, 1] + [fibonacci_series(i)[-1] + fibonacci_series(i)[-2] for i in range(2, n)]

# Test
print(fibonacci_series(6))


n = int(input("Enter the number :"))
fibonacci_series = fibonacci_series(n)
print(f"Fibonacci series up to {n}:", fibonacci_series)
