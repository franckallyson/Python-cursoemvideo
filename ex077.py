nomes = ('Learn', 'Program', 'Language', 'Python', 'Course', 'Free',
         'Study', 'Practice', 'Work', 'Market', 'Programmer', 'Future')
print('List of names and their wolves:')
for nome in nomes:
    print(f'\nThe name {nome} has: ', end='')
    for letra in nome:
        if letra in 'AaEeIiOoUu':
            print(f'{letra} ', end='')

