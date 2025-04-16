# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extended_number = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
        'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO',
        'DEZENOVE', 'VINTE')
print(f'''\033[1;31m{'='*55}\033[m
{'NÚMERO POR EXTENSO':^55}
\033[1;31m{'='*55}\033[m''')
while True:
        number = int(input('Digite um número entre 0 e 20: '))
        if number not in range(0, 20):
                print(f'{'TENTE DE NOVO!!!':^55}')
        if number in range(0, 20):
                break
print(f'''
Você digitou o número "\033[1;33m{extended_number[number]}\033[m"!''')
