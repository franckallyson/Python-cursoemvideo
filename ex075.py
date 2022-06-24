num = (int(input('Enter a number:')),
       int(input('Enter other number:')),
       int(input('Enter more other number:')),
       int(input('Enter the last number:')))
print(f'You typed: {num}')
print(f'The value 9 appeared {num.count(9)} times')
if 3 in num:
    print(f'The first value 3 was typed in position: {num.index(3)}')
else:
    print('The value 3 was not entered.')
print(f'The even numbers were: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')


