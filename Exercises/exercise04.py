# 1. Dice rolls
import random

dice = []
for i in range(10):
    dice.append(random.randint(1, 6))

# a)
print(f'Ascending: {sorted(dice)}')

# b)
print(f'Descending: {sorted(dice, reverse=True)}')

# c)
print(f'Maximum: {max(dice)}')
print(f'Minimum: {min(dice)}')

# 2. Food menu
# a)
food = ['vegetarisk lasagne', 'spaghetti', 'fisk', 'grönsakssoppa', 'pannkakor']

# b)
weekdays = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag']

# c)
print('Bambameny')
for i in range(len(weekdays)):
    print(f'{weekdays[i]}: {food[i]}')
