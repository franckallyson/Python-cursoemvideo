m = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        m[l].append(int(input(f'Enter a Number in position [{l}, {c}]: ')))
print('~~'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}] ', end='')
    print()
