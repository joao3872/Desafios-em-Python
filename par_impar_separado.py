lista = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if(numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)
    
    continua = str(input('Deseja continuar? [Sim / Não] ')).strip().upper()
    if(continua == 'SIM'):
        print( )
    elif(continua == 'NÃO'):
        break
    else:
        print('Valor Inválido. Tente novamente...')
        
print(f'A lista completa: {lista}')
print(f'O(s) número(s) Par(es): {sorted(pares)}')
print(f'O(s) número(s) Ímpar(es): {sorted(impares)}')
