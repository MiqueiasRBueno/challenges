# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = menor = media = cont = 0
parar = ''
while parar != 'N':
    cont += 1
    number = int(input('Digite um número: '))
    media += number / 2
    parar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < menor:
            menor = number
print(f'''Foram digitados {cont} números
A média dos valores digitados foi {media:.2f}
O maior valor digitado foi {maior}
O menor valor digitado foi {menor}''')
