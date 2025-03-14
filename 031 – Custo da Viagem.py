# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200Km e R$ 0,45 parta viagens mais longas.

# dicionário de cores
cores = {'branco': '\033[30m', 'vermelho': '\033[1;31m', 'verde': '\033[32m', 'amarelo': '\033[33m',
         'azul':'\033[1;34m', 'roxo': '\033[35m', 'ciano': '\033[7:36m', 'cinza': '\033[37m', 'limpa': '\033[m'}

# interação com o usuário
travel_distance = int(input('Digite a distância de sua viagem: '))
# compara as informações
if travel_distance <= 200:
    # calcula o valor da passagem até 200 km
    ticket_value = (travel_distance * 0.50)
    # mostra a mensagem para viagens até 200 km
    print(f'''Sua viagem tem a distância de {cores['roxo']}{travel_distance:.2f}{cores['limpa']} km
A viagem lhe custará o valor de R$ {cores['verde']}{ticket_value:.2f}{cores['limpa']}
{cores['amarelo']}Tenha uma boa viagem, volte sempre!{cores['limpa']}''')
else:
    # calcula o valor da passagem para viagens maiores que 200 km
    ticket_value_2 = (travel_distance * 0.45)
    # mostra a mensagem para viagens maiores que 200 km
    print(f'''Sua viagem tem a distância de {cores['roxo']}{travel_distance:.2f}{cores['limpa']} km
    A viagem lhe custará o valor de R$ {cores['verde']}{ticket_value_2:.2f}{cores['limpa']}
    {cores['amarelo']}Tenha uma boa viagem, volte sempre!{cores['limpa']}''')
