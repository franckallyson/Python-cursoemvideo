extensive = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
             'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
while True:
    while True:
        n = int(input('Enter a Number between 0 and 20:'))
        if 0 <= n <= 20:
            print(f'You write {extensive[n]}.')
            break
        else:
            print('Invalid Number, Try Again! ', end='')
    ans = ' '
    while ans not in 'YN':
        ans = str(input('Do you want continue?[Y/N]')).strip().upper()[0]
    if ans == 'N':
        break
print('End of search!')


