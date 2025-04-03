# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# Variável de entrada e interação:
number = int(input('Digite um número para ver sua tabuada: '))

# Laço de repetição:
for c in range(1, 11):
    print(f'{number:<{len(f'{number}')}} \033[1;31mX\033[m {c:>2} \033[1;31m=\033[m {c * number:>{len(f'{number}')+ 1}}')
