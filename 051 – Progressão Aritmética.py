# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
from time import sleep

print(f'''\033[1;31m{'=' * 50}\033[m
\033[1m{'10 TERMOS DE UMA P.A.':^50}\033[M
\033[1;31m{'=' * 50}\033[m''')
# Variável para interação com o usuário:
termo = int(input('Primeiro termo de uma P.A.: '))
razao = int(input('Razão dessa P.A.: '))
print(f'\033[1;31m{'=' * 50}\033[m')
# Laço para pa:
for n in range(1, 11):
    pa = termo + (n -1) * razao
    sleep(0.5)
    print(pa, end=' ')
print(f'''\033[1;36mACABOU!!!\033[m
\033[1;31m{'=' * 50}\033[m''')
