from random import randint
from time import sleep
jokenpo = ['Rock', 'Paper', 'Scissors']
computer = randint(0, 2)

print('--=' * 10)
print('      Lets Play Jokenpo')
print('--=' * 10)
print('''[ 1 ] Rock
[ 2 ] Paper
[ 3 ] Scissors''')

player = int(input('Your Move:'))

print('JOO')
sleep(0.5)
print('KEEN')
sleep(0.5)
print('PO!!!')
print('--=' * 10)
print('Your Choice: {}'.format(jokenpo[player - 1]))
print('Computer Choice: {}'.format(jokenpo[computer]))
print('--=' * 10)

if player == 1:
    if computer == 0:
        print('\033DRAWN!')
    elif computer == 1:
        print('Computer WON!')
    elif computer == 2:
        print('You WON!')
elif player == 2:
    if computer == 1:
        print('DRAWN!')
    elif computer == 2:
        print('Computer WON!')
    elif computer == 0:
        print('You WON!')
elif player == 3:
    if computer == 2:
        print('DRAWN!')
    elif computer == 0:
        print('Computer WON!')
    elif computer == 1:
        print('You WON!')
else:
    print('INVALID OPTION')
