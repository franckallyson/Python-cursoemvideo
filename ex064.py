s = 0
qntd = 0
n = int(input('Enter a number: [999] for Stop:'))
while n != 999:
    s += n
    qntd += 1
    n = int(input('Enter a number: [999] for Stop:'))
print('The sum between the entered values was {}.'.format(s))
print('{} Values were entered.'.format(qntd))
