from lib.interface import *


while True:
    resposta = menu(['Acessar Cadastro', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('op1')
    elif resposta == 2:
            cabecalho('opc2')
    elif resposta == 3:
        cabecalho('Saindo do Programa!...')
        break
    else:
        print('\033[31mERRO! Digite um valor válido!\033[m')
