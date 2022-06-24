n = list()
while True:
    val = int(input('Enter a number: '))
    if val not in n:
        n.append(val)
        print('\033[4mAdded Value\033[m')
    else:
        val = int(input('This value is already on the list.'))
    ans = ' '
    while ans not in 'YN':
        ans = str(input('Do you want continue?[Y/N]:')).upper().strip()[0]
    if ans == 'N':
        break
n.sort()
print(n)
