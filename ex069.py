quant_age = mans = women = 0
while True:
    print('~~' * 30)
    print(' '*17, 'Registration of Persons')
    print('~~' * 30)
    age = int(input("Enter the Person's Age:"))
    gender = ' '
    while gender not in 'MF':
        gender = str(input("Enter the Person's Gender[M/F]:")).strip().upper()[0]
    if age >= 18:
        quant_age += 1
    if gender == 'M':
        mans += 1
    if gender == 'F' and age < 20:
        women += 1
    ans = ' '
    while ans not in 'YN':
        ans = str(input('Do you want to register more?[Yes/No]')).strip().upper()[0]
    if ans == 'N':
        print('--' * 30)
        break
    print('~~'*30)
print('End of Search!')
print(f'{quant_age} people are over 18 years old.')
print(f'{mans} mans were register.')
print(f'{women} women register are under 20 years old.')