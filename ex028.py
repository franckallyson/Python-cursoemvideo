from random import randint
from time import sleep
n = randint(0, 5)
ans = int(input("\033[1;36m"'I thought of a number between 0 and 5, you can guess this number?'))
print("\033[0;32m"'PROCESSING...')
sleep(2)
if ans == n:
    print("\033[1;34m"'NICE! You got it right!!!')
else:
    print("\033[1;31m" 'OH NO! The correct number was {}'.format(n))
