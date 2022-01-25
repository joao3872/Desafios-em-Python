print('<' * 10, 'Lojas JJ', '>' * 10)
preco = continua = cont = contM = total = menor = 0
nome = barato = ''
while True:
    nome = str(input('Digite o nome do Produto: ')).strip()
    preco = float(input('Informe o Preço do Produto: R$ '))
    continua = str(input('Deseja continuar ? [Sim / Não] ')).strip().upper()
    cont += 1
    total += preco
    
    if(preco > 1000):
        contM += 1
    if(cont == 1 or preco < menor):
        menor = preco
        barato = nome
        
    if(continua == 'SIM'):
        print('---'*10)
    elif(continua == 'NÃO'):
        break
    else:
        print('Resposta inválida.')
        break
    
print(f'O Total gasto na compra foi de R$ {total :.2f}')
print(f'A compra possui {contM} Produto(s), que custa(m) mais de R$ 1000,00.')
print(f'E o Produto mais barato é {barato} com o custo de R$ {menor :.2f}')
