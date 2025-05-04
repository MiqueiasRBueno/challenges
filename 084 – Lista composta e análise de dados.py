# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cadastro_temp = []
cadastro_princ = []
maior = menor = 0
while True:
    cadastro_temp.append(str(input('Nome: ')).title().strip())
    cadastro_temp.append(float(input('Peso: ')))
    if len(cadastro_princ) == 0:
        maior = menor = cadastro_temp[1]
    else:
        if cadastro_temp[1] > maior:
            maior = cadastro_temp[1]
        if cadastro_temp[1] < menor:
            menor = cadastro_temp[1]
    cadastro_princ.append(cadastro_temp[:])
    cadastro_temp.clear()
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if stop == 'N':
        break
print(f'''Temos o total de {len(cadastro_princ)} pessoas cadastradas!
O maior peso cadastrado é de {maior:.2f} kg, e pertence a''', end=' ')
for p in cadastro_princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso cadastrado é de {menor:.2f} kg e pertence a', end=' ')
for p in cadastro_princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
