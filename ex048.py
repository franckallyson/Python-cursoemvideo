s = 0
quant = 0
for c in range(3, 501, 3):
    if c % 2 == 1:
        quant += 1
        s += c
print('The sum was: {}'.format(s))
print('Amount of values: {}'.format(quant))