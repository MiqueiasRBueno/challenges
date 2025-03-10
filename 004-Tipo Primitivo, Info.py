# Crie um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informações sobre ele.

tp_primitivo = input('Digite algo: ')
print(f'{tp_primitivo} é uma {type(tp_primitivo)}')
print(f'{tp_primitivo} é numérico? {tp_primitivo.isnumeric()}')
print(f'{tp_primitivo} é alfabético? {tp_primitivo.isalpha()}')
print(f'{tp_primitivo} é alfanumérico? {tp_primitivo.isalnum()}')
print(f'{tp_primitivo} é em maiúscula? {tp_primitivo.isupper()}')
print(f'{tp_primitivo} é em minúscula? {tp_primitivo.islower()}')
print(f'{tp_primitivo} é capitalizado? {tp_primitivo.istitle()}')
print(f'{tp_primitivo} só contem espaços? {tp_primitivo.isspace()}')
