def record(name='<unknown>', goals=0):
    print('**' * 20)
    print(f'{"PLAYER SHEET":^40}')
    print('__'*20)
    print(f'NAME: {name}')
    print('~~'*20)
    print(f'GOALS: {goals}')
    print(f'¯¯'*20)


# Main Program
print('__'*20)
nameInput = str(input('Player Name: '))
goalsInput = input('Player Goals: ')
if nameInput.strip() == '':
    nameInput = '<unknown>'
if not goalsInput.isnumeric():
    goalsInput = 0
record(nameInput, goalsInput)
