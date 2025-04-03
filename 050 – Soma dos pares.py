# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = cont = 0
numbers = []
for c in range(1, 7):
    numbers_pairs = int(input(f'Digite o {c}º número: '))
    numbers.append(numbers_pairs)
    if numbers_pairs % 2 == 0:
        soma += numbers_pairs
        cont += 1
print(f'Os números digitados foram {numbers}')
if cont > 0:
    print(f'''O valor dos números pares somados é {soma} 
Você informou {cont} número(s) pare(s)!''')
else:
    print('Você não digitou nenhum número par!')
