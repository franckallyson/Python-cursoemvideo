from random import randint
num = (randint(0, 9), randint(0, 9), randint(0, 9),
     randint(0, 9), randint(0, 9))
print(f'I Drew the values: ')
for n in num:
    print(f'{n} ', end='')
print(f'\nHighest value drawn: {max(num)}')
print(f'Lowest value drawn: {min(num)}')
