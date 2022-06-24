print('-' * 40)
print('|', ' '*13, 'Data', ' '*18, '|')
print('|', 'R$ 0.15 per kilometer driven', ' '*8, '|')
print('|', 'R$ 60.00 per day rented', ' '*13, "|")
print('-'*40)
ans = 'Yes'
while ans == 'Yes':
    print('-'*40)
    km = int(input('How many kilometers did the car travel?'))
    day = int(input('How many days?'))
    total = (km * 0.15) + (day * 60)
    print('The amount the costumer pay is R$ {:.2f}'.format(total))
    ans = input('Do you want to do a new search?[Yes/No]')
else:
    print('End of search!')
