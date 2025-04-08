# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = menor_peso = 0 # Variáveis que recebem os maiores e menores valores

for pessoas in range(1, 6): # Repetição para inserir os dados solicitados
    peso_pessoas = float(input(f'Digite o peso da {pessoas}ª pessoa: '))
    if pessoas == 1:
        maior_peso = menor_peso = peso_pessoas
    else:
        if peso_pessoas > maior_peso:
            maior_peso = peso_pessoas
        if peso_pessoas < menor_peso:
            menor_peso = peso_pessoas
print(f'''O maior peso lido foi {maior_peso} kg
O menor peso lido foi {menor_peso} kg''')
