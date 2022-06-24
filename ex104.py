def readInt(msg):
    while True:
        print('__' * 20)
        n = str(input(msg))
        if n.isdigit():
            return n
            break
        else:
            print('\033[4;31mThis is not an integer.\033[m')


# Main Program
number = readInt('Enter a number:')
print(f'Do you typed the number {number}.')
