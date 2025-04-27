
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Nur Zahlen erlaubt!")
    return a + b

def sub(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Nur Zahlen erlaubt!")
    return a - b

def mul(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Nur Zahlen erlaubt!")
    x = a
    for i in range(b-1):
        a += x
    return a

def div(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Nur Zahlen erlaubt!")
    if b == 0:
        raise ZeroDivisionError("Division durch null nicht erlaubt.")

    result = 0
    while a >= b:
        a -= b
        result += 1
    return result

def mod(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    if b == 0:
        raise ZeroDivisionError("Division durch null nicht erlaubt.")

    negative = a < 0

    a = abs(a)
    b = abs(b)

    while a >= b:
        a -= b

    if negative:
        a *= -1

    return a

def pow(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Nur Zahlen erlaubt!")
    c = a
    for i in range (1, b):
        a *= c
    return a

def sqrt(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Nur Zahlen erlaubt!")
    if a < 0:
        raise TypeError("Nur positive Zahlen erlaubt!")
    if a == 0 or a == 1:
        return a

    left = 0
    right = a
    if a < 1:
        right = 1

    while left < right:
        m = (right + left) / 2
        if m*m < a:
            left = m + 1
        else:
            right = m - 1
        return (right + left) / 2

def fac(a):
    if not isinstance(a, int):
        raise TypeError("Nur ganze Zahlen erlaubt!")
    if a < 0:
        raise ValueError("Fakultät ist nur für positive Zahlen definiert!")
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

def calc():
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

