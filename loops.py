# NOTE: A for loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string)

people = ['John', 'Paul', 'Sara', 'Susan', 'Jack']

'''
Simple FOR loop
'''
print('\nSimple for loop:')

for person in people:
    print(f'Current Person: {person}')

'''
BREAK
'''
print('\nBreak:')

for person in people:
    if person == 'Sara':
        break
    print(f'Current Person: {person}')

'''
CONTINUE
'''
print('\nContinue:')

for person in people:
    if person == 'Sara':
        continue
    print(f'Current Person: {person}')

'''
RANGE
'''
print('\nRange:')

for i in range(len(people)):
    print(people[i])
'''
CUSTOM RANGE
'''
print('\nCustom Range:')
for i in range(0, 11):
    print(f'Number:{i}')

'''
WHILE
'''
print('\nWhile:')
count = 0
while count <= 10:
    print(f'Count:{count}')
    count += 1
