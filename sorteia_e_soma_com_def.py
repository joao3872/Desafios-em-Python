from random import randint
from time import sleep

def sorteio():
    print('Sorteando 5 valores:', end = ' ')
    for c in range(5):
        s = randint(0, 10)
        print(f'{s}', end = ' ', flush=True)
        sleep(0.5)
        numeros.append(s)
    print('Fim')

def somaPar():
    print(f'\nSorteando os números Pares {numeros}', end = ' ')
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'A Soma dos Pares é {soma}')

numeros = []
sorteio()
somaPar()
