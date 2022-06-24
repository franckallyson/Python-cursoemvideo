number = int(input('Enter a integer number:'))
print('Choose one of the bases for conversion:\n'
      '[ 1 ] BINARY\n'
      '[ 2 ] OCTAL\n'
      '[ 3 ] HEXADECIMAL')
base = int(input('Your Choice:'))

if base == 1:
    print('This number in binary is {}'.format(bin(number)[2:]))
elif base == 2:
    print('This number in Octal is {}'.format(oct(number)[2:]))
elif base == 3:
    print('This number in Hexadecimal is {}'.format(hex(number)[2:]))
else:
    print('INVALID OPTION')
