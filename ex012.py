ans = 'Yes'
while ans == 'Yes':
    price = float(input('Enter a product value:'))
    disc = price * 0.95
    print('The value of the product with 5% discount is {:.2f}'.format(disc))
    ans = str(input('Do you want to do a new search?[Yes/No]'))
else:
    print('End of the search!')



