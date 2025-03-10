# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.

from math import sqrt
cateto_oposto = int(input('Digite a medida do cateto oposto "a": '))
cateto_adjacente = int(input('Digite a medida do cateto adjacente "b": '))
catetos = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = sqrt(catetos)
print(f'A hipotensa dos catetos "a":{cateto_oposto:.2f} e "b":{cateto_adjacente:.2f} é {hipotenusa:.2f}')
