preco = float(input('Informe o preço de um produto: '))
desc = (preco * (5/100))
newp = preco - desc

print('O preço antigo era de R$ {:.2f}, agora com 5% de desconto, passa a ser R$ {:.2f}'.format(preco, newp))
