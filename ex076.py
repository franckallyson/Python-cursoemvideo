list = ('Guaraná', 5.99, 'Coca-Cola', 10.99, 'Fanta Laranja', 6.99, 'Itubaína', 3.99)
print('~'*37)
print(f'{"P R I C E  L I S T I N G":^37}')
print('~'*37)
for pos in range(0, len(list), 2):
    print(f'{list[pos]:.<30}R${list[pos+1]:>6.2f}')
print('~'*37)