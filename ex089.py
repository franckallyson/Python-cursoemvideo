reportCard = list()
while True:
    name = str(input('Enter Student Name:')).capitalize()
    note1 = float(input('Enter the First Note:'))
    note2 = float(input('Enter the Second Note:'))
    average = (note1+note2)/2
    reportCard.append([name, [note1, note2], average])
    ans = ' '
    while ans not in 'YN':
        ans = str(input('Do you want continue?[Y/N]:')).upper().strip()[0]
    if ans == 'N':
        break
print('~~'*20)
print(f'{"R E P O R T  C A R D":^40}')
print(f'\033[4m{"Nº":<5}{"NAME":<29} NOTE\033[m')
for i, p in enumerate(reportCard):
    print(f'{i:<5}{p[0]:.<31}{p[2]:.1f}')
while True:
    s = int(input("Want to see which student's Grade?[999 to Stop]:"))
    if s == 999:
        break
    elif s <= len(reportCard) - 1:
        print(f'{reportCard[s][0]} had the Notes: {reportCard[s][1]}')
        print('~~'*20)
print('FINISHED PROGRAM..')
