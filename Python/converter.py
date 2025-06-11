def weight_converter():
    weight = float(input("Enter your weight: "))

    unit = input("Enter your unit (kg or lbs): ")

    if unit == "kg":
        weight *= 2.205
        unit = "lbs"
        print(f"Your weight is {round(weight, 1)} {unit}")
    elif unit == "lbs":
        weight /= 2.205
        unit = "kg"
        print(f"Your weight is {round(weight, 1)} {unit}")
    else:
        print("Invalid unit")

def temp_converter():
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



