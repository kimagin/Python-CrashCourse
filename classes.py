# NOTE:A class is like a blueprint for creating objects
# An object has properties and methods(functions)
# associated with it. Almost everything in Python is
# an object


# Create a class
class User:
    # Constructor
    # Self is like this in JS
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# Extending the class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}. My balance currently is {self.balance}'


# Initiaton of the object
Iman = User('Iman Kimiaei', "inkimiaei@gmail.com", 37)
Ida = Customer('Ida', 'Ida@gmail.com', '30')
Ida.set_balance(500)


print(type(Iman))
print(Iman.email)
print(Iman.greeting())
print(Ida.greeting())
