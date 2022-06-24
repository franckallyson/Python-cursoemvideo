def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: Enter Valid Number Integer!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n033[31mEntrada de Dados interrompida pelo Usuário\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: Enter Valid Real number!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de Dados Interrompida pelo Usuário!\033[m')
            return 0
        else:
            return n


numInt = leiaInt('Digite um Inteiro:')
numReal = leiaFloat('Digite um Real:')
print(f'The Integer Value Typed was {numInt} and the Real Value Typed was {numReal}')