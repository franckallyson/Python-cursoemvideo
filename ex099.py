from time import sleep


def bigger(*val):
    biggest = 0
    print('Analyzing past values:', end='')
    for v in val:
        print(f'{v} ', end='', flush=True)
        sleep(0.4)
        if biggest == 0:
            biggest = v
        elif v > biggest:
            biggest = v
    print()
    print(f'{len(val)} Values were informed.')
    print(f'The Biggest value among them is {biggest}.')
    print('¯¯'*20)


bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger()
