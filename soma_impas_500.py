# Soma todos os números ímpas, existente no intervalo de 1 até 500.

soma = 0
quantidade = 0
for c in range(1 * 3, 501, 6):
    soma += c
    quantidade += 1
print(f'A soma dos {quantidade} números ímpas é igual a: {soma}')
