num = cont = soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A Soma dos {cont} números é {soma}')
