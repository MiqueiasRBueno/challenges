# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

# Função:
def ficha(name='<desconhecido>', goals=0):
    print(f'O jogador(a) {name} fez {goals} gol(s) no campeonato')


# Programa Principal:
player_name = str(input('Nome do Jogador: ')).title().strip()
amount_goals = str(input(f'Quantidade de gols do jogador {player_name}: '))
if amount_goals.isnumeric():
    amount_goals = int(amount_goals)
else:
    amount_goals = 0
if player_name.strip() == '':
    ficha(goals=amount_goals)
else:
    ficha(player_name, amount_goals)
