def is_float(txt):
    """
    Função para verificar se a string pode ser convertida para float
    :param txt: string com os dados a serem analisados
    :return: retorna verdadeiro ou falso
    """
    try:
        float(txt)
        return True
    except ValueError:
        return False


def leiaDinheiro(txt):
    """
    Função para validar moedas
    :param txt: Dados para ser validado
    :return: Dados validados
    """
    ok = False
    valor = 0
    while True:
        dinh = str(input(txt)).strip().replace(',', '.')
        if is_float(dinh):
            valor = float(dinh)
            ok = True
        else:
            print(f'ERRO! "{dinh}" não é um valor válido!')
        if ok:
            break
    return valor
