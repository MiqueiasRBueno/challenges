# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

# dicionário de cores
cores = {'azul':'\033[1;34m', 'limpa': '\033[m', 'vermelho': '\033[1;31m', 'amarelo': '\033[33m'}
# variável de inserção de dados
name = str(input('Digite seu nome completo: ')).strip().split()
# mostra na tela o primeiro nome
print(f'Seu primeiro nome é {cores['amarelo']}{name[0].title()}{cores['limpa']}')
# Caso tenha mais de um some:
if len(name) > 1:
    # mostra o último nome na tela
    print(f'Seu último nome é {cores['vermelho']}{name[-1].title()}{cores['limpa']}')
