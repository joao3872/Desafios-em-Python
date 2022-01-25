num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um número (use 999 para finalizar): '))
    if(num != 999):
        soma += num
        cont += 1
print(f'Você digitou {cont} números e a Soma entre eles é {soma}')
