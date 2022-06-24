from time import sleep


def counter(start, end, step):
    if step == 0:
        step = 1
    print(f'From {start} to {end}, with {step} Step:')
    sleep(2)
    print(' => ', end='')
    if start < end:
        for c in range(start, end+1, step):
            print(f'{c}; ', end='', flush=True)
            sleep(0.5)
    elif start > end:
        step = abs(step)
        step = -step
        for c in range(start, end-1, step):
            print(f'{c}; ', end='', flush=True)
            sleep(0.5)
    print()
    print('••'*20)


print('A) ', end='')
counter(1, 10, 1)
print('B) ', end='')
counter(10, 0, -2)
print(f'{"C U S T O M  C O U N T E R":^40}')
print('¯¯'*20)
start = int(input('Counter Start:'))
end = int(input('Counter End:'))
step = int(input('Counter Step:'))
print('C) ', end='')
counter(start, end, step)
