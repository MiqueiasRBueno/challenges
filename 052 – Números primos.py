# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Variáveis de entrada de dados, inseridos pelo usuário:
number_pri = int(input('Digite um número inteiro: '))
qtd = 0
for c in range(1, number_pri + 1):
    primo =  number_pri % c
    if primo == 0:
        qtd += 1
if qtd == 2:
    print(f'O número {number_pri} é um número primo!')
elif qtd > 1:
    print(f'O número {number_pri} é um número composto!')