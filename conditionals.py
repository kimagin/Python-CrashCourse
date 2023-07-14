# If/Else conditions are used to decide to do something based on a condition being true or false

x = 10
y = 20


# Comparision Operators (==, !=, > , < , >=, <=)

if x > y :
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equale to {y}')
else :
    print(f'{y} is greater than {x}')


# Nested if statements

if x>2 :
    if x <=10:
        print(f'{x} is greater than 2 and less than or equale to 10')


# Logical Operators (and, or, not)

if x>2 and x <=10:
    print(f'{x} is greater than 2 and less than or equale to 10')

if x>2 or x <=10:
    print(f'{x} is greater than 2 and less than or equale to 10')

if not(x==y):
    print(f'{x} is not equale to {y}')







# Membership Operators (not, not in) - Membership Operators are used to test if a sequence is presented in an object
