# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

valores_cad = [[], []]
for c in range(0,7):
    numbers = int(input(f'Digite o {c + 1}º valor: '))
    if numbers % 2 == 0:
        valores_cad[0].append(numbers)
    else:
        valores_cad[1].append(numbers)
print(f'''Os valores pares cadastrados em nossa lista são: {sorted(valores_cad[0])}
E os valores impares cadastrados em nossa lista são: {sorted(valores_cad[1])}''')
