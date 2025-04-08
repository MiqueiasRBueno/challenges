# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

h_mais_velho = ''
maior_idade = cont = menores = media = 0
for c in range(1, 5):
    print(f'{'-' * 10} {c}{'ª PESSOA'}{'-' * 10}')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F] ')).strip().upper()
        if sexo == 'MF':
            break
    media += idade / 4
    if sexo == 'M':
        if c == 1:
            maior_idade = idade
            h_mais_velho = nome
        else:
            if idade > maior_idade:
                maior_idade = idade
                h_mais_velho = nome
    if sexo == 'F' and idade < 20:
        cont += 1
print(f'''A média de idade do grupo é de {media} anos
O homem mais velho do grupo tem {maior_idade} anos e se chama {h_mais_velho}
Ao todo temos {cont} mulheres com menos de 20 anos''')
