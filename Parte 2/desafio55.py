lista = []
for c in range(1, 6):
    peso = float(input(f'Informe o Peso da {c}º pessoa: Kg '))
    lista.append(peso)
    ordem = sorted(lista)
print(f'O Menor Peso é: {ordem[0]}Kg \nO Maior Peso é: {ordem[4]}Kg')
