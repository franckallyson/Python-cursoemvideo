n = list()
while True:
    n.append(int(input('Enter a number:')))
    ans = ' '
    while ans not in 'YN':
        ans = str(input('Do you want continue? [Y/N]:')).upper().strip()[0]
    if ans == 'N':
        break
print(f'Amount of values: {len[n]}')
n.sort(reverse=True)
print(f'The list of values in descending order is: {n}')
if 5 in n:
    print('The value 5 was entered and is at position ', end='')
    for i, v in enumerate(n):
        if v == 5:
            print(f'{i}..', end='')
else:
    print('The value 5 was not entered.')
