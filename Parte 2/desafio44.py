print('>' * 10, 'Lojas JJ', '<' * 10)
preco = float(input('Digite o Valor Total das Compras: R$ '))
print('Escolha a Forma de Pagamento: \n [1] à Vista ou no Cheque \n [2] à Vista no Cartão \n [3] 2x no Cartão \n [4] 3x ou Mais no Cartão')
opcao = int(input('Qual é a opção? '))
vista = (preco - preco * (10/100))
vistaC = (preco - preco * (5/100))
tresV = (preco + preco * (20/100))
print('Sua compra tem um total de R$ {:.2f}'.format(preco))

if(opcao == 1):
    print('Pagando a Vista, você ganha 10% de desconto, então o total a pagar é R$ {:.2f}'.format(vista))
elif(opcao == 2):
    print('Pagando a Vista no Cartão, você ganha 5% de desconto, então o total a pagar é R$ {:.2f}'.format(vistaC))
elif(opcao == 3):
    print('Você pagará 2x de R$ {:.2f}'.format(preco / 2))
elif(opcao == 4):
    vezes = int(input('Em quantas vezes? '))
    print('Sua compra será parcelada em {}x de R$ {:.2f} com 20% de Juros'.format(vezes, (tresV / vezes)))
    print('Sua compra de R$ {:.2f} terá um total de R$ {:.2f}'.format(preco, tresV))
else:
    print('Você não escolheu uma das Formas de Pagamento.')
