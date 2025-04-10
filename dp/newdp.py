def fibonacci_bottom_up(n):
    if n <= 1:
        return n


    fib = [0] * n
    fib[0], fib[1] = 0, 1

    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib

n = 10  
print(fibonacci_bottom_up(n))