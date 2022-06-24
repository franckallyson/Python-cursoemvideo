people = list()
person = list()
heavy = 0
light = 0
while True:
    person.append(str(input('Name: ')))
    person.append(float(input('Weight: ')))
    people.append(person[:])
    if len(people) == 1:
        heavy = person[1]
        light = person[1]
    else:
        if heavy < person[1]:
            heavy = person[1]
        if light > person[1]:
            light = person[1]
    person.clear()
    ans = ' '
    while ans not in 'YN':
        ans = str(input('Do you want continue?[Y/N]:')).strip().upper()[0]
    if ans == 'N':
        break
print(f'{len(people)} People were registered!')
print(f'The highest weight recorded was {heavy:.1f}Kg. People with this weight are ', end='')
for p in people:
    if p[1] == heavy:
        print(f'[{p[0]}] ', end='')
print(f'\nThe lightest weight recorded was {light:.1f}Kg. People with this weight are ', end='')
for p in people:
    if p[1] == light:
        print(f'[{p[0]}] ', end='')
