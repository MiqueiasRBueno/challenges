# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

ficha = []
while True:
    nome = (str(input('Nome do aluno: ')).title().strip())
    nota_um = (float(input('1ª Nota: ')))
    nota_dois = (float(input('2ª Nota: ')))
    media = (nota_um + nota_dois) / 2
    ficha.append([nome, [nota_um, nota_dois], media])
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if stop in 'N':
        break
print(f'''\033[1;31m{'=' * 50}\033[m
\033[1;m{'Nº':<3}{'NOME':^40}{'NOTA':>7}\033[m
\033[1;31m{'_' * 50}\033[m''')
for i, a in enumerate(ficha):
    print(f'{i + 1:<2}{a[0]:^30}{a[2]:>18.2f}')
print(f'\033[1;31m{'=' * 50}\033[m')
while True:
    print('Para finalizar digite "999"!')
    mostrar = int(input('Escolha o aluno para mostrar as notas: '))
    aluno = mostrar -1
    if aluno == 998:
        print('Finalizando')
        break
    if aluno <= len(ficha) - 1:
        print(f'''\033[1;31m{'=' * 50}\033[m
{'Aluno':<4}{'Notas':>44}
\033[1;31m{'_' * 50}\033[m
{f'{ficha[aluno][0]}':_<40}{ficha[aluno][1]}
\033[1;31m{'=' * 50}\033[m''')
