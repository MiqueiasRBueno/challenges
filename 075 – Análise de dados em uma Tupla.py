# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = ((int(input('Digite um número: '))), (int(input('Digite outro número: '))),
           (int(input('Digite mais um número: '))), (int(input('Digite outro número: '))))
print(f'Você digitou os valores: ', end=' ')
for n1 in valores:
    print(f'\033[1;31m{n1}\033[m', end=' ')
if 9 in valores:
    print(f'\nO número \033[1;35m9\033[m apareceu \033[1;35m{valores.count(9)}\033[m vezes')
if 3 in valores:
    print(f'O número \033[1;33m3\033[m apareceu na \033[1;33m{valores.index(3)+1}\033[mª posição')
else:
    print('\nNão temos valores \033[1;33m3\033[m em nossa tupla!')
print('Os valores pares são: ', end=' ')
for pares in valores:
    if pares % 2 == 0:
        print(f'\033[1;32m{pares}\033[m', end=' ')
