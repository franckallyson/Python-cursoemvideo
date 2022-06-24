def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if not formato else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if not formato else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(p, aum, dim):
    print('__'*20)
    print(f'{"RESUMO DO VALOR":^40}')
    print('¯¯'*20)
    print(f'Preço Analisado: \t{moeda(p)}')
    print(f'Dobro do Preço: \t{dobro(p, True)}')
    print(f'Metade do Preço: \t{metade(p, True)}')
    print(f'{aum}% de aumento: \t{aumentar(p, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(p, dim, True)}')
    print('¯¯' * 20)
