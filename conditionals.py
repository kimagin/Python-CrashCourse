# NOTE: If/Else conditions
# are used to decide to do something based on a condition being true or false

x = 10
y = 20


# NOTE: Comparision Operators (==, !=, > , < , >=, <=)

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equale to {y}')
else:
    print(f'{y} is greater than {x}')


# NOTE: Nested if statements

if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equale to 10')


# NOTE: Logical Operators (and, or, not)


'''
AND
'''
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equale to 10')

'''
OR
'''
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and less than or equale to 10')

'''
NOT
'''
if not (x == y):
    print(f'{x} is not equale to {y}')


# NOTE: Membership Operators (not, not in)
# Membership Operators are used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4, 5, 10]

if x in numbers:
    print(x in numbers)

if (y not in numbers):
    print(y in numbers)


# NOTE: Identity Operators (is, is not)
# Compare the objects, not if they are equale, but if they are actually
# the same object, with the same memory location:

'''
IS
'''
if x is y:
    print(x is y)

'''
IS NOT
'''
if x is not y:
    print(True)
