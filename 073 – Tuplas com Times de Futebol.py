# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.

brazilian_table = ('Flamengo', 'Palmeiras', 'Ceará', 'Juventude', 'Fluminense', 'Vasco', 'Internacional', 'Fortaleza',
                   'Corinthians', 'Botafogo', 'RedBull', 'Cruzeiro', 'Grêmio', 'Bahia', 'São Paulo', 'Atlético- MG',
                   'Mirassol', 'Santos', 'Vitória', 'Sport' )
print(f'''\033[1;31m{'='*68}\033[m
{'TABELA DOS TIMES DO BRASILEIRÃO':^68}
\033[1;31m{'='*68}\033[m

{f'{brazilian_table[:5]}':^68}
{f'{brazilian_table[5:10]}':^68}
{f'{brazilian_table[10:15]}':^68}
{f'{brazilian_table[15:20]}':^68}

\033[1;31m{'='*68}\033[m
{'CINCO PRIMEIROS TIMES DO BRASILEIRÃO':^68}
\033[1;31m{'='*68}\033[m

{f'{brazilian_table[:5]}':^68}

\033[1;31m{'='*68}\033[m
{'QUATRO ÚLTIMOS TIMES DO BRASILEIRÃO':^68}
\033[1;31m{'='*68}\033[m
{f'{brazilian_table[16:20]}':^68}

\033[1;31m{'='*68}\033[m
{'TIMES DO BRASILEIRÃO EM ORDEM ALFABÉTICA':^68}
\033[1;31m{'='*68}\033[m
{f'{sorted(brazilian_table)}':^68}''')
