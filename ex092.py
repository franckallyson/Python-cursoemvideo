from datetime import date
register = dict()
register['name'] = str(input('Name:')).capitalize()
birthDate = int(input('Year of birth:'))
register['age'] = date.today().year - birthDate
register['ctps'] = int(input('Work Card:'))
if register['ctps'] != 0:
    register['contractYear'] = int(input('Year of contract:'))
    register['salary'] = float(input('Wage:'))
    register['retirement'] = register['contractYear']+35 - birthDate
print('__'*30)
for k, v in register.items():
    print(f' => {k.capitalize()} = {v}')
