# Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que o ajude,
# lendo os nomes e o escrevendo o nome escolhido
from random import choice

alunos = []
for i in range(1,5):
    aluno = str(input(f'Digite o nome do {i}° aluno: ')).strip().title()
    alunos.append(aluno)
sorteado = choice(alunos)
print(f'O aluno sorteado para apagar o quadro foi: {sorteado}')
