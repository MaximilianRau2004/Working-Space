
def get_phone(country, area, first, last):
    return f"+{country}-{area}-{first}-{last}"

phone_num = get_phone(1, 234, 567, 890)
print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def display_name(*args):
    for arg in args:
        print(arg)

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def shipping_label(*args, **kwargs):
    print("Shipping order:")
    for arg in args:
        print(arg, end=" ")
    print()    
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=" ")

display_name("John", "Doe", "Jane", "Smith")
print_address(street="123 Fake St.", city="Detroit", state="MI", zip="54321")
shipping_label("John", "Doe", "Jane", "Smith",
               street="123 Fake St.", city="Detroit", state="MI", zip="54321" )
