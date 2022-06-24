ans = 'Yes'
while ans == 'Yes':
    temp = float(input('Enter the temperature in Celsius: '))
    far = (temp * 9 / 5) + 32
    print('The temperature {}°C in Fahrenheit is {}°F'.format(temp, far))
    ans = input('Do you want to do a new search? [Yes/No]')
else:
    print('End of search')
