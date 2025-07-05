
class Car:
    def __init__(self, model, color, year, for_sale):
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale

    def __str__(self):
        return f"{self.model}, {self.color}, {self.year}, {self.for_sale}"

    def drive(self):
        print(f"driving {self.model}")

    def stop(self):
        print(f"stopped {self.model}")

    def sell(self):
        print(f"sold {self.model}")

car1 = Car("BMW", "red", 2019, True)
car2 = Car("Mercedes", "blue", 2020, False)

print(car1)

car1.drive()
car1.stop()
car1.sell()