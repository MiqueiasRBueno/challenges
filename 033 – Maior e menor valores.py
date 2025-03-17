# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# dicionário de cores
cores = {'branco': '\033[30m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[33m',
         'azul':'\033[1;34m', 'roxo': '\033[35m', 'ciano': '\033[7;36m', 'cinza': '\033[37m', 'limpa': '\033[m'}

# Variáveis que receberão os maiores e menores valores
biggest = smallest = 0
# Laço de repetição
for c in range(1, 4):
    # Variável para inserção dos dados
    number_biggest_smallest = int(input(f'Digite o \033[1;3{c}m{c}°\033[m número qualquer: '))
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
print(f'''O maior valor digitado foi {cores['azul']}{biggest}{cores['limpa']}
E o menor valor digitado foi o {cores['verde']}{smallest}{cores['limpa']}''')
