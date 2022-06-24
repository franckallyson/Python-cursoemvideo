players = dict()
goals = list()
registry = list()
while True:
    totGoals = 0
    players['name'] = str(input('Player name:')).strip().capitalize()
    players['matchs'] = int(input(f'How many games did {players["name"]} play:'))
    if players['matchs'] == 0:
        players['goals'] = [0]
        players['total'] = totGoals
    else:
        for c in range(0, players['matchs']):
            goals.append(int(input(f'How many goals did he score in match {c+1}:')))
            totGoals += goals[c]
        players['goals'] = goals[:]
        players['total'] = totGoals
        goals.clear()
    registry.append(players.copy())
    while True:
        ans = str(input('Do you want continue?[Y/N]:')).strip().upper()[0]
        if ans in 'YN':
            break
        print('ERROR!')
    if ans == 'N':
        break
print('__'*25)
print(f'{"Nº":<5}{"NAME":<15}{"GOALS":<20}{"TOTAL":<5}')
print('¯¯'*25)
for i, p in enumerate(registry):
    print(f'{i:<5}{p["name"]:<15}{str(p["goals"]):<20}{p["total"]:<5}')
print('¯¯'*25)
while True:
    p = int(input('Which player do you want to see details:[999 to Stop]'))
    if p == 999:
        break
    elif len(registry) <= p:
        print("ERROR!")
    else:
        print(f'Did {registry[p]["name"]} play {registry[p]["matchs"]} games.')
        for i, v in enumerate(registry[p]['goals']):
            print(f'  => Score {v} in Match {i+1}')
        print(f'The player score {registry[p]["total"]} goals')
print('FINISH PROGRAM..')
