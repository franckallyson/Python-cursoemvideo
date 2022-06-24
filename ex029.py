spd = int(input("What is the car's current speed?"))
if spd > 80:
    over = spd - 80
    ticket = over * 7
    print("\033[1;31m"'You was fined for velocity excess! The allowed is 80 Km/h')
    print("\033[1;31m"'For being {} Kilometers above allowed, you received U${:.2f} in fines'.format(over, ticket))
else:
    print("\033[1;32m"'Have a good travel!')
