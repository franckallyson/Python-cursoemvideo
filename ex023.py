n = int(input('Enter a number: '))
U = n // 1 % 10
D = n // 10 % 10
C = n // 100 % 10
UM = n // 1000 % 10
print('Unidade: {} \nDezena: {} \nCentena: {} \nUnidade de Milhar: {}'.format(U, D, C, UM))