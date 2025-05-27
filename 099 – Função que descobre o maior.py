# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    print('\033[1;31m=\033[m' * 45)
    print('Analisando os valores passados...')
    tot = 0
    for c in num:
        print(c, end=' ')
        tot += 1
    print(f' _Foram informados {tot} valores!')
    print(f'O maior valor informado foi {max(num)}')


# Programa Principal:
maior(1, 3, 6, 7, 9)
maior(4, 5 , 2, 7, 8, 9, 3, 90, 2132)
maior(0)
