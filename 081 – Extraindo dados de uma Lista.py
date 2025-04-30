# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

value_list = []
value_sum = 0
while True:
    value = int(input('Digite um valor: '))
    value_sum += 1
    value_list.append(value)
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if stop == 'N':
        break
print(f'''Foram digitados {value_sum} valores em nossa lista,
A lista ordenada em forma decrescente {sorted(value_list, reverse=True)}''')
if 5 in value_list:
    print('Nós temos o valor 5 em nossa lista!')
else:
    print('Não temos o valor 5 em nossa lista!')
