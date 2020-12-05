num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número (use 999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A Soma dos {cont} números é {soma}')
