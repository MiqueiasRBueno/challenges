# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
    print('\033[1;31m=\033[m' * 45)
    print('Analisando os valores passados...')
    tot = 0
    if len(num) <= 0:
        print(f' _Foram informados {tot} valores!')
        print(f'O maior valor informado foi 0')
    else:
        for c in num:
            print(c, end=' ')
            sleep(0.5)
            tot += 1
        print(f' _Foram informados {tot} valores!')
        print(f'O maior valor informado foi {max(num)}')


# Programa Principal:
maior(1, 3, 6, 7, 9)
maior(4, 5 , 2, 7, 8, 9, 3, 90, 2132)
maior()
