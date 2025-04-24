# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Melancia', 'Banana', 'Jiló', 'Raiz', 'Ana')
for vg in palavras:
    print(f'\nNa palavra {vg} tem as vogais: ', end=' ')
    for vogais in vg:
        if vogais.lower() in 'aeéiíoóu':
            print(vogais, end=' ')
