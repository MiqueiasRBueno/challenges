# Faça um programa que leia o ano de nascimento de um jovem e informe,
# conforme a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Importa a biblioteca date e math
from datetime import date
from math import floor

print(f'''\033[1;32m{'=' * 58}
{' ' * 19}\033[m\033[1;36mALISTAMENTO MILITAR\033[m\033[1;32m
{'=' * 58}\033[m''')

# Variável para inserir os dados do ano de nascimento do candidato a alistamento militar.
print('\033[1;32m=\033[m' * 58)
day_of_birth = int(input('Digite o dia que você nasceu: '))
month_of_birth = int(input('Digite o mês que você nasceu: '))
year_of_birth = int(input('Digite o ano que você nasceu: '))
print('\033[1;32m=\033[m' * 58)
sex = ' '
while sex not in 'FM':
    sex = str(input('''Digite seu sexo:
    [F] Feminino
    [M] Masculino
    => ''')).upper().strip()
    if sex == 'FM':
        break
print('\033[1;32m=\033[m' * 58)
date_now = date.today()
date_of_birth = date(year_of_birth, month_of_birth, day_of_birth)
difference_age = date_now - date_of_birth
day = difference_age.days
year = day / 365.25
age_floor = floor(year)
if age_floor == 18 and sex == 'M':
    print(f'''Você completou {age_floor} este ano.
Compareça a uma junta militar para se alistar!''')
elif age_floor < 18 and sex == 'M':
    print(f'''Você tem apenas {age_floor} ainda não completou a idade para alistamento militar.
Faltam {18 - age_floor} anos para atingir a idade, aguarde completar 18 anos e procure a junta militar''')
elif age_floor > 18 and sex == 'M':
    print(f'''Você tem {age_floor} anos.
{' ' * 10}\033[1;33mA idade máxima para o alistamento varia de acordo com a situação do cidadão:\033[m

\033[1;33m45 anos:\033[m Para brasileiros natos ou naturalizados que não tenham se alistado no ano em que completaram 18 anos.

\033[1;32m35 anos:\033[m Para brasileiros natos ou naturalizados que perderam o
         prazo de alistamento e desejam ingressar nas Forças Armadas.

\033[1;31m24 anos:\033[m Para portadores de necessidades especiais.

Se você se enquadra em alguma das situações acima:
Compareça ao exército ou a junta militar' de sua cidade.''')
