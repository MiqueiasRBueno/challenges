# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# dicionário de cores
cores = {'branco': '\033[30m', 'vermelho': '\033[1;31m', 'verde': '\033[32m', 'amarelo': '\033[33m',
         'azul':'\033[1;34m', 'roxo': '\033[35m', 'ciano': '\033[7:36m', 'cinza': '\033[37m', 'limpa': '\033[m'}

# interação com o usuário
number_even_odd = int(input('Digite um número inteiro: '))

# Verifica se ou número é impar ou par
if number_even_odd % 2 == 0:
    # mostra na tela a resposta se número par
    print(f'O número {cores['verde']}{number_even_odd}{cores['limpa']}, é um número par!')
else:
    # mostra na tela a resposta se número ímpar
    print(f'O número {cores['vermelho']}{number_even_odd}{cores['limpa']}, é um número ímpar!')