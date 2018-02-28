# fib()
# @param n an integer
# @return (void)
# Print Fibonacci sequence until n

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
