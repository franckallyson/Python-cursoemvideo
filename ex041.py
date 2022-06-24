from datetime import date
birth = int(input('What year was the athlete born?'))
age = date.today().year - birth
print('The athlete have {} years old'.format(age))

if age <= 9:
    print('The Athlete belongs to the category: \033[4mMIRIM\033[m')
elif age <= 14:
    print('The Athlete belongs to the category: \033[4mINFANTIL\033[m')
elif age <= 19:
    print('The Athlete belongs to the category: \033[4mJÚNIOR\033[m')
elif age <= 25:
    print('The Athlete belongs to the category: \033[4mSÊNIOR\033[m')
else:
    print('The Athlete belongs to the category: \033[4mMASTER\033[m')
