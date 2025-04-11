# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = soma = 0
numbers = int(input('Digite um valor: (999 para parar) '))
while True:
    cont += 1
    soma += numbers
    numbers = int(input('Digite um valor: (999 para parar) '))
    if numbers == 999:
        break
print(f'''\033[34mVocê digitou\033[m \033[1m{cont}\033[m \033[34mvalores
E a soma desses valores é\033[m \033[1m{soma}\033[m\033[34m!\033[m''')
