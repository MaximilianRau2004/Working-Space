import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
time = datetime.time(hour=23, minute=59, second=59)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%y")

target_datetime = datetime.datetime(2026, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if current_datetime < target_datetime:
    print("Target date is in the future")
else:
    print("Target date is in the past")

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