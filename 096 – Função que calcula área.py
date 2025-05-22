# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def grounds_calculator(l, c):
    grounds = l * c
    print(f'A área do terreno de \033[32m{l}\033[m X \033[32m{c}\033[m é de \033[32m{grounds}\033[m m²')


# Programa principal
print(f'''\033[1;32m{"CONTROLE DE TERRENOS":^50}\033[m
\033[1;31m{"-" * 50}\033[m''')
width = float(input('LARGURA (m): '))
length = float(input('COMPRIMENTO (m): '))
grounds_calculator(width, length)
