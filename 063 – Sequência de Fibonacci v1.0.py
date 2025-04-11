# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8


print(f'''\033[1;32m{'='*55}\033[m
\033[1m{'SEQUÊNCIA DE FIBONACCI':^55}\033[m
\033[1;32m{'='*55}\033[m''')
termos = int(input('Quantos termos quer mostrar? '))
print(f'\033[1;32m{'='*55}\033[m')
t_um = 0
t_dois = 1
cont = 3
print(t_um, end='\033[1;33m-->\033[m')
print(t_dois, end='\033[1;33m-->\033[m')
while cont <= termos:
    cont += 1
    t_tres = t_um + t_dois
    t_um = t_dois
    t_dois = t_tres
    print(t_tres, end='\033[1;33m-->\033[m')
print('Fim!')
print(f'\033[1;32m{'='*55}\033[m')
