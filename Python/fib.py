def fib(n):
    n0 = 0
    n1 = 1
    for i in range(2, n):
        i = n0 + n1
        n0 = n1
        n1 = i
    return i

print(fib(7))
