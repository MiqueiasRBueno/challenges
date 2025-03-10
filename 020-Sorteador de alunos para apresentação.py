# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia os nomes dos 4 alunos e mostre a ordem sorteada.

from random import shuffle
soma = 0
alunos = []
for i in range(1, 5):
    aluno = str(input(f'Digite o nome do {i}° aluno a apresentar seu trabalho: ')).strip().title()
    alunos.append(aluno)
shuffle(alunos)
print(f'A ordem de apresentação do trabalho é:')
for c in alunos:
    soma += 1
    print(f'{soma}º= {c}')
