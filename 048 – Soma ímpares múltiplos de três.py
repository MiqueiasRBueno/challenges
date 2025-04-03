# Faça um programa que calcule a soma entre todos os números que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.

soma = cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os \033[1;34m{cont}\033[m valores ímpares, '
      f'no intervalo de 1 à 500, múltiplo de 3 é \033[1;33m{soma} ')
