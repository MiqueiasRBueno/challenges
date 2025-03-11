# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 'Santo'.

saint_in_ini = (str(input('Em que cidade voçê mora? ')).upper().strip()).split()
if saint_in_ini[0] == 'SANTO':
    print('O nome da cidade que foi digitado começa com Santo?\nSim, começa!')
else:
    print('O nome da cidade que foi digitado começa com Santo?\nNão, não começa!')
