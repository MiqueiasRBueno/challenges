def leiaInt(msg):
    """
    Função para validaçâo de números inteiro
    :param msg: Recebe os dados para serem validados
    :return: retorna o valor validado
    """
    ok = False  # Enquanto ok for falso, programa entra em loop
    valor = 0  # Variável declarada com valor inicial 0
    while True:  # loop infinito
        num = str(input(msg))  # variável para receber o valor digitado
        try:  # analisa se 'n' é um valor numérico
            valor = int(num)  # Se 'n' for um valor numérico, valor recebe 'n'
            ok = True  # ok passa a ser verdadeiro
        except ValueError:  # se 'n' não for um valor numérico
            print('\033[0;31mERRO! Digite um número válido!\033[m')  # Exibe uma mensagem de erro
        if ok:  # se tudo ok
            break  # finaliza o programa
    return valor  # retorna o valor de valor

def linha(tam=42):
    return '\033[31m-\033[m' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[m\033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Digite sua opção: ')
    return opc
