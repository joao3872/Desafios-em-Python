lista = []
dados = []
pesos = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    pesos.append(dados[1])
    dados.clear()
    
    continua = str(input('Deseja continuar? [Sim / Não] ')).strip().upper()
    if(continua == 'SIM'):
        print('<>' * 18)
    elif(continua == 'NÃO'):
        break
    else:
        print('Valor Inválido. Tente de novo...')

print(f'Temos {len(lista)} pessoa(s) na lista')
print(f'O Menor peso foi: {min(pesos)}, Peso de:', end = ' ')

for p in lista:
    if(p[1] == min(pesos)):
        print(f'[{p[0]}]', end = ' ')

print(f'\nO Maior peso foi: {max(pesos)}, Peso de:', end = ' ')
for p in lista:
    if(p[1] == max(pesos)):
        print(f'[{p[0]}]', end = ' ')
