from random import randint
computer = randint(0, 10)
guesses = 1
ans = int(input('I thought of a number, can you guess?'))
while ans != computer:
    if ans > computer:
        ans = int(input('WRONG ANSWER, Is a smaller number, Try again:'))
    else:
        ans = int(input('WRONG ANSWER, Is a larger number, Try again:'))
    guesses += 1
print('Congratulation, you got it right!')
print('It took {} Tries.'.format(guesses))
