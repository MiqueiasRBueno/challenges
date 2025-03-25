# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, conforme
# a média atingida:
# - Média abaixo de 5,0: Reprovado
# - Média entre 5,0 e 6,9: Recuperação
# - Média 7.0 ou superior: Aprovado

# Variáveis para guardar os dados inseridos pelo usuário
print(f'''\033[1;32m{'=' * 50}\033[m
{' ' * 15}BOLETIM DOS ALUNOS
\033[1;32m{'=' * 50}\033[m''')
nota_1 = float(input('Digite a 1ª nota do aluno: '))
nota_2 = float(input('Digite a 2ª nota do aluno: '))
media = (nota_1 + nota_2) / 2
print(f'''\033[1;32m{'=' * 50}\033[m
1ª Nota {nota_1:.1f}
2ª Nota {nota_2:.1f}
\033[1;32m{'=' * 50}\033[m
{' ' * 20}MÉDIA
\033[1;32m{'=' * 50}\033[m''')
if media >= 7:
    print(f'''Sua nota média é {media:.1f}
Meus parabéns, você está aprovado!''')
elif 5 <= media < 7:
    print(f'''Sua nota média é {media:.1f}
Você está de recuperação, precisa se esforçar mais!''')
else:
    print(f'''Sua nota média é {media:.1f}
Você foi reprovado, faltou interesse nas aulas!''')