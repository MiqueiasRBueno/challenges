# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores_dicio = dict()
jogadores_lista = list()
num_gols = []
def linhas():
    print(f'\033[1;32m{"-=" * 27}\033[m')



while True:
    jogadores_dicio['Nomes'] = str(input('Nomes do jogador e ou jogadora: ')).title().strip()
    num_partidas = int(input(f'Quantas partidas o jogador e ou jogadora {jogadores_dicio["Nomes"]} jogou?: '))
    for np in range(0, num_partidas):
        num_gols.append(int(input(f'Quantos gols {jogadores_dicio["Nomes"]} marcou na {np + 1}ª partida?: ')))
        jogadores_dicio['Gols'] = num_gols[:]
        jogadores_dicio['Total'] = sum(num_gols)
    jogadores_lista.append(jogadores_dicio.copy())
    jogadores_dicio.clear()
    num_gols.clear()
    while True:
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if stop in 'SN':
            break
        print('ERRO! Digite S ou N/: ')
    if stop in 'N':
        break
linhas()
print(f'{"_CÓD":<10}{"NOME":^8}{"GOLS":^15}{"TOTAL":>20}')
for i, j in enumerate(jogadores_lista):
    print(f' {i:<5}{j["Nomes"]:^15}{f'{j["Gols"]}':^13}{j["Total"]:^35}')
linhas()
while True:
    mostrar = int(input('Mostrar dados de qual jogador (999 Para parar): '))
    if mostrar == 999:
        break
    if mostrar >= len(jogadores_lista):
        print(f'ERRO! Não existe jogador e ou jogadora com o código {mostrar}!')
    else:
        linhas()
        print(f' __LEVANTAMENTO DO JOGADOR E OU JOGADORA {jogadores_lista[mostrar]["Nomes"]}:')
        partida = 0
        for g in jogadores_lista[mostrar]['Gols']:
            print(f'No {1 + partida}ª jogo ele fez {g} gols')
            partida += 1
    linhas()
print(f'\n{'\033[1;32m<<\033[mVolte Sempre!\033[1;32m>>\033[m':^70}')
