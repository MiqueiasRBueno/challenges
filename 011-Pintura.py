# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

parede_largura = int(input('Digite a largura de sua parede: '))
parede_altura = int(input('Digite a altura de sua parede: '))
parede_metros = parede_largura * parede_altura
tinta_litros = parede_metros / 2
print(f'Para uma parede de {parede_metros:.2f} metro(s) quadrados você precisara'
      f' de {tinta_litros:.2f} litro(s) de tinta.')
