matriz = [[], [], []]

for linhas in range(3):
    for colunas in range(3):
        numeros = int(input(f'Digite um número para [{linhas} {colunas}] '))
        matriz[linhas].append(numeros)

for linhas in range(3):
    for colunas in range(3):
        print(f'[{matriz[linhas][colunas]:^5}]', end = ' ')
    print()
