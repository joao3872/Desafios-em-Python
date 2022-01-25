matriz = [[], [], []]
somaPar = soma = 0

for linhas in range(3):
    for colunas in range(3):
        numeros = int(input(f'Digite um número para [{linhas} {colunas}] '))
        matriz[linhas].append(numeros)
        if(numeros % 2 == 0):
            somaPar += numeros

for linhas in range(3):
    for colunas in range(3):
        print(f'[{matriz[linhas][colunas]:^5}]', end = ' ')
    print()

    if(matriz != matriz[2]):
        soma += matriz[linhas][colunas]

print(f'\nA Soma dos números da 3º coluna: {soma}')
print(f'A Soma dos números Pares é: {somaPar}')
print(f'O Maior número da 2º linha é: {max(matriz[1])}')
