# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda
num = int(input('Digita um valor: '))
por = float(input('Qual a porcentagem desejada?: '))
print(f'O valor {num} aumentado em {por} % é {moeda.aumentar(num, por)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O valor {num} menos {por} % é  {moeda.diminuir(num, por)}')
