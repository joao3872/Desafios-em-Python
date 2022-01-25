termo = int(input('Digite o primeiro Termo: '))
razao = int(input('Digite a Razão: '))
ordem = termo + 10 * razao
for c in range(termo, ordem, razao):
    print(f'{c}', end = ' -> ')
print('Finalizado.')
