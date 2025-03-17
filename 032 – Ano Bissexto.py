# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# dicionário de cores
cores = {'branco': '\033[30m', 'vermelho': '\033[1;31m', 'verde': '\033[32m', 'amarelo': '\033[33m',
         'azul':'\033[1;34m', 'roxo': '\033[35m', 'ciano': '\033[7:36m', 'cinza': '\033[37m', 'limpa': '\033[m'}

# interação com os usuário
leap_year = int(input('Digite o ano que deseja saber se é bissexto: '))
# analisa se o ano é bissexto
if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
    # mostra a mensagem se um ano é bissexto
    print(f'{cores['azul']}O ano de{cores['limpa']}{cores['verde']} {leap_year}{cores['limpa']} {cores['azul']}é um ano bissexto.{cores['limpa']}')
# analisa se o ano não é bissexto
else:
    # mensagem caso o ano não seja bissexto
    print(f'{cores['azul']}O ano de {cores['limpa']}{cores['verde']}{leap_year}{cores['limpa']} {cores['azul']}não é um ano bissexto{cores['limpa']}')
