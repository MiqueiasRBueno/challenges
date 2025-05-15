# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

people_registration_dict = dict()
people_registration_list = list()
media = soma = 0
while True:
    people_registration_dict['Name'] = str(input('Nome: '))
    while True:
        people_registration_dict['Sex'] = str(input('Sexo: ')).upper().strip()[0]
        if people_registration_dict['Sex'] in 'MF':
            break
        print('ERRO! Digite F ou M, por favor: ')
    people_registration_dict['Age'] = int(input('Idade: '))
    soma += people_registration_dict['Age']
    people_registration_list.append(people_registration_dict.copy())
    people_registration_dict.clear()
    while True:
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if stop in 'SN':
            break
        print('ERRO! Digite S ou N, por favor: ')
    if stop in 'N':
        break
print(f'A) Cadastramos {len(people_registration_list)} pessoas')
media = soma / len(people_registration_list)
print(f'B) A média de idade das pessoas cadastradas é de {media:5.2f}')
print('C)Os nomes das mulheres cadastradas são: ', end=' ')
for p in people_registration_list:
    if p['Sex'] in 'F':
        print(p['Name'], end=' ')
print()
print('D) As pessoas com idade superior a da média:')
for p in people_registration_list:
    if p['Age'] > media:
        for k, v in p.items():
            print(f'_{k} = {v}', end=' ')
print()
