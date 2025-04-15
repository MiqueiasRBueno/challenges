# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print(f'''\033[1;31m{'=' * 55}\033[m
{'VAMOS JOGAR PAR OU IMPAR':^55}
\033[1;31m{'=' * 55}\033[m''')
cont = 0
game_over =' '
while True:
    cont += 1
    player = int(input('Digite um valor: '))
    par_impar = str(input('Você quer par ou ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(1, 10)
    soma = player + computador
    if soma % 2 == 0 and par_impar == 'P':
        print(f'''Você jogou {player} e o computador {computador}
Total de {soma}, \033[1;32mDEU PAR\033[m!!!
\033[1;31m{'=' * 55}\033[m''')
    elif soma % 2 != 0 and par_impar == 'I':
        print(f'''Você jogou {player} e o computador {computador}
Total de {soma}, \033[1;32mDEU ÍMPAR\033[m!!!
\033[1;31m{'=' * 55}\033[m''')
    else:
        game_over = 0
    if game_over == 0:
        break
print(f'''\033[1;31m{'=' * 55}\033[m
{'GAME OVER!!!':^55}
\033[1;31m{'=' * 55}\033[m   
Você perdeu após {cont} partidas jogadas''')