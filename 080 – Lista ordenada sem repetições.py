# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

value_list = []
for c in range (0,5):
    num = (int(input('Digite um valor: ')))
    if num not in value_list:
        if c == 0:
            value_list.append(num)
            print('Este valor será adicionado no final da lista!')
        elif num > value_list[-1]:
            value_list.append(num)
            print('Este valor será adicionado ao final da lista!')
    else:
        pos = 0
        while pos < len(value_list):
            if num <= value_list[pos]:
                value_list.insert(pos, num)
                print(f'Este valor foi adicionado no {pos} da lista')
                break
            pos += 1
print(value_list)

print(f'''\033[1;31m{'='*55}\033[m
{'LISTA ORDENADA SEM REPETIÇÕES':^55}
\033[1;31m{'='*55}\033[m''')
value_list = []
for c in range(0,5):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num not in value_list:
        if c == 0:
            value_list.append(num)
            print('Valor adicionado ao final da lista com sucesso!')
        elif num > value_list[-1]:
            value_list.append(num)
            print('Valor adicionado ao final da lista com sucesso!')
        else:
            pos = 0
            while pos < len(value_list):
                if num <= value_list[pos]:
                    value_list.insert(pos, num)
                    print(f'Este valor foi adicionado na {pos} da lista!')
                    break
                pos += 1
print(f'''\033[1;31m{'='*55}\033[m
{f'Os valores digitados foram: {value_list}':^55}
\033[1;31m{'='*55}\033[m''')
