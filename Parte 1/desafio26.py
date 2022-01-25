frase = input('Digite uma frase: ')
ap = frase.upper().count('A')
pp = (frase.upper().find('A') + 1)
up = (frase.upper().rfind('A') + 1)

print('A letra A aparece {} vezes \nA primeira letra A aparece na posição: {} \nE a última letra A aparece na posição: {}'.format(ap, pp, up))
