import math

def fib(n):
    n0 = 0
    n1 = 1
    for i in range(2, n):
        i = n0 + n1
        n0 = n1
        n1 = i
    return i

print(fib(7))

list = [1,2,3,4]
for i in range(len(list)):
    print(i)


a = float(input("Enter a side a: "))
b = float(input("Enter a side b: "))

c = math.sqrt(a ** 2 + b ** 2)
print(c)

