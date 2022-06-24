s = 0
qntd = 0
ans = 'S'
biggest = 0
smaller = 0
while ans == 'S':
    n = int(input('Enter a number:'))
    s += n
    qntd += 1
    if qntd == 1:
        biggest = smaller = n
    else:
        if biggest < n:
            biggest = n
        if smaller > n:
            smaller = n
    ans = str(input('Do you want continue? [S/N]')).upper().strip()[0]
m = s / qntd
print('Media: {:.2f}'.format(m))
print('Higher: {}'.format(biggest))
print('Smaller: {}'.format(smaller))