# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    — > Função fatorial de um número
    :param num: Número para fatoração
    :param show: Se verdadeiro mostra a fatoração por extenso
    :return: Retorna o resultado da fatoração.
    """
    from time import sleep
    ft = 1
    if show:
        print(f'{num}! = ', end=' ')
    for c in range(num, 0, -1):
        ft *= c
        if show:
            print(c, end=' ')
            sleep(0.4)
            if c > 1:
                print('X', end=' ')
            else:
                print('=', end=' ')
    return ft



# Programa principal:
print(fatorial(5, True))
