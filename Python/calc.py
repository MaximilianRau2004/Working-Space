
def add(a: int | float, b: int | float) -> int | float:
    return a + b

def sub(a: int | float, b: int | float) -> int | float:
    return a - b

def mul(a: int | float, b: int | float) -> int | float:
    x = a
    for i in range(b-1):
        a += x
    return a

def div(a: int | float, b: int | float) -> int | float:
    if b == 0:
        raise ZeroDivisionError("Division durch null nicht erlaubt.")

    result = 0
    while a >= b:
        a -= b
        result += 1
    return result

def mod(a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError("Division durch null nicht erlaubt.")

    return a - b * (a // b)

def pow(a: int | float, b: int | float) -> int | float:
    c = a
    for i in range (1, b):
        a *= c
    return a

def sqrt(a: int) -> int:
    if a < 0:
        raise TypeError("Nur positive Zahlen erlaubt!")
    if a == 0 or a == 1:
        return a

    left = 0
    right = a
    m = 0

    while left <= right:
        m = (right + left) // 2
        if m*m < a:
            left = m + 1
        else:
            right = m - 1
    return m



def fac(a: int) -> int:
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
            print(f"Ergebnis: {fac(a)}")
        elif sign == "sqrt":
            print(f"Ergebnis: {sqrt(a)}")
        else:
            b = int(input("Geben Sie bitte die zweite Zahl ein: "))
            match sign:
                case "+":
                    print(f"Ergebnis: {add(a, b)}")
                case "-":
                    print(f"Ergebnis: {sub(a, b)}")
                case "*":
                    print(f"Ergebnis: {mul(a, b)}")
                case "/":
                    print(f"Ergebnis: {div(a, b)}")
                case "%":
                    print(f"Ergebnis: {mod(a, b)}")
                case "**":
                    print(f"Ergebnis: {pow(a, b)}")
                case _:
                    print("Ungültige Operation")
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

calc()
