n = int(input('Enter a number:'))
a1 = 0
a2 = 1
total = 1
c = 3
print('0 -> 1 ->', end='')
while c <= n:
    total = a2 + a1
    a1 = a2
    a2 = total
    print(' {} ->'.format(total), end='')
    c += 1
print(' END')
