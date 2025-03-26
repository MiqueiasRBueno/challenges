# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, conforme a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

# importa o módulo date da biblioteca date
from datetime import date

# variável para armazenar o ano atual
data = date.today().year

# variável para inserir o ano de nascimento do atleta
ano_nasce = int(input('Digite o ano que o atleta nasceu: '))
# Bloco de condições para classificação dos atletas
if data - ano_nasce < 9:
    print(f'''O atleta tem apenas \033[1;34m{data - ano_nasce}\033[m anos
Portanto ele é da categoria "\033[1;34mMIRIM\033[m"!''')
elif 9 <= data - ano_nasce < 14:
    print(f'''O atleta tem apenas \033[1;33m{data - ano_nasce}\033[m anos
Portanto ele é da categoria "\033[1;33mINFANTIL\033[m"!''')
elif 14 <= data - ano_nasce < 19:
    print(f'''O atleta tem apenas \033[1;32m{data - ano_nasce}\033[m anos
Portanto ele é da categoria "\033[1;32mJUNIOR\033[m"!''')
elif 19 <= data - ano_nasce < 25:
    print(f'''O atleta já completou \033[1;33m{data - ano_nasce}\033[m anos
Portanto ele pertence a categoria "\033[1;33mSÊNIOR\033[m"!''')
else:
    print(f'''O atleta já completou \033[1;31m{data - ano_nasce}\033[m anos
Portanto ele é da categoria "\033[1;31mMASTER\033[m"!''')