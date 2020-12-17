lista = []

while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    
    continua = str(input('Deseja continuar? [Sim / Não] ')).strip().upper()
    if(continua == 'SIM'):
        print( )
    elif(continua == 'NÃO'):
        break 
    else:
        print('Valor Inválido. Tente novamente...')

print(f'Você digitou {len(lista)} números.')
print(f'Os números em ordem decrescente: {sorted(lista, reverse = True)}')

if(5 in lista):
    print('O número 5 está na lista !')
else:
    print('O número 5 não está na lista.')
