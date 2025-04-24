# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Lapís', 1.75,
         'Caneta', 2.50,
         'Caderno', 32.00,
         'Giz de cera', 8.00,
         'Cola branca', 12.00)
print(f'''\033[1;31m{'='*40}\033[m
{'TABELA DE PREÇOS':^40}
\033[1;31m{'='*40}\033[m''')
for pos in range(0, len(lista)): # imprime cada item da lista
    if pos % 2 == 0: # se o item da lista estiver em uma posição par:
        print(f'{lista[pos]:.<30}', end='')
    else: # se o item estiver em uma posição impar:
        print(f'R$ {lista[pos]:>7}')
print(f'\033[1;31m{'='*40}\033[m')
