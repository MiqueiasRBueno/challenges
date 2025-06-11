def aumentar(preco=0, taxa=0):
    """
    _> Função para aumentar uma porcentagem de um valor digitado pelo usuário.
    :param preco: Número a ser aumentado
    :param taxa: valor da porcentagem a ser aumentada
    :return: retorna novo valor com o aumento
    """
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco=0, taxa=0):
    """
    _> Função que diminui uma porcentagem de um valor digitado pelo usuário.
    :param preco: Número a ser diminuído
    :param taxa: valor da porcentagem a ser diminuída
    :return: retorna o novo valor diminuído a porcentagem digitada
    """
    res = preco - (preco * taxa/100)
    return res


def dobro(preco=0):
    """
    _> Dobra um valor digitado pelo usuário
    :param preco: valor digitado pelo usuário para ser dobrado
    :return: retorna o dobro do valor digitado
    """
    res = preco * 2
    return res


def metade(preco=0):
    """
    _> Função que mostra a metade do valor digitado pelo usuário
    :param preco: valor digitado pelo usuário para ser dividido pela metade
    :return: retorna a metade do valor digitado
    """
    res = preco / 2
    return res


def moeda(preco=0, tmoeda='R$'):
    """
    _> Função para formatação monetária
    :param preco: Valor a ser formatado
    :param tmoeda: Moeda corrente
    :return:
    """
    return f'{tmoeda}{preco:^8.2f}'.replace('.', ',')
