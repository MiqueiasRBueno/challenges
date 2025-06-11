def aumentar(n, per):
    """
    _> Função para aumentar uma porcentagem de um valor digitado pelo usuário.
    :param n: Número a ser aumentado
    :param per: valor da porcentagem a ser aumentada
    :return: retorna novo valor com o aumento
    """
    return n + ((n * per) / 100)

def diminuir(n, per):
    """
    _> Função que diminui uma porcentagem de um valor digitado pelo usuário.
    :param n: Número a ser diminuído
    :param per: valor da porcentagem a ser diminuída
    :return: retorna o novo valor diminuído a porcentagem digitada
    """
    return n - ((n * per) / 100)

def dobro(n):
    """
    _> Dobra um valor digitado pelo usuário
    :param n: valor digitado pelo usuário para ser dobrado
    :return: retorna o dobro do valor digitado
    """
    return n * 2

def metade(n):
    """
    _> Função que mostra a metade do valor digitado pelo usuário
    :param n: valor digitado pelo usuário para ser dividido pela metade
    :return: retorna a metade do valor digitado
    """
    return n / 2
