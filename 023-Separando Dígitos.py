# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um de seus dígitos separados:
# unidade
# dezena
# centena
# milhar

separating_digits = int(input('Digite um número ente 0 e 9999: '))
unit = separating_digits % 10
ten = separating_digits // 10 % 10
hundreds = separating_digits // 100 % 10
thousand = separating_digits // 1000 % 10
print(f'O número dígitado tem:\n{unit} unidade\n{ten} dezenas\n{hundreds} dezenas\n{thousand} milhar')
