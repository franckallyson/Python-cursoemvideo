exp = str(input('Enter the expression:'))
p = list()
for l in exp:
    if l == '(':
        p.append(l)
    elif l == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(l)
            break
if p != 0:
    print('Invalid Expression!')
else:
    print('Valid Expression!')
