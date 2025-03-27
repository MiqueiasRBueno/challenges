# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

# variáveis com as medidas dos seguimentos do triângulo.
segment_a = segment_b = segment_c = 0
# variáveis para inserir os dados para análiso do triângulo.
for c in range(1,4):
    triangle_segment = float(input(f'Digite a medida do \033[1;3{c + 1}m{c}\033[mº lado do triângulo: '))
    if c == 0:
        segment_a = triangle_segment
        segment_b = triangle_segment
        segment_c = triangle_segment
    else:
        if c== 1:
            segment_a = triangle_segment
        if c== 2:
            segment_b = triangle_segment
        if c== 3:
            segment_c = triangle_segment
if segment_a == segment_b == segment_c:
    print(f'''Seguimento \033[1;32mA\033[m: {segment_a}
Seguimento \033[1;33mB\033[m: {segment_b}
Seguimento \033[1;34mC\033[m: {segment_c}
Este é um triângulo "\033[1;32mEQUILÁTERO\033[m", pois seus lados são todos iguais! ''')
elif segment_a == segment_b != segment_c or segment_b == segment_c != segment_a or segment_c == segment_a != segment_b:
    print(f'''Seguimento \033[1;32mA\033[m: {segment_a}
Seguimento \033[1;33mB\033[m: {segment_b}
Seguimento \033[1;34mC\033[m: {segment_c}
Este é um triângulo "\033[1;32mISÓSCELES\033[m", pois dois de seus lados são todos iguais! ''')
else:
    print(f'''Seguimento \033[1;32mA\033[m: {segment_a}
Seguimento \033[1;33mB\033[m: {segment_b}
Seguimento \033[1;34mC\033[m: {segment_c}
Este é um triângulo "\033[1;32mESCALENO\033[m", pois seus lados são todos diferentes! ''')
