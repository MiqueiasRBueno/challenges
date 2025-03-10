# Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas, conforme o valor digitado.

nome = str(input('Digite seu nome: ')).strip().title()
print(f'Olá {nome}!\nPrazer em te conhecer!')
