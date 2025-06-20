# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

# Função:
def notas(*num, show=False):
    """
        — > A função notas é um programa para analisar notas de vários alunos
        :param num: recebe os números adicionados
        :param show: se verdadeiro mostra a situação da média das notas da classe
        :return: retorna um dicionário com os dados adicionados
        """
    classe = dict()
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
        if media > 5:
            classe['Situação'] = 'Boa!'
        if media >= 7:
            classe['Situação'] = 'Ótima!'

    return classe


# Programa principal
resp = notas(10, 4, 5, 10, 8, 9, show=True)
print(resp)
