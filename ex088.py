from random import randint
from time import sleep
record = []
prizeDraw = []
quant = int(input('How many games do you want to make?'))
for g in range(0, quant):
    for d in range(0, 6):
        prizeDraw.append(randint(1, 60))
        while prizeDraw.count(prizeDraw[d]) > 1:
            prizeDraw.append(randint(1, 60))
    prizeDraw.sort()
    record.append(prizeDraw[:])
    prizeDraw.clear()
print('SORTING...')
sleep(2)
print('~~'*20)
print('Your Games:')
for g in range(0, quant):
   print(f'{g+1}º Game: {record[g]}')
print(f'-='*6, {"GOOD LUCK"}, '=-'*6)
