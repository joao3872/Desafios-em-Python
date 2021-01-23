# Forma de pagamento de uma compra.

print('>' * 10, 'Lojas JJ', '<' * 10)
preco = float(input('Digite o Valor Total das Compras: R$ '))
print('Escolha a Forma de Pagamento: \n [1] à Vista ou no Cheque \n [2] à Vista no Cartão \n [3] 2x no Cartão \n [4] 3x ou Mais no Cartão')
opcao = int(input('Qual é a opção? '))
vista = (preco - preco * (10/100))
vistaC = (preco - preco * (5/100))
tresV = (preco + preco * (20/100))
print(f'Sua compra tem um total de R$ {preco :.2f}')

if(opcao == 1):
    print(f'Pagando a Vista, você ganha 10% de desconto, então o total a pagar é R$ {vista :.2f}')
elif(opcao == 2):
    print(f'Pagando a Vista no Cartão, você ganha 5% de desconto, então o total a pagar é R$ {vistaC :.2f}')
elif(opcao == 3):
    print(f'Você pagará 2x de R$ {preco / 2 :.2f}')
elif(opcao == 4):
    vezes = int(input('Em quantas vezes? '))
    print(f'Sua compra será parcelada em {vezes}x de R$ {(tresV / vezes) :.2f} com 20% de Juros')
    print(f'Sua compra de R$ {preco :.2f} terá um total de R$ {tresV :.2f}')
else:
    print('Você não escolheu umas das Formas de Pagamento.')

