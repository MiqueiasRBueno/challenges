# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print(f'''\033[1;31m{'=' * 55}\033[m
\033[1m{'TABUADA V3.0':^55}
\033[31m{'=' * 55}\033[m''')
while True:
    tabu = int(input('Quer ver a tabuada de qual valor? '))
    if tabu < 0:
        break
    for c in range(0, 10):
        c += 1
        print(f'{tabu:>{len(f'{tabu}')}} \033[1;31mX\033[m {c:>{len(f'{tabu}')}}'
              f' \033[1;31m=\033[m {tabu * c:>{len(f'{tabu}')+ 1}}')
print(f'''\033[1;31m{'=' * 55}\033[m
Tabuada finalizada com sucesso!''')
