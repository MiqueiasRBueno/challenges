# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

# dicionário de cores
cores = {'branco': '\033[30m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[33m',
         'azul':'\033[1;34m', 'roxo': '\033[35m', 'ciano': '\033[1;36m', 'cinza': '\033[37m', 'limpa': '\033[m'}

# variável de armazenamento das informações digitadas pelo usuário
current_salary = float(input(f'{cores['ciano']}Digite o valor do salário atual de seu funcionário:'
                             f' R${cores['limpa']} '))
# Analisa a condição para o definir o aumento de salário do funcionário
if current_salary <= 1250:
    # Calcula o valor do novo sálario com o acréscimo
    increase_fifteen_percent = (current_salary * 0.15) + current_salary
    print(f'''O salário atual do funcionário é de \033[7;31;1;4mR$ {current_salary:.2f}{cores['limpa']}
Novo salário do funcionário com um acréscimo de 15%:\033[7;31;1;4m R$ {increase_fifteen_percent}{cores['limpa']}''')
else:
    ten_percent_increase = (current_salary * 0.1) + current_salary
    print(f'''O salário atual do funcionário é de \033[7;33;1;4mR$ {current_salary:.2f}{cores['limpa']}
Novo salário do funcionário com um acréscimo de 10%: \033[7;33;1;4mR$ {ten_percent_increase:.2f}{cores['limpa']}''')
