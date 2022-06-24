from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de Listar o Conteúdo de um Arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de Cadastrar uma Nova Pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de Sair do Sistema
        cabecalho('SAINDO DO SISTEMA... Até Logo!')
        break
    else:
        print('\033[31mOpção Inválida!\033[m')
    sleep(2)
