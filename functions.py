# A function is a block of code which only runs when it is called.
# In Python, we do not use curly brackets, we use indentation with
# tabs or spaces


'''
Create a function
'''

# Define the function


def sayHello(name='Sam'):
    print(f"Hello {name}!")


# Call the function
sayHello('John Doe')
sayHello()


# Return values

def getSum(num1=0, num2=0):
    total = num1+num2
    return total


sayHello('John Doe')

num = getSum(3, 4)
print(num)


# A lambda function is a small anonymous function.
# A lambda function can take any member of arguments, but can only have
# one expression. Very similar to JS arrow function.

# in JS it will be like this :
# getSumLambda = (num1,num2) => num1+num2

# Ruff gives a warning and suggests to use a def instead of a lambda
# https://beta.ruff.rs/docs/rules/lambda-assignment/
# to turn it off ignore E731 rule in pyproject.toml

def getSumLambda(num1, num2): return num1+num2


print(getSumLambda(9, 3))
