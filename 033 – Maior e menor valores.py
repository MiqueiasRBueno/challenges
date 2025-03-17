# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

biggest = smallest = 0
# Laço de repetição
for c in range(1, 4):
    # Variável para inserção dos dados
    number_biggest_smallest = float(input(f'Digite o {c}° número qualquer: '))
    # Analisa se é o primeiro dado inserido
    if c == 1:
        # as variáveis menor e maior recebem os dados digitados pelo usuário
        biggest = number_biggest_smallest
        smallest = number_biggest_smallest
    else:
        # compara se o número digitado é maior e coloca na variável maior
        if number_biggest_smallest > biggest:
            biggest = number_biggest_smallest
        # compara se o número digitado é o menor e coloca na variável menor
        if number_biggest_smallest < smallest:
            smallest = number_biggest_smallest
print(f'''{biggest}
{smallest}''')