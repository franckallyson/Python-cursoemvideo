n = list()
biggest = 0
smaller = 0
for c in range(0, 5):
    n.append(int(input(f'Enter the {c}º Number:')))
    if c == 0:
        biggest = smaller = n[0]
    else:
        if n[c] > biggest:
            biggest = n[c]
        if n[c] < smaller:
            smaller = n[c]
print(f'The list is {n}')
print(f'The highest value entered was {biggest} at position ', end='')
for i, v in enumerate(n):
    if v == biggest:
        print(f'{i}...', end='')
print(f'The smallest value entered was {smaller} at position ', end='')
for i, v in enumerate(n):
    if v == smaller:
        print(f'{i}...', end='')
