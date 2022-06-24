a1 = int(input('Enter the first term:'))
r = int(input('Enter the reason:'))
n = 1
new_n = 10
terms = 0
while new_n != 0:
    terms += new_n
    n2 = new_n
    n2 += n
    while n != n2:
        an = a1 + (n-1)*r
        print('{} -> '.format(an), end='')
        n += 1
    print('PAUSE')
    new_n = int(input('Want to see how many more terms?'))
print('Finished Process with {} terms Shown.'.format(terms))
