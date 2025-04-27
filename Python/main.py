
def weigthConverter():
    weigth = float(input("Enter your weigth: "))

    unit = input("Enter your unit (kg or lbs): ")

    if unit == "kg":
        weigth *= 2.205
        unit = "lbs"
        print(f"Your weigth is {round(weigth, 1)} {unit}")
    elif unit == "lbs":
        weigth /= 2.205
        unit = "kg"
        print(f"Your weigth is {round(weigth, 1)} {unit}")
    else:
        print("Invalid unit")

def tempConverter():
    unit = input("Enter your unit(C or F): ")
    temp = float(input("Enter your temperature: "))

    if unit == "C":
        temp = 9 * temp / 5 + 32
        unit = "°F"
        print(f"Your temperature is {round(temp, 1)} {unit}")
    elif unit == "F":
        temp = (temp - 32) * 5 / 9
        unit = "°C"
        print(f"Your temperature is {round(temp, 1)} {unit}")
    else:
        print("Invalid unit")

num = 5

print("Positive" if num > 0 else "Negative")


