def aumentar(preco=0, taxa=0, formato=False):
    """
    _> Função para aumentar uma porcentagem de um valor digitado pelo usuário.
    :param preco: Número a ser aumentado
    :param taxa: valor da porcentagem a ser aumentada
    :param formato: Função para formatação de moeda
    :return: retorna novo valor com o aumento
    """
    res = preco + (preco * taxa/100)
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    """
    _> Função que diminui uma porcentagem de um valor digitado pelo usuário.
    :param preco: Número a ser diminuído
    :param taxa: valor da porcentagem a ser diminuída
    :param formato: Função para formatação de moeda
    :return: retorna o novo valor diminuído a porcentagem digitada
    """
    res = preco - (preco * taxa/100)
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    """
    _> Dobra um valor digitado pelo usuário
    :param preco: valor digitado pelo usuário para ser dobrado
    :param formato: Função para formatação de moeda
    :return: retorna o dobro do valor digitado
    """
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    """
    _> Função que mostra a metade do valor digitado pelo usuário
    :param preco: valor digitado pelo usuário para ser dividido pela metade
    :param formato: Função para formatação de moeda
    :return: retorna a metade do valor digitado
    """
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco, tmoeda='R$'):
    """
    _> Função para formatação monetária
    :param preco: Valor a ser formatado
    :param tmoeda: Moeda corrente
    :return:
    """
    return f'{tmoeda}{preco:^8.2f}'.replace('.', ',')
