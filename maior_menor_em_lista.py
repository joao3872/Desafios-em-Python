valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite número: ')))
print(f'Os números digitados foram: {valores}')
print(f'O Maior número foi {max(valores)} na(s) posição(ões):', end = ' ')

for c in range(0, 5):
    if valores[c] == max(valores):
        print(f'{c + 1} ', end = ' ')
        
print(f'\nO Menor número foi {min(valores)} na(s) posição(ões):', end = ' ')

for c in range(0, 5):
    if valores[c] == min(valores):
        print(f'{c + 1} ', end = ' ')
