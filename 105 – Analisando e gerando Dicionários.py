# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

# Dicionário:
classe = dict()

# Função:
def notas(*num, show=False):
    tot = maior = menor = soma = 0
    for i, n in enumerate(num):
        tot += 1
        soma += n
        classe['Total'] = tot
        if i < 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    classe['Maior'] = maior
    classe['Menor'] = menor
    media = soma / len(num)
    classe['Média'] =  f'{media:.2f}'
    if show:
        if media < 5:
            classe['Situação'] = 'Ruim!'
        if media < 7:
            classe['Situação'] = 'Boa!'
        if media >= 7:
            classe['Situação'] = 'Ótima!'

    return classe


# Programa principal
classe = notas(0, 4, 5, 6, 8, 9, show=True)
print(classe)
