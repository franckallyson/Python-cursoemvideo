n = int(input('Enter a number:'))
c = 1
print('-'*15)
while c <= 10:
    print('{} X {:2} = {:2}'.format(n, c, (n*c)))
    c = c + 1
else:
    print('-'*15)



