# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

# Criação dos parâmetros da função:
def escreva(txt):
    tam = len(txt) + 4
    print(f'''\033[1;32m{"-" * tam}\033[m
\33[1;31m{txt.title():^{tam}}\033[m
\033[1;32m{"-" * tam}''')


# Programa principal:
escreva('rio preto acessórios')
