from ex108 import moeda

p = float(input('Enter price: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% temos R${moeda.moeda(moeda.aumentar(p, 10))}')