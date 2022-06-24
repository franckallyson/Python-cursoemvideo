from random import randint
from time import sleep
numbers = list()


def prizeDraw(list):
    print('The numbers drawn were: ', end='')
    for c in range(0, 5):
        list.append(randint(0, 9))
        print(f'{numbers[c]} ', end='', flush=True)
        sleep(0.4)
    print()


def sumEven():
    sum = 0
    for v in numbers:
        if v % 2 == 0:
            sum += v
    print(f'The sum between the even numbers drawn in {numbers} is: {sum}.')


prizeDraw(numbers)
sumEven()
