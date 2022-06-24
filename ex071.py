print('~'*40)
print('{:^40}'.format('NOSE BANK'))
print('-'*40)
value = int(input('What is the value of the withdrawal?'))
total = value
ballot = 50
tot_ballot = 0
while True:
    if total >= ballot:
        total -= ballot
        tot_ballot += 1
    else:
        if tot_ballot > 0:
            print(f'You will withdraw {tot_ballot} banknotes from R${ballot:.2f}')
        if ballot == 50:
            ballot = 20
        elif ballot == 20:
            ballot = 10
        elif ballot == 10:
            ballot = 1
        tot_ballot = 0
        if total == 0:
            break
print('-'*40)
print('Nose Bank thanks!')
