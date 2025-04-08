# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime
ano = datetime.now().year
jovens = velhos = 0
for c in range(1, 8):
    nasceu = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = ano - nasceu
    jovens += idade < 21
    velhos += idade > 21
if jovens > 0:
    print(f'Na lista temos {jovens} menores de 21 anos')
else:
    print('Não temos pessoas menores de 21 anos em nossa lista!')
if velhos > 0:
    print(f'E temos na lista {velhos} maiores de 21 anos')
else:
    print('Não temos pessoas maiores de 21 anos em nossa lista!')
