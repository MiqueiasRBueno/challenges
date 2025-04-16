# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$ 1000.
# C) qual é o nome do produto mais barato.

cont = total = maiores_mil = menor_preco = 0
mais_barato = ' '
print(f'''\033[1;31m{'=' * 55}\033[m
{F'MINI BOX BUENO':^55}
\033[1;31m{'=' * 55}\033[m''')
while True:
    cont += 1
    produto = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço Do Produto: R$ '))
    total += preco
    if cont == 1:
        menor_preco = preco
    else:
        if preco < menor_preco:
            mais_barato = produto
            menor_preco = preco
        if preco > 1000:
            maiores_mil += 1
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if parar == 'N':
        break
print(f'''\033[1;31m{'=' * 55}\033[m
O valor total da compra é de R$ {total:.2f}
Tem(os) {maiores_mil} produto(s) maior(es) de R$ 1000,00
E o produto mais barato é {mais_barato}, custou R$ {menor_preco:.2f}
\033[1;31m{'=' * 55}\033[m''')
