# conta quantas vezes a letra A aparece, mostra a primeira posição que o A aparece é mostra a última posição.

frase = input('Digite uma frase: ').strip()
vezes = frase.upper().count('A')
primeira = (frase.upper().find('A') + 1)
ultima = (frase.upper().rfind('A') + 1)

print(f'A letra A aparece {vezes} vezes \nA primeira posição que a letra A aparece é: {primeira} \nE a última posição que a letra A aparece é: {ultima}')
