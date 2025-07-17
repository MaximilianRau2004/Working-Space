def add_sprinkles(func):
    def wrapper():
        func()
        print("And sprinkles!")
    return wrapper

@add_sprinkles
def get_ice_crem():
    print("Here is your ice crem")

get_ice_crem()


try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input!")
except Exception:
    print("Something went wrong!")
finally:
    print("Goodbye!")