# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


# Configuração da função contador:
def contador():
    print('\033[1;32m=\033[m' * 55)
    sleep(0.5)
    print('a) Contagem de 1 até 10, de 1 em 1:')
    sleep(0.5)
    for n in range(1, 11, 1):
        sleep(0.5)
        print(n, end=' ')
    sleep(0.5)
    print('FIM')
    print('\033[1;32m=\033[m' * 55)
    sleep(0.5)
    print('b) Contagem de 10 até 0, de 2 em 2:')
    sleep(0.5)
    for n1 in range(10, 0, -2):
        sleep(0.5)
        print(n1, end=' ')
    sleep(0.5)
    print('FIM')
    print('\033[1;32m=\033[m' * 55)
    sleep(0.5)
    print('Agora é sua vez de personalizar a contagem:')
    sleep(0.5)
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    for i in range(inicio, fim, passo):
        sleep(0.5)
        print(i, end=' ')
        sleep(0.5)
    print('FIM')


# Programa principal:
contador()