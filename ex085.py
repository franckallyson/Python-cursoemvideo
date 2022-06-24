odd_even = [[], []]
for c in range(0, 7):
    if c == 0:
        n = int(input('Enter a number:'))
    else:
        n = int(input('Enter one more number:'))
    if n % 2 == 0:
        odd_even[0].append(n)
        print('Added in EVEN!')
    else:
        odd_even[1].append(n)
        print('Added in ODD')
odd_even[0].sort()
odd_even[1].sort()
print(odd_even)
print(f'Even Values: {odd_even[0]}')
print(f'Odd Values: {odd_even[1]}')

