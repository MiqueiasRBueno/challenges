# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

# Função:
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if  n.isnumeric(): # analisa se 'n' é um valor numérico
            valor = n # Se 'n' for um valor numérico, valor = n
            ok = True # ok passa a ser verdadeiro
        else: # se 'n' não for um valor numérico
            print('\033[0;31mERRO! Digite um número válido!\033[m') # Exibe uma mensagem de erro
        if ok: # se tudo ok
            break # finaliza o programa
    return valor # retorna o valor de valor



# Programa principal:
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
