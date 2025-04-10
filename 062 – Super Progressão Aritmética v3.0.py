# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print(f'''\033[1;31m{'='*55}\033[m
{'GERADOR DE P.A':^55}
\033[1;31m{'='*55}\033[m''')
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão P.A: '))
print(f'\033[1;31m{'='*55}\033[m')
total = n = 0
mais = 10
while mais != 0:
    total += mais
    while n != total:
        n += 1
        pa = termo + (n - 1) * razao
        print(f'{pa}', end='\033[1;34m-->\033[m')
    mais = int(input('\033[1;34mPAUSA\033[m\nMais quantos temos você que mostrar [0]para parar: '))
print(f'\033[1;31m{'='*55}\033[m\nP.A finalizada com {total} termos mostrados!')