heavier = 0
lesser = 0
for people in range(1, 6):
    weight = float(input("Enter the person's weight(kg): "))
    if people == 1:
        heavier = weight
        lesser = weight
    else:
        if weight > heavier:
            heavier = weight
        if weight < lesser:
            lesser = weight
print('The highest weight read was {:.1f}Kg'.format(heavier))
print('The lowest weight read was {:.1f}Kg'.format(lesser))
