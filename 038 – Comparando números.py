# Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

# dicionário de cores
cores = {'branco': '\033[1;30m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m',
         'azul':'\033[1;34m', 'roxo': '\033[1;35m', 'ciano': '\033[7:36m', 'cinza': '\033[1;37m', 'limpa': '\033[m'}

# Lista com os valores digitados pelo usuário
num = []

# Título do programa
print(f'''{' ' * 20}{cores['amarelo']}Comparando Números{cores['limpa']}
{cores['azul']}{'=' * 58}{cores['limpa']}''')

# Laço de repetição para interação com o usuário
for c in range(1, 3):
    value = int(input(f'Digite o {c}° valor inteiro: '))
    num.append(value)

# Compara os valores digitados e mostra a mensagem para o usuário
if num[0] > num[1]:
    print(f'''{cores['azul']}{'=' * 58}{cores['limpa']}
O primeiro valor digitado é maior que o segundo.
{cores['azul']}{'=' * 58}{cores['limpa']}''')
elif num[0] < num[1]:
    print(f'''{'\033[1;34m=\033[m' * 58}
O segundo valor digitado é maior que o primeiro!
{cores['azul']}{'=' * 58}{cores['limpa']}''')
else:
    print('Não existe valor maior, os dois são iguais')
print(f'''O primeiro valor digitado foi {num[0]}
O segundo valor digitado foi {num[1]}
{cores['azul']}{'=' * 58}{cores['limpa']}''')
