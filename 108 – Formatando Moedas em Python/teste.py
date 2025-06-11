# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda
num = float(input('Digite o preço: R$ '))
por = float(input('Qual a taxa desejada?: '))
print(f'O valor de {moeda.moeda(num)} aumentado em {por} % é de {moeda.moeda(moeda.aumentar(num, por))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O valor R$ {moeda.moeda(num)} menos {por} % é {moeda.moeda(moeda.diminuir(num, por))}')
