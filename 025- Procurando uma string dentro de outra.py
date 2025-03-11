# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

name_people = str(input('Qual é seu nome completo? ')).upper().strip()
if 'SILVA' in name_people:
    print('Seu nome tem "Silva"?\nSim, meu nome tem Silva!')
else:
    print('Seu nome tem "Silva"?\nNão, meu nome não tem Silva!')
