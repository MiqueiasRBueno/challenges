# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario_atual = float(input('Digite o valor de seu salário atual: R$'))
salario_novo = salario_atual + (salario_atual * 0.15)
print(f'O valor do salário atual é de R${salario_atual:.2f}\n'
      f'O valor do novo salário com o aumento de 15% é de R${salario_novo:.2f}')
