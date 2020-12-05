from time import sleep
num = 0
while True:
    cont = 0
    num = int(input('Digite um número, para parar digite um número negativo: '))
    if(num < 0):
        break      
    while cont < 10:
        cont += 1
        print(f'{num} X {cont} = {num * cont}')
print('Finalizando...'), sleep(1)
print('<>' * 12)
print('Programa finalizado.')
