# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/Pix: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print(f'\033[1;32m{'=' * 65}\033[m')
preco_produto = float(input('Digite o valor do produto: '))
print(f'''\033[1;32m{'=' * 65}\033[m
{' ' * 18}\033[1mEscolha a forma de pagamento:\033[m
\033[1;32m{'=' * 65}\033[m
[1] Para pagamento à vista em dinheiro / Pix: Com 10% de desconto
[2] Para pagamento à vista no cartão: Com 5% de desconto
[3] Para pagamento em até 2X no cartão: Preço formal
[4] Para pagamento em 3X ou mais no cartão: 20% de juros
''')
forma_pagamento = int(input('Escolha uma das formas de pagamento possíveis: '))
print(f'''\033[1;32m{'=' * 65}\033[m
A forma escolhida foi à vista [dinheiro/ Pix]''')
if forma_pagamento == 1:
    print(f'''Você terá um desconto de 10% sobre o valor do produto
Preço Formal R$ {preco_produto:.2f}
Total a Pagar com desconto R$ {preco_produto - (preco_produto * 0.10)}
\033[1;32m{'=' * 65}\033[m''')
