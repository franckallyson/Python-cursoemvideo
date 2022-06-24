a1 = int(input('Enter the first term:'))
r = int(input('Enter the reason:'))
n = 1
while n != 11:
    an = a1 + (n-1)*r
    print('{} -> '.format(an), end='')
    n += 1
print('FIM')

