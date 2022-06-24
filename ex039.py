from datetime import date
gender = str(input('What is your Gender?[Male/Female]'))
if gender.upper() == 'MALE':
    birth = int(input('Year of Birth:'))
    age = date.today().year - birth
    less = 18 - age
    more = age - 18
    print('You have {} Years'.format(age))
    if age < 18:
        print('There are still {} years to enlist'.format(less))
        print('Your enlistment will be in {}'.format(birth + 18))
    elif age > 18:
        print('You should have enlisted {} years ago'.format(more))
        print('Your enlistment was in {}'.format(birth + 18))
    else:
        print("It's time for you to enlist!")
elif gender.upper() == 'FEMALE':
    print('Women are not required to enlist.')