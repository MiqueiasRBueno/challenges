# Crie um programa que faça o computador jogar Jokenpô com você.

# Importação da biblioteca:
from random import choice
from time import sleep

# Título do jogo:
print(f'''\033[1;31m{'=' * 55}\033[m
\033[1;34m{'JOKENPÔ':^55}\033[m
\033[1;31m{'=' * 55}\033[m''')
# tupla com os itens do jogo:
itens = ['PEDRA', 'PAPEL', 'TESOURA']

# Sorteio do computador:
computador = choice(itens)

# Opções do jogo:
print(f'''\033[1;32m{'SUAS OPÇÕES':^55}\033[m
[1] PEDRA
[2] PAPEL
[3] TESOURA
\033[1;31m{'=' * 55}\033[m''')
jogador = int(input('Digite sua opção: '))
sleep(0.85)
print('JO...')
sleep(0.85)
print('JOKEN...')
sleep(0.85)
print('JOKENPÔ!!!')
sleep(0.85)
# Condições para mostrar as mensagens
if computador == 'PEDRA' and jogador == 2:
    print(f'''Computador escolheu "{computador}"
Jogador escolheu "{itens[jogador - 1]}"
\033[1;31m{'=' * 55}\033[m
Jogador ganhou!!!''')
elif computador == 'PAPEL' and jogador == 3:
    print(f'''Computador escolheu "{computador}"
Jogador escolheu "{itens[jogador - 1]}"
\033[1;31m{'=' * 55}\033[m
Jogador ganhou!!!''')
elif computador == 'TESOURA' and jogador == 1:
    print(f'''Computador escolheu "{computador}"
Jogador escolheu "{itens[jogador - 1]}"
\033[1;31m{'=' * 55}\033[m
Jogador ganhou!!!''')
elif computador == itens[jogador - 1]:
    print(f'''O computador escolheu {computador}
Jogador escolheu "{itens[jogador - 1]}"
\033[1;31m{'=' * 55}\033[m
Empatou, tente de novo!!!''')
else:
    print(f'''O computador escolheu {computador}
Jogador escolheu "{itens[jogador - 1]}"
\033[1;31m{'=' * 55}\033[m
O computador ganhou, tente de novo!!!''')
