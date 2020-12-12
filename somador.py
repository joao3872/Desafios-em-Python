num = int(input('Quantas Notas Deseja Somar ? '))
soma = 0
cont = 0
for c in range(0, num):
    cont += 1    
    valor = float(input(f'Digite o Valor Total da {cont}° Nota: R$ '))
    soma += valor
print(f'O valor total é: R$ {soma :.2f}')
