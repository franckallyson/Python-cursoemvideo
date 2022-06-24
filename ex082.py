n = list()
ni = list()
np = list()
while True:
    n.append(int(input('Enter a number:')))
    ans = ' '
    while ans not in 'YN':
        ans = str(input('Do you want continue?[Y/N]:')).upper().strip()[0]
    if ans == 'N':
        break
print(f'Complete list: {n}')
for i, v in enumerate(n):
    if v % 2 == 0:
        np.append(v)
    else:
        ni.append(v)
print(f'List with even values: {np}')
print(f'List with odd values: {ni}')
