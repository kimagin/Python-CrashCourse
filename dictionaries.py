# A Dictionary is a collection which is unordered,changeable and indexed.
# No duplicate member is allowed.


'''
Create a Dictionary
'''

#directly
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

#with a constructor

person2 = dict(first_name='Sara', last_name='Williams')


'''
Interacting with Values
'''
#Get Values
print(person['first_name'])
print(person.get('last_name'))

#Add key/values
person['phone'] = '123-456789'

#Get all the keys
print(person.keys())

#Get dict items
print(person.items())


#Copy a Dictionary
person3 = person.copy() #it is similar to JS spread operator [...]
person3['city'] = 'Krakow'


#Remove an item
del(person['age'])
person.pop('phone')

#Clear the Dictionary
person.clear()

#Get length
print(len(person3))

#List of Dictionaries
people = [
    {'name':'Martha','age':30},
    {'name':'Kevin','age':25}
]

print(person, type(person))
print(person2, type(person))
print(person3, type(person))


print(people)
print(people[0]['name']) #returns Martha

