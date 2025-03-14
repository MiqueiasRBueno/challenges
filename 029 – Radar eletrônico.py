# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada km acima do limite.

# dicionário de cores
cores = {'branco': '\033[30m', 'vermelho': '\033[1;31m', 'verde': '\033[32m', 'amarelo': '\033[33m',
         'azul':'\033[1;34m', 'roxo': '\033[35m', 'ciano': '\033[7:36m', 'cinza': '\033[37m', 'limpa': '\033[m'}

# interação com o usuário
speed = int(input('Digite a velocidade atual do veículo: '))
# compara se a informação é verdadeira ou falsa
if speed >= 80.1:
    print(f'''    Você foi multado, excedeu o limite de velocidade!
    Velocidade máxima da via {cores['vermelho']}80{cores['limpa']} km
    {cores['amarelo']}Dirija com cuidado!{cores['limpa']}''')
else:
    print(f'''    Meus parabéns, você respeitou os limites de velocidade!
    Velocidade máxima da via {cores['vermelho']}80{cores['limpa']} km
    {cores['amarelo']}Continue assim, respeitando a vida!{cores['limpa']}''')
