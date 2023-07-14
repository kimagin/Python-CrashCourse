# A Tuple is a collection which is ordered and unchangable. Allows duplicate members

'''
Create a Tuple
'''

fruits_a = ('Apples','Oranges','Grapes')
fruits_b = tuple(('Apples','Oranges','Grapes'))

# Remember to use a trailing comma for the single values
fruits_b = ('Apples',)

print(fruits_a[1])
# fruits[0] = 'Pears'  This will result an error as tuples are immutable

del fruits_b     # completely delete a tuple

print(len(fruits_a))  # length


# A Set is a collection which is unordered and unindexed. No duplicate allowed

'''
Create a Set
'''


fruits_set = {'Apples','Ornages','Mangos'}

# Check if is in the Set
print('Apples' in fruits_set)

# Add to Set
fruits_set.add('Grapes')
fruits_set.add('Apples') #if we add a duplicate member, it simply ignores it


# Remove from Set
fruits_set.remove('Grapes')

# Clear Set
fruits_set.clear()

# Delete Set
del fruits_set
