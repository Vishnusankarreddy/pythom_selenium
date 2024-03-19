# Python object and classes
"""class ClassName:
  # Statement"""


# Defining a class in python
# Creating an Object in python
# Constructors in python.


# Defining a class in python
class student:
    name = "Ram"
    rank = 1
    def show(self):
        print(self.name)
        print(self.rank)


# Creating an Object in python
Student1 = student()
print(Student1.rank)
Student1.show()


# Constructors in python.
class Car:
    def __init__(self, name, price):  # Corrected spelling from __int__ to __init__
        self.name = name
        self.price = price

    def show(self):
        print(self.name)
        print(self.price)

bmw = Car("bmw",100000)
bmw.show()
benz = Car("benz", 200000)
benz.show()


