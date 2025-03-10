# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira:
from math import trunc

num_quebrado = float(input('Digite um número real: '))
print(f'O número {num_quebrado} tem sua parte inteira {trunc(num_quebrado)}')
