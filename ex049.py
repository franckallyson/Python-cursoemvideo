n = int(input('Want to see the multiplication table for which number?'))
for c in range(1, 11):
    print('{:2} x {:2} = {:2}'.format(c, n, c * n))
print('End')
