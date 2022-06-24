weight = float(input('What is your weight(Kg):'))
tall = float(input('How tall are you (m): '))

BMI = weight / (tall ** 2)
print('Your IMC is {:.1f}'.format(BMI))

print('Situation: ', end='')
if BMI < 18.5:
    print('\033[4mUNDERWEIGHT\033[m')
elif 18.5 <= BMI < 25:
    print('\033[4mIDEAL WEIGHT\033[m')
elif 25 <= BMI < 30:
    print('\033[4mOVERWEIGHT\033[m')
elif 30 <= BMI < 40:
    print('\033[4mOBESITY\033[m')
else:
    print('\033[4mMORBID UNDERWEIGHT\033[m')
