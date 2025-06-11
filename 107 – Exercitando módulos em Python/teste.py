# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda
num = float(input('Digite o preço: R$ '))
por = float(input('Qual a taxa desejada?: '))
print(f'O valor de R$ {num} aumentado em {por} % é de R$ {moeda.aumentar(num, por)}')
print(f'O dobro de R$ {num} é R$ {moeda.dobro(num)}')
print(f'A metade de R$ {num} é R$ {moeda.metade(num)}')
print(f'O valor R$ {num} menos {por} % é  R$ {moeda.diminuir(num, por)}')
