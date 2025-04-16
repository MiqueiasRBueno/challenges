# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
# cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.

print(f'''\033[1;31m{'='*55}\033[m
{'BANCO BUENOCRED':^55}
\033[1;31m{'='*55}\033[m''')
valor_saque = int(input('Qual valor deseja sacar: R$ '))
total = valor_saque
cedulas = 200
total_cedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas:>3} de R$ {f'{cedulas:.2f}':>6}')
        elif cedulas == 200:
            cedulas = 100
        elif cedulas == 100:
            cedulas = 50
        elif cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 2
        total_cedulas = 0
        if total == 0:
            break
