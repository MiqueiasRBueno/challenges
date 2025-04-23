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
    print(f'\nO número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'\nO número 3 apareceu na posição {valores.index(3)+1}')
else:
    print('Não temos valores 3 em nossa tupla!')
print('Os valores pares são: ', end=' ')
for pares in valores:
    if pares % 2 == 0:
        print(pares, end=' ')
