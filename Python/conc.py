

menu = {"pizza": 3.00,
        "burger": 2.00,
        "fries": 1.00,
        "chips": 2.00,
        "soda": 1.50}

cart = []
total = 0

print("-----MENU-----")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("--------------")

while True:
    food = input("Enter item name (or q to quit): ")
    if food.lower() == "q":
        break
    elif food in menu:
        cart.append(food)
        total += menu.get(food)

print("--YOUR ORDER--")
for item in cart:
    print(item, end= " ")
print()
print(f"Total: ${total:.2f}")
