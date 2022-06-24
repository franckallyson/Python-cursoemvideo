n = int(input('Enter a Number:'))
f_total = n
print('{}! = {} X '.format(n, n), end='')
while f > 0:
    f_total *= f
    print('{}'.format(f), end='')
    print(' X ' if f > 1 else ' = ', end='')
    f -= 1
'''for f in range(n - 1, 0, -1):
    f_total *= f
    print('{}'.format(f), end='')
    print(' X ' if f > 1 else ' = ', end='')
    f -= 1'''
print('{}.'.format(f_total))
