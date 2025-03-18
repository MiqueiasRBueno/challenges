# Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se elas podem ou não formar um triângulo.

# dicionário de cores
cores = {'branco': '\033[30m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[33m',
         'azul':'\033[1;34m', 'roxo': '\033[35m', 'ciano': '\033[1;36m', 'cinza': '\033[37m', 'limpa': '\033[m'}

# seguimentos
segment_a = segment_b = segment_c = 0
# laço para inserção de dados de cada segmento
for c in range(1,4):
    triangle_segment = float(input(f'Digite o {c}º seguimento: '))
    if c == 1:
        segment_a = triangle_segment
        segment_b = triangle_segment
        segment_c = triangle_segment
    else:
        if c == 1:
            segment_a = triangle_segment
        if c == 2:
            segment_b = triangle_segment
        if c == 3:
            segment_c = triangle_segment
if segment_a < segment_b + segment_c and segment_b < segment_a + segment_c and segment_c < segment_a + segment_b:
    print(f'Os seguimentos acima, {cores['verde']}podem formar um triângulo!{cores['limpa']}')
else:
    print(f'Os seguimentos acima, {cores['vermelho']}não podem formar um triângulo!{cores['limpa']}')
