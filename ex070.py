spent = quant_prod = cheap = 0
name_cheap = ' '
while True:
    name = str(input('Enter product name:')).strip()
    price = float(input('Enter product price:'))
    if price > 1000:
        quant_prod += 1
    if cheap == 0 or cheap > price:
        cheap = price
        name_cheap = name
    spent += price
    ans = ' '
    while ans not in 'YN':
        ans = str(input('Do you want to register a new product?[Y/N]')).strip().upper()[0]
    if ans == 'N':
        break
    print('~~'*30)
print('~~'*30)
print('End of Register:')
print(f'Total purchase amount: R${spent:.2f}')
print(f'{quant_prod} Products cost more than R$1000.00')
print(f'The cheapest product is {name_cheap}. Costing R${cheap:.2f}')
