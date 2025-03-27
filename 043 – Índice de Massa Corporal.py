# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, conforme a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

# Título do programa
print(f'''\033[1;35m{'=' * 51}\033[m
{' ' * 6}\033[1;34mCALCULADORA DE ÍNDICE DE MASSA CORPORAL\033[m
\033[1;35m{'=' * 51}\033[m''')

# Variável para guardar o peso do cliente:
peso = float(input('Digite o valor de seu peso atual: '))

# Variável para guardar a altura do cliente:
altura = float(input('Digite o valor de sua altura atual: '))
print('\033[1;35m=\033[m' * 51)

# Código para calcúlo do 'IMC'e condições:
if peso / (altura ** 2) <= 18.5:
    print(f'''Peso: {peso:.2f} kg
Altura: {altura:.2f} m
IMC: {peso / (altura ** 2):.2f} kg/m2
\033[1;35m{'=' * 51}\033[m
Você está "\033[1;31mAbaixo do Peso\033[m"!''')
elif 18.5 < peso / (altura ** 2) <= 25:
    print(f'''Peso: {peso:.2f} kg
Altura: {altura:.2f} m
IMC: {peso / (altura ** 2):.2f} kg/m2
\033[1;35m{'=' * 51}\033[m
Você está com o "\033[1;34mPeso Ideal\033[m"!''')
elif 25 < peso / (altura ** 2) <= 30:
    print(f'''Peso: {peso:.2f} kg
Altura: {altura:.2f} m
IMC: {peso / (altura ** 2):.2f} kg/m2
\033[1;35m{'=' * 51}\033[m
Você está com "\033[1;33mSOBREPESO\033[m"!''')
elif 30 < peso / (altura ** 2) <= 40:
    print(f'''Peso: {peso:.2f} kg
Altura: {altura:.2f} m
IMC: {peso / (altura ** 2):.2f} kg/m2
\033[1;35m{'=' * 51}\033[m
Você está com "\033[1;33mOBESIDADE\033[m"!''')
else:
    print(f'''Peso: {peso:.2f} kg
Altura: {altura:.2f} m
IMC: {peso / (altura ** 2):.2f} kg/m2
\033[1;35m{'=' * 51}\033[m
Você está com "\033[1;31mOBESIDADE MÓRBIDA\033[m"!''')
