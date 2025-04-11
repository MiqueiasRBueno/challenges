# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = soma = 0
numbers = int(input('Digite um número: [999 para parar] '))
while numbers != 999:
    cont += 1
    soma += numbers
    numbers = int(input('Digite um número: [999 para parar] '))
print(f'Você digitou {cont} e a soma entre eles foi {soma}')