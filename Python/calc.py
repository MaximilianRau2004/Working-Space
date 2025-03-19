def fac(a):
    if not isinstance(a, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    if a < 0:
        raise ValueError("Fakultät ist nur für positive Zahlen definiert!")
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    return a + b

def sub(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    return a - b

def mul(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    return a * b

def div(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    if b == 0:
       raise ZeroDivisionError("Nur Zahlen ungleich 0 erlaubt!")
    return a / b

def mod(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    return a % b

def pow(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    c = a
    for i in range (1, b):
        a *= c
    return a

def sqrt(a):
    if not isinstance(a, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    left = 0
    right = a
    while left <= right:
        mid = (left+right) // 2
        if mid*mid == a:
            return mid
        elif mid*mid < a:
            left = mid + 1
        else:
            right = mid - 1

try:
    a = int(input("Geben Sie bitte die erste Zahl ein: "))
    sign = input("Geben Sie bitte die Operation ein (+, -, *, /, %, !, **, sqrt): ")

    if sign == "!":
        print(fac(a))
    elif sign == "sqrt":
        print(sqrt(a))
    else:
        b = int(input("Geben Sie bitte die zweite Zahl ein: "))
        if sign == "+":
            print(add(a, b))
        elif sign == "-":
            print(sub(a, b))
        elif sign == "*":
            print(mul(a, b))
        elif sign == "/":
            print(div(a, b))
        elif sign == "%":
            print(mod(a, b))
        elif sign == "**":
            print(pow(a, b))
        else:
            print("Ungültige Operation")
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

