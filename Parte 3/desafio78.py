valores = []
verefica_maior = []
verefica_menor = []

for cont in range(0, 5):
    numeros = int(input(f'Digite um número para a Posição {cont + 1}: '))
    valores.append(numeros)
    for posicao, num in enumerate(valores):
        if num == max(valores):
            verefica_maior.append(posicao)
        if num == min(valores):
            verefica_menor.append(posicao)
print(f'Os valores digitados foram: {valores}')
print(f'O Maior número digitado foi {max(valores)} nas posições {verefica_maior}')
print(f'O Menor número digitado foi {min(valores)} nas posições {verefica_menor}')
