# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = list()
# função para sortear 5 valores:
def sorteia(lista):
    print('\033[32m-\033[m' * 53)
    print('Sorteando 5 valores: ', end=' ')
    for t in range(0, 3):
        print('.', end=' ')
        sleep(0.3)
    for n in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
    for valor in lista:
        print(valor, end=' ')
        sleep(0.3)
    print()

# função para a soma de pares:
def somapar(lista):
    print('\033[32m-\033[m' * 53)
    print(f'A soma dos valores pares', end=' ')
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
            sleep(0.3)
            print(valor, end=' ')
    sleep(0.3)
    print(f', temos {soma}')


# Programa principal
sorteia(numeros)
sleep(0.3)
somapar(numeros)
