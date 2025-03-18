def fac(a):
    for i in range(1, a):
        a *= i
    return a

def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    return a + b

def div(a, b):
    if b == 0:
       raise ZeroDivisionError("Nur ganze Zahlen erlaubt!")
    return a / b

print(add(3, 4))
name = input("Wie heißt du? ")
print(f"Hi {name}, nice to meet you")
print(type(name))

a: int = 0
b: int = 0
print(a+b)
