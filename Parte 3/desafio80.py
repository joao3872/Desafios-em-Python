lista = []

for c in range(0, 5):
    numero = int(input('Digite um número: '))

    if c == 0 or numero > max(lista):
        lista.append(numero)
        print(f'O número {numero}, foi adicionado na última posição. \n')
    else:
        posicao = 0
        while posicao < max(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'O número {numero}, foi adicionado na {posicao + 1}º posição \n')
                break
            posicao += 1
print(lista)
