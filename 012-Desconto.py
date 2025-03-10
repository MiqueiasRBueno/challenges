# Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco_produto = float(input('Qual o valor do produto? R$'))
desconto_produto = preco_produto - (preco_produto * 0.05)
print(f'O preço total do produto é R${preco_produto:.2f}\n'
      f'O preço do produto com 5% de desconto é R${desconto_produto:.2f}')
