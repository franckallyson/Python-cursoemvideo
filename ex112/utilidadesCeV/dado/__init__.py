def leiaNumero(msg):
    while True:
        p = str(input(msg)).strip().replace(',', '.')
        if p.replace('.', '', 1).isdigit():
            return float(p)
        print(f'\033[4;31mERRO! O valor informado "{p}" não é numérico!\033[m')
