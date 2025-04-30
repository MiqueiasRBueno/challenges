# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

value_list = []
pares = []
impares = []
while True:
    value_int = int(input('Digite um valor: '))
    value_list.append(value_int)
    if value_int % 2 == 0:
        pares.append(value_int)
    else:
        impares.append(value_int)
    stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if stop in 'N':
        break
print(f'''Valores pares digitados são: {pares}
Valores ímpares digitados são: {impares}
Todos os valores digitados são: ''', end=' ')
print(*value_list)
