# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests

try:
    url = "https://www.pudim.com.br"
    response = requests.get(url)
    response.raise_for_status()
    print(f'O site Pudim está acessível"')
except requests.exceptions.RequestException as e:
    print(f'O site Pudim não está acessível: \n{e}')



