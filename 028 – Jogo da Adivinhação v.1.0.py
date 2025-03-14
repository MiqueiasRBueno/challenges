# Escreva um programa que faça o computador “pensar” em um número inteiro entre
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
# computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# dicionário de cores
cores = {'branco': '\033[30m', 'vermelho': '\033[1;31m', 'verde': '\033[32m', 'amarelo': '\033[33m',
         'azul':'\033[1;34m', 'roxo': '\033[35m', 'ciano': '\033[7:36m', 'cinza': '\033[37m', 'limpa': '\033[m'}

# importa a biblioteca
from random import randint

# variável para armazenar o número sorteado
number_sorted = randint(0, 5)

# Interação com o usuário, sugerir que escolha um número entre 0 e 5.
number_user = int(input('Escolha um número entre 0 e 5: '))
# mostra o número sorteado pelo programa
print(f'    Número sorteado pelo computador: {cores['amarelo']}{number_sorted}{cores['limpa']}')
# compara o número sorteado pelo programa com o escolhido pelo usuário
if number_sorted == number_user:
    # se verdadeiro que os números são iguais, mostra essa mensagem
    print(f'''    Número escolhido pelo usuário: {cores['verde']}{number_user}{cores['limpa']}
    {cores['vermelho']}Parabéns, você acertou!{cores['limpa']}''')
# caso número não seja o mesmo
else:
    # imprime essa mensagem na tela
    print(f'''    Número escolhido pelo usuário: {cores['roxo']}{number_user}{cores['limpa']}
    {cores['vermelho']}Não foi dessa vez, tente denovo!{cores['limpa']}''')
