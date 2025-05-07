# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
sorteio = []
mega = []
qtd = int(input('Quantos jogos deseja fazer?: '))
total = 1
while total <= qtd:
    cont = 0
    while True:
        number = randint(1, 60)
        if number not in sorteio:
            sorteio.append(number)
            cont += 1
        if cont >= 6:
            break
    sorteio.sort()
    mega.append(sorteio[:])
    sorteio.clear()
    total += 1
for jog, dez in enumerate(mega):
    print(f'\033[1;34m{jog + 1}º\033[m \033[1;31mJogo:\033[m {dez}')