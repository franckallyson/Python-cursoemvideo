n1 = float(input('Enter the 1st note:'))
n2 = float(input('Enter the 2nd note:'))
average = (n1 + n2)/2
print("The student's average is {:.1f}".format(average))
if average < 5.0:
    print('With this average the student is: \033[4mFAILED\033[m')
elif 5.0 <= average < 7.0:
    print('With this average the student is: \033[4mIN RECOVERY\033[m')
elif average >= 7.0:
    print('With this average the student is: \033[4mAPPROVED\033[m')
