lista = []
continua = ''

while True:
    numero = int(input('Digite um número: '))
    if(numero in lista):
        print('Valor duplicado. Tente de novo.')
    else:
        lista.append(numero)
        print('Valor adicionado com sucesso !')
        
    continua = str(input('Deseja continuar? [Sim / Não] ')).strip().upper()
    if(continua == 'SIM'):
        print( )
    elif(continua == 'NÃO'):
        break
    else:
        print('Valor Inválido. Tente novamente... \n')
        
print(sorted(lista))
