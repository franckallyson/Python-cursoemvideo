color = ('\033[m',          # 0 - No Color
         '\033[41m',        # 1 - Red
         '\033[42m',        # 2 - Green
         '\033[7m',         # 3 - White
         '\033[44m')        # 4 - Blue


def aid(x):
    return help(x)


def title(txt, c=0):
    from time import sleep
    print(color[c], end='')
    print('_'*(len(txt)+4))
    print(f'  {txt}')
    print('¯'*(len(txt)+4))
    print(color[0], end='')
    sleep(1)


# Main Program
while True:
    title('HELP SYSTEM PyHelp', 2)
    x = str(input('Function or Library > ')).lower()
    if x == 'end':
        break
    title(f'Acessing the {x} Command Manual', 4)
    print(color[3], end='')
    aid(x)
title('END!', 1)
