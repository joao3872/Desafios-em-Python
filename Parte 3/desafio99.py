from time import sleep
def maior(* numeros):
    print('<>' * 20)
    print('Analisando os valores...')
    for c in numeros:
        print(f'{c}', end = ' ')
        sleep(0.3)
    print(f'Foram informados {len(numeros)} números. \n O Maior valor foi {max(numeros)}')

maior(7, 8, 0, 3, 2, 5)
maior(8, 10, 6)
maior(4)
maior(17, 28, 21, 78)
maior(100, 83, 48, 53, 1)
