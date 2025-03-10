# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

din_carteira = float(input('Quanto dinheiro você possui em sua carteira? '))
dollars = float((input('Digite a cotação do dollar atual: ')))
qtd_dollars = (din_carteira / dollars)
print(f'Com R${din_carteira:.2f} você consegue comprar US${qtd_dollars:.2f} ')
