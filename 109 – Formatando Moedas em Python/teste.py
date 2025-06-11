# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda
num = float(input('Digite o preço: R$ '))
por = float(input('Qual a taxa desejada?: '))
print(f'O valor de {moeda.moeda(num)} aumentado em {por} % é de {moeda.aumentar(num, por, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O valor R$ {moeda.moeda(num)} menos {por} % é {moeda.diminuir(num, por, True)}')
