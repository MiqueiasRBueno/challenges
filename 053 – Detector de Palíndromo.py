# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# Entrada de dados digitados pelo usuário, . strip() desconsidera espaços a direita e a esquerda, .upper() passa tudo
# para maiúsculo e .replace(' ', '') tira os espaços entre as palavras:

palin = str(input("Digite um a Frase: ")).strip().upper()
no_space = palin.replace(' ', '')
palin_joi = ''.join(no_space) # Reverte o conteúdo da variável de trás para frente
palavras = ''

for letras in range(len(palin_joi) - 1, -1, -1): # Para cada letra digitada,
    palavras += palin_joi[letras] # Ele insere na variável 'palavras', de tras para frente, uma por uma.
if palavras == no_space: # Se verdadeiro que as duas variáveis são iguais,
    print(f'''A frase \033[1;34m{palin}\033[m, é um "\033[1;34mPALÍNDROMO"!\033[m''') # O programa imprimi esta frase
else: # Se for falsa,
    print(f'A frase \033[1;31m{palin}\033[m, não é um "\033[1;31mPALÍNDROMO\033[m"!') # O programa imprimi esta frase
