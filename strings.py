# Strings in Python are surrounded by either single or double quotation marks.
# Let's look at string formatting and some methods


'''
String Formatting
'''

name = 'Iman'
age = 38

# Concatenate
print('Hello, my name is '+name+' and I am ' + str(age))
# note the conversion of str, otherwise error

# Argument by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (v 3.6+)
print(f'My name is {name} and I am {age}')


s = 'hello world'

'''
String Methods
'''

print(s.capitalize())  # capitalize
print(s.upper())  # uppercase
print(s.lower())  # lowwercase
print(s.swapcase())  # swapcase
print(len(s))  # get length
print(s.replace('world', 'everyone'))
print(s.count('h'))  # count number of occurance
print(s.startswith('h'))  # true or false
print(s.endswith('d'))  # -----"-------
print(s.split())  # splits into a list
print(s.find('r'))  # returns index of substring

# These tree will return false because of the Space
print(s.isalnum())  # true if it is Alphanumeric
print(s.isalpha())  # true if it is Alphabetic
print(s.isnumeric())  # true if it is Numeric
