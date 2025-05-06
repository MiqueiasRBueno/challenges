# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0]]
soma_pares = soma_coluna = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor para a [{linha}:{coluna}]: '))
print(f'\033[1;31m{'=' * 55}\033[m')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    else:
        if matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'''\033[1;31m{'=' * 55}\033[m
A soma de todos os números pares da matriz são : {soma_pares}
E a soma de todos os números da terceira coluna é {soma}
O maior número digitado na segunda linha da matriz foi: {maior}
\033[1;31m{'=' * 55}\033[m''')
