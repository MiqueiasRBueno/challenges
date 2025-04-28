# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numbers = []
while True:
    num = (int(input('Digite um valor: ')))
    if num not in numbers:
        numbers.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Este número já existe na lista, não sera adicionado!')
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if parar == 'N':
        break
print(f'Os valores adicionados na lista foram: {sorted(numbers)}')
