# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

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


def leiaFloat(msg):
    """
    Função para validação de número reais
    :param msg: Recebe os dados a serem validados
    :return: retorna o valor validado
    """
    ok = False
    valor = 0
    while True:
        num = str(input(msg)).strip().replace(',', '.')
        try:
            valor = float(num)
            ok = True
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o número real foi {real}')