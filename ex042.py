r1 = float(input('Enter the 1st straight line:'))
r2 = float(input('Enter the 2nd straight line:'))
r3 = float(input('Enter the 3rd straight line:'))
if abs(r2 - r3) < r1 < (r2 + r3):
    print('These straights lines \033[4mCAN\033[m form a triangle.')
    if r1 == r2 == r3:
        print('The triangle that can be formed is: \033[4mEQUILATERAL\033[m')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print('The Triangle that can be formed is: \033[4mISOSCELES\033[m')
    else:
        print('The Triangle that can be formed is: \033[4mSCALENE\033[m')
else:
    print('These straights lines \033[4mCANNOT\033[m form a triangle.')
