class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"{self.name} à {self.age}ans")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"et son salaire est de {self.salary}")


employee = Employee('alice', 24, "1450€")

employee.display_details()