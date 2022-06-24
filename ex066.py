amount = sum = 0
while True:
    n = int(input('Enter a number:[999] to Stop:'))
    if n == 999:
        break
    sum += n
    amount += 1
print(f'{amount} Numbers were entered and the sum between them is {sum}')
