from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end = ' ', flush=True)
            sleep(0.5)
            cont += passo
        print('Fim')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end = ' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('Fim')

print('Contagem de 1 até 10 de 1 em 1.')
for c in range(1, 11):
    print(f'{c}', end = ' ', flush=True)
    sleep(0.5)
print('Fim')

print('Contagem de 10 até 0 de 2 em 2.')
for c in range(10, -1, -2):
    print(f'{c}', end = ' ', flush=True)
    sleep(0.5)
print('Fim')

print('Agora é sua vez, de personalizar a contagem:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
