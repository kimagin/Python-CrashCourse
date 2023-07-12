# A list is a collection which is ordered and changeable. Allows duplicate members.

'''
Create a list
'''

#dirctly
numbers_a = [1,3,5,6,8]
fruits = ['Apple','Ananas','Cocunouts','Pears']

#with a constructor
numbers_b = list((1,2,3,4,5))

print(numbers_a, numbers_b)

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

fruits.append('Mangos')     #append
fruits.remove('Grapes')     #remove
fruits.insert(2,'Banana')   #insert in a certain index
fruits[0] = 'Pytahaia'      #change
fruits.pop(2)               #remove from a position
fruits.reverse()            #reverse
fruits.sort()               #sort
fruits.sort(reverse=True)   #reverse sort
