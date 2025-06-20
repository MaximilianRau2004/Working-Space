
fruits = ['apple', 'banana', 'cherry']
vegetables = ['carrot', 'potato', 'tomato']
meats = ['pork', 'beef', 'chicken']

groceries = [fruits, vegetables, meats, ["milk", "cheese", "bread"]]

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()

capitals = {"USA": "Washington D.C.",
            "Canada": "Ottawa",
            "Japan": "Tokyo"}

capitals.update({"Germany": "Berlin"})

print(capitals)



