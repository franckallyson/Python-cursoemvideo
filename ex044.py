price = float(input('What is the Price of the Product?'))
print('''How do you want to pay?
[ 1 ] Cash/Check :: 10% Off
[ 2 ] Cash on the Card :: 5% Off
[ 3 ] 2x on the Card :: Formal Price
[ 4 ] 3x or more on the Card :: 20% Interest''')
pay_method = int(input('Your Choice: '))

if pay_method == 1:
    print('The value of the product stays R${:.2f}'.format(price - (price * 0.10)))
elif pay_method == 2:
    print('The value of the product stays R${:.2f}'.format(price - (price * 0.05)))
elif pay_method == 3:
    parcel = price / 2
    print('You will pay 2 installments of R${:.2f} and the total amount will be {:.2f}'.format(parcel, price))
elif pay_method == 4:
    price_tot = price + (price * 0.20)
    ins = int(input('In how many installments you will pay?'))
    parcel = price_tot / ins
    print('You will pay {} installments of R${:.2f} and the total amount will be R${:.2f}'.format(ins, parcel, price_tot))
else:
    print('INVALID OPTION')
