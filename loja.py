print('<' * 10, 'Lojas JJ', '>' * 10)
nome = preco = continua = cont = total = 0
lista = []
while True:
    nome = str(input('Digite o nome do Produto: ')).strip()
    lista.append(nome)
    barato = sorted(lista) 
    preco = float(input('Informe o Preço do Produto: R$ '))
    continua = str(input('Deseja continuar ? [Sim / Não] ')).strip().upper()
    total += preco
    
    if(preco > 1000):
        cont += 1
       
    if(continua == 'SIM'):
        print('---'*10)
    elif(continua == 'NÃO'):
        break
    else:
        print('Resposta inválida.')
        break
    
print(f'O Total gasto na compra foi de R$ {total :.2f}')
print(f'A compra possui {cont} Produto(s), que custa(m) mais de R$ 1000,00.')
print(f'E o Produto(s) mais barato(s) é {barato[0]}')
