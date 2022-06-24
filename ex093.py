player = dict()
goals = list()
total = 0
player['name'] = str(input('Name:')).capitalize()
player['numberMatches'] = int(input('Number of Matches:'))
if player['numberMatches'] > 0:
    for c in range(0, player['numberMatches']):
        goals.append(int(input(f'   Goals in match {c+1}:')))
        total += goals[c]
    player['goals'] = goals.copy()
    player['total'] = total
else:
    player['goals'] = [0]
    player['total'] = 0
print('__'*30)
print(player)
print('__'*30)
for k, v in player.items():
    print(f'{k} is {v}.')
print('__'*30)
print(f'{player["name"]} played {player["numberMatches"]} matches.')
for i, v in enumerate(player['goals']):
    if player['numberMatches'] == 0:
        print(f'This player did not play.')
    else:
        print(f'   => Goals in Match {i+1} = {v}')
print(f'The total of goals was: {player["total"]}')
