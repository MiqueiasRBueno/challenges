# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

print(f'''\033[1;32m{'-=' * 30}\033[m
{'GERENCIAMENTO DE JOGADORES':^60}
\033[1;32m{'-=' * 30}\033[m''')
cad_jogador = dict()
qtd_gols = list()
cad_jogador['Nome'] = str(input('Nome do Jogador e ou Jogadora: ')).title().strip()
qtd_partidas = int(input(f'Quantas partidas o jogador e ou jogadora \033[34m{cad_jogador['Nome']}\033[m jogou? '))
tot = 0
for qtd in range(0, qtd_partidas):
    qtd_gols.append(int(input(f'Quantos gols \033[34m{cad_jogador['Nome']}\033[m na \033[34m{1 + tot}\033[mª'
                              f' partida? ')))
    cad_jogador['Gols'] = qtd_gols
    cad_jogador['Total'] = sum(cad_jogador['Gols'])
    tot += 1

print(cad_jogador)