# Faça um programa que leia um frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'.
# Em que posição aparece a primeira vez.
# Em que posição apare a última vez.

first_last_occurrence = str(input('Digite uma frase qualquer: ')).strip().upper()
letter = str(input('Digite uma letra para buscar na frase: ')).upper()
print(f'A letra "{letter}" aparece {first_last_occurrence.count(letter)} vezes na frase acima!')
print(f'A letra "{letter}" aparece primeiro na posição {first_last_occurrence.find(letter) + 1} da frase.')
print(f'E a última posição que aparece é {first_last_occurrence.rfind(letter) + 1}')
