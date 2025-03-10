# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias locados.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodados.

carro_km_rodados = float(input('Digite quantos quilômetros o veículo rodou: '))
carro_dias_locados = float(input('Digite a quantidade de dias locados: '))
total_pagar = (carro_km_rodados * 0.15) + (carro_dias_locados * 60)
print(f'O total a pagar pela locação do veículo é de R${total_pagar:.2f}')
