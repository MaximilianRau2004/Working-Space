
foods = []
prices = []
total = 0

while True:
    food = input("Enter food name (or q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter food price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("Your cart:")

for food in foods:
    print(food, end = " ")

for price in prices:
    total += price

print(f"\nTotal: ${total:.2f}")