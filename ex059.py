n1 = int(input('Enter the First Number:'))
n2 = int(input('Enter the Second Number:'))
print('=--'*10)
ans = 0
while ans != 5:
    print('''      --=M E N U=--
    [1] Add
    [2] Multiply
    [3] Higher Number
    [4] New Numbers
    [5] Go out''')
    ans = int(input('>>> What do you want to do?'))
    if ans == 1:
        sum = n1 + n2
        print('The Sum between {} and {} is {}.'.format(n1, n2, sum))
    elif ans == 2:
        product = n1 * n2
        print('The Product between {} and {} is {}.'.format(n1, n2, product))
    elif ans == 3:
        if n1 > n2:
            print('{} is greater than {}.'.format(n1, n2))
        elif n1 < n2:
            print('{} is greater than {}.'.format(n2, n1))
        else:
            print('Both the numbers are same.')
    elif ans == 4:
        print('New Query!')
        n1 = int(input('Enter the First Number:'))
        n2 = int(input('Enter the Second Number:'))
    elif ans == 5:
        print('End of Search')
    else:
        print('INVALID OPTION, TRY AGAIN')
    print('=--'*10)
print('Finished Program!')
