# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

cont = menores = mulheres = homens = 0
while True:
    cont += 1
    print(f'''\033[1;31m{'=' * 55}\033[m
{F'CADASTRE A {cont}ª PESSOA':^55}
\033[1;31m{'=' * 55}\033[m''')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:[M/F] ')).strip().upper()[0]
    menores += idade < 18
    mulheres += idade < 20 and sexo == 'F'
    homens += sexo == 'M'
    parar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if parar not in 'S':
        break
print(f'''\033[1;31m{'=' * 55}\033[m
Nos temos {menores} menores de 18 anos cadastrados
Temos {homens} homens cadastrados
Temos {mulheres} mulheres menores de 20 anos cadastradas''')
