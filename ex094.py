people = dict()
record = list()
average = sum = 0
while True:
    people['name'] = str(input('Name:')).capitalize()
    while True:
        people['gender'] = str(input('Gender[M/F]:')).upper().strip()[0]
        if people['gender'] in 'MF':
            break
        print('ERROR!')
    people['age'] = int(input('Age:'))
    sum += people['age']
    record.append(people.copy())
    while True:
        ans = str(input('Do you want continue?[Y/N]:')).strip().upper()[0]
        if ans in 'YN':
            break
        print('ERROR!')
    if ans == 'N':
        break
print('__'*20)
print(f'A) Number of people registered: {len(record)}')
average = sum / len(record)
print(f'B) Average Age: {average:.1f}')
print(f'C) The women registered were: ', end='')
for p in record:
    if p['gender'] == 'F':
        print(f'{p["name"]}; ', end='')
print()
print('D) People above average Age:')
for p in record:
    if p['age'] > average:
        for k, v in p.items():
            print(f'{k.capitalize()} = {v}; ', end='')
        print()
