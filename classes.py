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
        return f'My name is {self.name} and I am {self.age}. My balance is {self.balance}'


# Initiaton of the object

# Getting user inputs
name = input('What is your name :')
email = input('Your email address :')
age = input('Your age is :')

# Creating a new user
new_user = User(name, email, age)  # Class of User


# Creating a new Customer
Ida = Customer('Ida', 'Ida@gmail.com', '30')  # Extended class of Customer
Ida.set_balance(500)


print(type(new_user))
print(new_user.email)
print(new_user.greeting())
print(Ida.greeting())
