# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.

from random import randint

numeros = list()
# função para sorteiar 5 valores:
def sorteia(lista):
    print('\033[32m-\033[m' * 45)
    print('Sorteando 5 valores: ', end=' ')
    for n in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
    for valor in lista:
        print(valor, end=' ')
    print()

# função para a soma de pares:
def somapar(lista):
    print('\033[32m-\033[m' * 45)
    print(f'A soma dos valores pares são ', end='')
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(soma)


# Programa principal
sorteia(numeros)
somapar(numeros)
