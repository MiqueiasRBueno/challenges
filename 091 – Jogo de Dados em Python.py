# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from operator import itemgetter
from random import randint
from time import sleep

jogo_dados = {'Jogador 01': randint(1, 6), 'Jogador 02': randint(1, 6),
              'Jogador 03': randint(1, 6), 'Jogador 04': randint(1,6)}
ranking = []
print(f'\033[31m{'=' * 30}\033[m')
sleep(0.7)
print(f'{'Jogo De Dados':-^30}')
sleep(0.7)
print(f'\033[31m{'=' * 30}\033[m')
for k, v in jogo_dados.items():
    sleep(0.7)
    print(f'{f'{k} tirou {v}':-^30}')
ranking = sorted(jogo_dados.items(), key=itemgetter(1), reverse=True)
sleep(0.7)
print(f'\033[31m{'=' * 30}\033[m')
sleep(0.7)
print(f'{'Ranking de Jogadores':-^30}')
sleep(0.7)
print(f'\033[31m{'=' * 30}\033[m')
for k, v in enumerate(ranking):
    sleep(0.7)
    print(f'{f'{k + 1}ºLugar: {v[0]} com {v[1]}':-^30}')
print(f'\033[31m{'=' * 30}\033[m')
