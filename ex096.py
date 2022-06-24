def area(width, length):
    area = width * length
    print(f'Width is: {width}')
    print(f'Length is: {length}')
    print(f'The Land Area is {area:.1f} m²')


def title(txt):
    print('__'*20)
    print(f'{txt:^40}')
    print(f'¯¯'*20)


title('L A N D  A R E A')
width = float(input('Enter the Land Width:'))
length = float(input('Enter the Land Length:'))
area(width, length)
