# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
# an = a1 + ( n - 1). r
from time import sleep

print(f'''\033[31;1m{'=' * 55}\033[m
{'PROGRESSÃO ARITMÉTICA 2.0':^55}
\033[31;1m{'=' * 55}\033[m''')
termo_pa = int(input('Digite o valor do termo de sua p.a: '))
razao_pa = int(input('Digite o valor da razão da p.a: '))
print(f'''\033[31;1m{'=' * 55}\033[m
P.A de {termo_pa} e razão {razao_pa}= ''', end='')
n = 0
while n != 10:
    sleep(0.7)
    n += 1
    pa = termo_pa + (n - 1) * razao_pa
    print(f'{pa}', end=' ')
print(f'''\033[1;32mACABOU!\033[m
\033[31;1m{'=' * 55}\033[m''')
