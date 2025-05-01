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
