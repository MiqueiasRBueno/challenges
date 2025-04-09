# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print(f'''\033[1;31m{'=' * 55}\033[m
\033[1m{'CALCULADORA':^55}
\033[1;31m{'=' * 55}\033[m''')
pri_valor = float(input('Primeiro valor: '))
seg_valor = float(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print(f'''\033[1;31m{'=' * 55}\033[m
{'Escolha a operação que deseja executar:':^55}
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
\033[1;31m{'=' * 55}\033[m''')
    escolha = int(input('Qual sua opção? '))
    if escolha == 1:
        print(f'''\033[1;31m{'=' * 55}\033[m
A soma dos dos valores {pri_valor:.2f}
                     + {seg_valor:.2f}
                       {pri_valor + seg_valor:.2f}''')
    elif escolha == 2:
        print(f'''\033[1;31m{'=' * 55}\033[m
O produto da multiplicação dos valores {pri_valor:.2f}
                                     X {seg_valor:.2f}
                                      {pri_valor * seg_valor:.2f}''')
    elif escolha == 3:
        if pri_valor > seg_valor:
            maior = pri_valor
        else:
            maior = seg_valor
        print(f'''\033[1;31m{'=' * 55}\033[m
O maior valor digitado é {maior:.2f}''')
    elif escolha == 4:
        pri_valor = float(input('Primeiro valor: '))
        seg_valor = float(input('Segundo valor: '))
print(f'\033[1;31m{'=' * 55}\033[m\nPrograma finalizado com sucesso!')
