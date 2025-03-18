# list
my_list = [10, "Hallo", 3.14, True]

print(my_list[0])
print(my_list[-1])

my_list.append("Neu")
print(my_list)

my_list.remove("Hallo")
print(my_list)

for i in my_list:
    print(i)

# tuple
my_tuple = (1, 2, 3, "python")
print(my_tuple)

# my_tuple[1] = 5  # ❌ Fehler!

a, b, c, d = my_tuple
print(a, d)  # 1 Python

# set
my_set = set(my_tuple)
print(my_set)

my_set = {1, 2, 3, 3, 2, 1}
print(my_set)

my_set.add(4)
my_set.remove(1)
print(my_set)

my_set2 = {3, 4, 5}
print(my_set.union(my_set2))
print(my_set.intersection(my_set2))

# dict = HashMap
my_dict = {
    "name": "Alice",
    "age": 25,
    "place": "Berlin"
}

print(my_dict["name"])

my_dict["job"] = "Engineer"
print(my_dict)

for key, val in my_dict.items():
    print(key, ":", val)