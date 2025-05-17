# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores_dicio = dict()
jogadores_lista = list()
num_gols = []
while True:
    while True:
        jogadores_dicio['Nomes'] = str(input('Nomes do jogador e ou jogadora: ')).title().strip()
        num_partidas = int(input(f'Quantas partidas o jogador e ou jogadora {jogadores_dicio["Nomes"]} jogou?: '))
        for np in range(0, num_partidas):
            jogadores_dicio['Gols'] = int(input(f'Quantos gols {jogadores_dicio["Nomes"]} marcou na {np + 1}ª partida?: '))
            num_gols.append(jogadores_dicio.copy()['Gols'])
            jogadores_dicio['Total'] = sum(num_gols)
        jogadores_lista.append(jogadores_dicio.copy())
        jogadores_dicio.clear()
        while True:
            stop = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
            if stop in 'SN':
                break
            print('ERRO! Digite S ou N/: ')
        if stop in 'N':
            break
    print(f'\033[1;32m{"-=" * 27}\033[m')
    print(f'{"_CÓD":<10}{"NOME":^8}{"GOLS":^15}{"TOTAL":>20}')
    for i, j in enumerate(jogadores_lista):
        print(f' {i:<5}{j["Nomes"]:^10}{f'{num_gols}':^18}{j["Total"]:>20}')
    print('-=' * 27)
    print(f' __LEVANTAMENTO DO JOGADOR E OU JOGADORA {jogadores_lista[0]["Nomes"]}:')
    print()
    jogo = 0
    for g in num_gols:
        print(f'\t\tNo {1 + jogo}° jogo {jogadores_lista[0]["Nomes"]} fez {g} gols')
        jogo += 1
    if stop == 999:
        break