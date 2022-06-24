s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Enter an integer number:'))
    if n % 2 == 0:
        s += n
        cont += 1
print('You typed {} even numbers. The sum of the even values is:{}'.format(cont, s))
