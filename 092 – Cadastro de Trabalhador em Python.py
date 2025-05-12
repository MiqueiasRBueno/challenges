#  Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#  Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#  Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: ')).title().strip()
ano_nascimento = int(input('Ano Nascimento: '))
dados['Idade'] = datetime.now().year - ano_nascimento
dados['CTPS'] = int(input('Carteira de Trabalho: (0 não tem CTPS): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano De Contratação: '))
    dados['Sálario:'] = float(input('Sálario: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print(f'\033[1;31m{'=' * 40}\033[m')
for k, v in dados.items():
    print(f'_ {k} tem o valor {v}')
print(f'\033[1;31m{'=' * 40}')