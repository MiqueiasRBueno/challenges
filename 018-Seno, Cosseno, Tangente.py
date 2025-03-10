# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians
angulo = int(input('Digite o ângulo desejado: '))
print(f'O ângulo {angulo}º tem seu:'
      f'\nRadiano= {radians(angulo):.2f}'
      f'\nSeno= {sin(radians(angulo)):.2f}'
      f'\nCosseno= {cos(radians(angulo)):.2f}'
      f'\nTangente= {tan(radians(angulo)):.2f}')
