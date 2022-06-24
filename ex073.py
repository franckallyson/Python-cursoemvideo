teams = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Flamengo', 'Athletico-PR', 'Ceará', 'Santos',
         'Atlético-GO', 'Bahia', 'Corinthians', 'Fluminense', 'Juventude', 'Internacional',
         'Sport', 'Cuiabá', 'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense')
print('~~' * 60)
print(f'Team Lits: {teams}')
print('~~' * 60)
print(f'5 firsts teams: {teams[:5]}')
print('~~' * 60)
print(f'Last 4 teams: {teams[-4:]}')
print('~~' * 60)
print(f'Alphabetical Order: {sorted(teams)}')
print('~~' * 60)
print(f'Chapecoense is: {teams.index("Chapecoense")}º')