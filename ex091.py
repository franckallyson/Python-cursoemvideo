from random import randint
from time import sleep
from operator import itemgetter
players = dict()
print('THROWING DICE...')
players['player1'] = randint(1, 6)
players['player2'] = randint(1, 6)
players['player3'] = randint(1, 6)
players['player4'] = randint(1, 6)
for k, v in players.items():
    sleep(0.5)
    print(f'    => {k.capitalize()} take out {v} ')
print('__'*20)
print('RANKING')
ranking = list()
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f' => {i+1}º = {v[0]} with {v[1]}.')
print('__'*20)
print('END')
