from abc import ABC, abstractmethod

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


class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    @abstractmethod
    def eat(self):
        pass

    def sleep(self):
        print(f"{self.name} is sleeping")

    def walk(self):
        print(f"{self.name} is walking")

class Pet(Animal):
    def __init__(self, owner, name, color, age):
        super().__init__(name, color, age)
        self.owner = owner

    def pet(self):
        print(f"{self.name} is being petted")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Pet):
    def bark(self):
        print(f"{self.name} is barking")

    def walk(self):
        super().walk()

class Cat(Pet):
    def meow(self):
        print(f"{self.name} is meowing")

class Hawk(Animal):
    def sleep(self):
        print(f"{self.name} is sleeping")

dog = Dog("Rex", "brown", 3, "John")
cat = Cat("Fluffy", "white", 2, "Jane")
hawk = Hawk("Bully", "black", 1)

dog.bark()
dog.walk()
dog.pet()

animals = [dog, cat, hawk]
