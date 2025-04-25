# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = menor = 0
for num in range(1, 6):
    valores.append(int(input(f'Digite o valor para posição {num}: ')))
print(f'''Você digitou os valores {valores}
O maior valor digitado foi {max(valores)} e está na posição: ''', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(i + 1, end='...')
print(f'\nO menor valor digitado foi {min(valores)} e está na posição: ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(i + 1, end='...')
