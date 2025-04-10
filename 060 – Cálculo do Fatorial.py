# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
from time import sleep

number = int(input('Digite um valor: '))
ft = number
mult = 1
sleep(0.8)
print('\033[1;33mCal', end='')
sleep(0.8)
print('cu', end='')
sleep(0.8)
print('lan', end='')
sleep(0.8)
print('do\033[m', end='')
sleep(0.8)
print('\033[1;31m. . .', end=' ')
sleep(0.8)
print('. . .', end=' ')
sleep(0.8)
print('. . .\033[m')
sleep(0.8)
print(f'{number}! \033[1;32m=\033[m {number}', end=' ')
while ft != 1:
    ft -= 1
    mult *= ft + 1
    sleep(0.8)
    print(f'\033[1;32mX\033[m {ft}', end=' ')
print(f'\033[32;1m=\033[m {mult}')
