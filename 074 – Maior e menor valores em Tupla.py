# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

sorteio = randint(0, 10), randint(0,10), randint(0,10), randint(0, 10), randint(0, 10)
print(f'''{sorteio}
O mair valor sorteado é {max(sorteio)}
E o menor valor sorteado é {min(sorteio)}''')