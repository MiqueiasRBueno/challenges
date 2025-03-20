# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Entrada de dados:
house_value = float(input('Digite o valor da casa à financiar: R$ '))
buyer_salary = float(input('Digite o valor do salário do candidato a comprador: R$ '))
installment_number = int(input('Digite o número de parcelas desejado: '))
# Cálcula o valor das prestações e o percentual sobre o salário
installment_value = house_value / installment_number
salary_percentage = (installment_value * 100) / buyer_salary
# Informações impressas na tela:
print(f'''O valor da casa a financiar é de R$ {house_value:.2f}
O salário do candidato ao financiamento é de R$ {buyer_salary:.2f}''')
# Condições para o financiamento
if salary_percentage <= 30:
    print(f'''{'=' * 60}
O valor das prestações são de R$ {installment_value:.2f}
Corresponde á {salary_percentage:.0f}% do salário do candidato ao financiamento
Meus parabéns, seu empréstimo foi aprovado!
{'=' * 60}''')
else:
    print(f'''{'=' * 60}
O valor das prestações são de R$ {installment_value:.2f}
Corresponde á {salary_percentage:.0f}% do salário do candidato ao financiamento
Que pena, seu empréstimo foi reprovado!
{'=' * 60}''')
