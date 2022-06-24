import random
c = 0
r = int(input('How many students do you want to ruffle?'))
lista = list(range(r))
while c <= (r-1):
    lista[c] = input('{}º Student: '.format(c+1))
    c = c + 1
print('The drawn Order was: {}'.format(random.sample(lista, r)))