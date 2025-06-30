# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests

def verificar_pudim():
    url = "http://www.pudim.com.br"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f'O site {url} está acessível"')
    except requests.exceptions.RequestException as e:
        print(f'O site {url} não está acessível: \n{e}')


if __name__ == '__main__':
    verificar_pudim()