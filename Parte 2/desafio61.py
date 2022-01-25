print('Gerador de PA \n')
termo = int(input('Digite o Termo: '))
razao = int(input('Digite a Razão: '))
calculo = 1
limite = int(input('Informe o número máximo do limite: '))
while calculo < limite + 1:
    decimo = termo + (calculo - 1) * razao
    print(f'{decimo}', end = ' -> ')
    calculo += 1
print('Acabou')
