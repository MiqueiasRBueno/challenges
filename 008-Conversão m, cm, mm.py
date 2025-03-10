# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input('Digite um valor: ', ))
valor_cent = (valor * 100)
valor_mil = (valor * 1000)
print(f'{valor} metro(s) tem:\n{valor_mil} milímetro(s)\n{valor_cent} centímetro(s)')