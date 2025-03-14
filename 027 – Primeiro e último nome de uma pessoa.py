# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

cores = {'azul':'\033[1;34m', 'limpa': '\033[m', 'vermelho': '\033[1;31m', 'amarelo': '\033[33m'}
name = str(input('Digite seu nome completo: ')).strip().split()
print(f'Seu primeiro nome é {cores['amarelo']}{name[0].title()}{cores['limpa']}')
if len(name) > 1:
    print(f'Seu último nome é {cores['vermelho']}{name[-1].title()}{cores['limpa']}')
