m = [[], [], []]
sumEven = sumRdColumn = highSecLine = 0
for l in range(0, 3):
    for c in range(0, 3):
        m[l].append(int(input(f'Enter a Number in position [{l}, {c}]: ')))
        if m[l][c] % 2 == 0:
            sumEven += m[l][c]
        if c == 2:
            sumRdColumn += m[l][c]
        if l == 1:
            if c == 0:
                highSecLine = m[l][c]
            elif m[l][c] > highSecLine:
                highSecLine = m[l][c]
print('~~'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}] ', end='')
    print()
print('~~'*20)
print(f'Sum of Even Values: {sumEven}')
print(f'Sum of Third Column Values: {sumRdColumn}')
print(f'Highest value of Second Line: {highSecLine}')
