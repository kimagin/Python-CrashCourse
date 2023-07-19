# A variable is a container for a value, which can be of various types

'''
this is a multiline comment
or docstring (used to define a function)
can be a single or double quotes
'''

"""
VARIABLE RULES:
    - Variable names are case sensitive
    - Must start with a letter or an underscore
    - Can have numbers but can not start with one
"""

x = 1  # int
y = 2.5  # float
name = "John"  # string
is_open = True  # boolean / must start with a capital letter

# Multiple assignment
x, y, name, is_open = (1, 2.5, 'John', True)

# Basic math
a = x + y

print('Hello World!')
print(x, y, name, is_open, a)

# Casting
x = str(x)
y = int(y)
z = float(y)

# Checking types
print(type(z), z)
