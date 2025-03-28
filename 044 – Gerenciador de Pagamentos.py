# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/Pix: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print(f'''\033[1;32m{'=' * 65}\033[m
{' ' * 18}\033[1;33mEscolha a forma de pagamento:\033[m
\033[1;32m{'=' * 65}\033[m''')
preco_produto = float(input('Digite o valor do produto: '))
print(f'''\033[1;32m{'=' * 65}\033[m
[1] Para pagamento à vista em dinheiro / Pix: Com 10% de desconto
[2] Para pagamento à vista no cartão: Com 5% de desconto
[3] Para pagamento em até 2X no cartão: Preço formal
[4] Para pagamento em 3X ou mais no cartão: 20% de juros
''')
forma_pagamento = int(input('Escolha uma das formas de pagamento possíveis: '))
print(f'''\033[1;32m{'=' * 65}\033[m''')
if forma_pagamento == 1:
    print(f'''A forma escolhida foi à vista [dinheiro/ Pix]
Você terá um desconto de 10% sobre o valor do produto
Preço Formal_________________R$ {preco_produto:.2f}
Desconto_____________________R$ \033[4m{preco_produto * 0.1:.2f}\033[m
Total a Pagar com desconto___R$ {preco_produto - (preco_produto * 0.1):.2f}
\033[1;32m{'=' * 65}\033[m''')
elif forma_pagamento == 2:
    print(f'''A forma escolhida foi à vista no cartão
Você terá um desconto de 5% sobre o valor do produto
Preço Formal_________________R$ {preco_produto:.2f}
Desconto_____________________R$ \033[4m{preco_produto * 0.05:.2f}\033[m
Total a Pagar com desconto___R$ {preco_produto - (preco_produto * 0.05):.2f}
\033[1;32m{'=' * 65}\033[m''')
elif forma_pagamento == 3:
    print(f'''A forma escolhida foi em 2x no cartão
Você pagará o preço formal
Preço Formal_________________R$ {preco_produto:.2f}
Desconto_____________________R$ \033[4m00.00\033[m
Total a Pagar________________R$ {preco_produto:.2f}
\033[1;32m{'=' * 65}\033[m''')
elif forma_pagamento == 4:
    print(f'''A forma escolhida foi parcelado no cartão
Você terá um acréscimo de 20% sobre o valor do produto
Preço Formal_________________R$ {preco_produto:.2f}
Desconto_____________________R$ \033[4m{preco_produto * 0.20:.2f}\033[m
Total a Pagar com desconto___R$ {preco_produto + (preco_produto * 0.20):.2f}
\033[1;32m{'=' * 65}\033[m''')
print('Obrigado pela preferência, volte sempre!')
