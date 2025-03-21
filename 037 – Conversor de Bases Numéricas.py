# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# Entrada de dados com a interação do usuário:
print(f'''{' ' * 17}\033[1;34mCONVERSOR DE BASES NUMÉRICAS\033[m
{'\033[1;32m=\033[m' * 63}''')
number = int(input('Digite um número inteiro qualquer: '))
print(f'''{'\033[1;32m=\033[m' * 63}
Selecione a opção que desejar para converter o número digitado:

[1] - Para converter em binário
[2] - Para converter em octal
[3] - Para converter em hexadecimal

{'\033[1;32m=\033[m' * 63}''')
option = int(input('''Digite uma das opções de 1 a 3: '''))
print('\033[1;32m=\033[m' * 63)
if option not in range(1, 4):
    option = int(input('Tente outra vez: '))
    print('\033[1;32m=\033[m' * 63)
elif option == 1:
    print(f'O número {number} convertido em binário é {bin(number)}')
elif option == 2:
    print(f'O número {number} convertido em octal é {oct(number)}')
elif option == 3:
    print(f'O número {number} convertido em hexadecimal é {hex(number)}')
print('\033[1;32m=\033[m' * 63)
