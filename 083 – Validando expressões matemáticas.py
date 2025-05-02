# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = str(input('Digite uma expressão: '))
parentheses = []
for simb in expression: # para cada simbolo "()" na expressão
    if simb == '(': # se simbolo for igual a um "(" abrindo
        parentheses.append('(')  # então o programa colocará dentro da lista
    elif simb == ')': # se simbolo for igual um ")" fechando
        if len(parentheses) > 0: # e len da lista for maior que 0
            parentheses.pop() # removerá o último elemento da lista
        else: # se for menor que zero
            parentheses.append(')') # colocará um ")" na lista
if len(parentheses) == 0: # se o len da lista for igual a zero
    print('Sua expressão está correta!') # a expressão esta correta
else:
    print('Sua expressão está errada!') # se for maior que zero, estará errada
