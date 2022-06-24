from random import randint
wins = 0
print('=='*30)
print(' '*20, 'EVEN OR ODD')
print('=='*30)
while True:
    computer = randint(0, 10)
    a1 = int(input('Choose a number between 0 and 10:'))
    a2 = ' '
    while a2 not in 'EeOo':
        a2 = str(input('Even or Odd?:[E/O]')).strip().upper()[0]
    sum = computer + a1
    print(f'You chose {a1} and the computer chose {computer}. {sum} is ', end='')
    if a2 == 'E':
        if sum % 2 == 0:
            print('EVEN, YOU WIN.')
            wins += 1
        else:
            print('ODD, YOU LOSE.')
            break
    elif a2 == 'O':
        if sum % 2 != 0:
            print('ODD, YOU WIN.')
            wins += 1
        else:
            print('EVEN, YOU LOSE.')
            break
    print('~~'*30)
if wins == 0:
    print("\033[4mYou haven't won any!\033[m")
elif wins == 1:
    print(f'\033[4mYou only won {wins}.\033[m')
else:
    print(f'\033[4mYou made {wins} wins in a row!\033[m')
