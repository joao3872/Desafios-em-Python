# De 6 números informados, é feita a Soma somente do números Pares.

soma = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if(num % 2 == 0):
        soma += num
print(f'A Soma dos números Pares é: {soma}')
