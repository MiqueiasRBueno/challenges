# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
print(f'''\033[1;31m{'=' * 55}\033[m
\033[1m{'JOGO DE ADIVINHAÇÃO':^55}\033[m
\033[1;31m{'=' * 55}\033[m
Sou seu computador, pensei em um número entre 0 e 10.
Será que você consegue adivinhar?''')
palpite = int(input('Qual é o seu palpite? '))
tentativas = 1
while palpite != computador:
    tentativas += 1
    if palpite < computador:
        palpite = int(input('Mais... Tente de novo! '))
    else:
        palpite = int(input('Menos ... Tente de novo! '))
print(f'''\033[1;31m{'=' * 55}\033[m
Parabéns, você acertou com {tentativas} tentativas!''')
