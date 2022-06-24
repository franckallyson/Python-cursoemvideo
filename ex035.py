s1 = float(input('Enter the 1st straight line: '))
s2 = float(input('Enter the 2nd straight line: '))
s3 = float(input('Enter the 3rd straight line: '))
if s1 > abs(s2 - s3) and s1 < (s2 + s3):
    print('These straights lines {}CAN{} form a triangle.'.format('\033[4;32m', '\033[m'))
else:
    print('These straights lines {}CANNOT{} form a triangle.'.format('\033[4;31m', '\033[m'))
