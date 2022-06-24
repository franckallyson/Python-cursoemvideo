km = float(input('How many kilometers will the trip take?'))
#if km <= 200:
#    price = km * 0.5
#else:
#    price = km * 0.45
price = km * 0.5 if km <= 200 else km * 0.45
print('The value of the travel is U${:.2f}'.format(price))
