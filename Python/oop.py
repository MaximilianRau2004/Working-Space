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

class Employee:
    count = 0
    total_salary = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.count += 1
        Employee.total_salary += salary

    def get_info(self):
        return f"{self.name} is a {self.position}"

    @staticmethod
    def is_valid_position(position):
        return position in ["manager", "engineer", "sales"]

    @classmethod
    def get_employee_count(cls):
        return f"Total count of employees is {cls.count}"

    @classmethod
    def get_average_salary(cls):
        if cls.count == 0:
            return 0
        else:
           return f"Average salary of employees is {cls.total_salary / cls.count }"

employee1 = Employee("John", "engineer", 5000)
employee2 = Employee("Jane", "sales", 4000)
employee3 = Employee("Bob", "manager", 6000)

print(Employee.is_valid_position("engineer"))
print(employee1.get_info())
print(Employee.get_employee_count())
print(Employee.get_average_salary())

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title}, {self.author}, {self.pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

book1 = Book("Python", "John", 100)
book2 = Book("Java", "Jane", 200)
book3 = Book("C++", "Bob", 300)

print(book1 == book2)