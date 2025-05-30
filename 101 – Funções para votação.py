# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(nascimento):
    """
    Está função verifica se está em idade eleitoral.
    :param nascimento: Recebe o ano de nascimento
    :return: Apresenta o resultado
    """
    from datetime import datetime

    ano = datetime.now().year
    idade = ano - nascimento
    if idade < 16:
        return f'Com a idade de {idade} anos: NÃO VOTA!'
    elif 16 <= idade <= 18 or idade > 65:
        return f'Com a idade de {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com a idade de {idade} anos: VOTO OBRIGATÓRIO!'


# Programa Principal:

nasc = int(input('Digite a data de nascimento: '))
print(voto(nasc))
