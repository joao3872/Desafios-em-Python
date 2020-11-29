# Mostra a sequência de Fibonacci.

print('Sequência de Fibonacci \n')
termos = int(input('Quantos Termos ? '))
primeiroT = 0
segundoT = 1
cont = 3
print(f'{primeiroT} -> {segundoT}', end = ' -> ')

while cont <= termos:
    resultado = primeiroT + segundoT
    print(f'{resultado}', end = ' -> ')
    primeiroT = segundoT
    segundoT = resultado
    cont += 1
print('Acabou.')
