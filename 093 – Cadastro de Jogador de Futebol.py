# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

print(f'''\033[1;32m{'-=' * 30}\033[m
{'Gerenciamento de Jogadores' :^60}
\033[1;32m{'-=' * 30}\033[m''')
ger_jogadores = dict()
qtd_gols = list()
ger_jogadores['Nome'] = str(input('Nome do jogador e ou jogadora: ')).title().strip()
qtd_partida = int(input(f'Quantas partidas \033[32m{ger_jogadores['Nome']}\033[m jogou? '))
print('\033[32m-=\033[m' * 30)
for q in range(0, qtd_partida):
    qtd_gols.append(int(input(f'Quantos gols \033[32m{ger_jogadores['Nome']}\033[m'
                              f' marcou na \033[32m{q + 1}\033[mª partida? ')))
    ger_jogadores['Gols'] = qtd_gols
    ger_jogadores['Total'] = sum(qtd_gols)
for k, v in ger_jogadores.items():
    print(f'O valor \033[32m{k}\033[m recebe o valor \033[32m{v}\033[m')
print(f'''\033[32m{'-=' * 30}\033[m
{'Número de Gols Por partida e Média':^60}
\033[32m{'-=' * 30}\033[m''')
tot = 0
for c in qtd_gols:
    print(f'O jogador marcou \033[32m{c}\033[m gols na \033[32m{1 + tot}\033[mª partida')
    tot += 1
print(f'O jogador \033[32m{ger_jogadores['Nome']}\033[m marcou uma média '
      f'de \033[32m{sum(qtd_gols) / qtd_partida:.2f}\033[m gols por partida!')
print('\033[32m-=\033[m' * 30)
