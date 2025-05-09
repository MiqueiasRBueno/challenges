# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

boletim = dict()
boletim['nome'] = str(input('Nome: ')).title().strip()
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['media'] <= 5:
    boletim['situacao'] = 'Reprovado'
elif 7 > boletim['media'] > 5:
    boletim['situacao'] = 'Recuperação'
else:
    boletim['situacao'] = 'Aprovado'
print(f'\033[1;31m{'=' * 55}\033[m')
for k, v in boletim.items():
    print((f'-{k}').title(), (f'é igual a {v}'))
print(f'\033[1;31m{'=' * 55}\033[m')
