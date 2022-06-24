'''JEITO QUE EU FIZ
gender = ['M', 'F']
sex = ''
while sex not in gender:
    sex = str(input('Enter the gender:[M/F]')).upper().strip()[0]
    if sex not in gender:
        print('INVALID OPTION, TRY AGAIN:', end='')
print('Sex "{}" Computed!'.format(sex))'''

sex = str(input('Enter the Gender[M/F]:')).upper().strip()[0]
while sex not in 'MF':
    sex = str(input('INVALID OPTION, TRY AGAIN: Enter the Gender[M/F]:')).upper().strip()[0]
print('Sex "{}" Computed'.format(sex))
