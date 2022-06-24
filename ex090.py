reportCard = dict()
reportCard['name'] = str(input("Name of the Student:")).strip().capitalize()
reportCard['average'] = float(input(f'{reportCard["name"]} Average:'))
if reportCard['average'] < 5:
    reportCard['situation'] = 'Failed'
elif 5 <= reportCard['average'] < 7:
    reportCard['situation'] = 'Recovery'
else:
    reportCard['situation'] = 'Approved'
print('~='*20)
for k, v in reportCard.items():
    print(f' => {k.capitalize()} = {v}')
print('END')