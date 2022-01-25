def fatorial(numero, show = False):
    fat = 1
    for cont in range(numero, 0, -1):
        if show:
            print(f'{cont}', end = ' ')
            if cont > 1:
                print('X', end = ' ')
            else:
                print('=', end = ' ')
        fat *= cont
    return fat

# Programa principal...
numero = int(input('Digite um número: '))
mostra = str(input('Digite S para mostrar o fatorial ou N para mostra apenas o resultado: ')).strip().upper()
if mostra == 'S':
    show = True
else:
    show = False

print(fatorial(numero, show = show))
