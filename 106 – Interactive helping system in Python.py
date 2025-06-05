# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

# Função:
def intHelp():
    """
    • > Função mini-sistema que utiliza o interactive help do Python
    :return: A documentação da função ou biblioteca desejada
    """
    print(f'''\033[1;42m{"-" * 40}
{"SISTEMA DE AJUDA PYTON HELP":^40}
{"-" * 40}
\033[m''', end='')
    while True:
        msg = str(input('Função ou Biblioteca>> '))
        if msg in 'fim':
            break
        print(f'''\033[1;43m{"-" * 40}
{f"Acessando a documentação de '{msg}'":^40}
{"-" * 40}
\033[m''', end='''\033[40;7m''')
        help(msg)
        print('\033[m', end='')
    print(f'''\033[1;41m{"-" * 40}
{"ATÉ LOGO!":^40}
{"-" * 40}
\033[m''')
    return help


# Programa principal:
intHelp()
