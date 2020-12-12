preco = float(input('Informe o preço de um produto: R$ '))
desconto = (preco * (5/100))
newp = (preco - desconto)

print(f'O preço antigo do produto era R$ {preco :.2f} \nE você ganhou um desconto de 5%, portanto o novo preço é de R$ {newp :.2f}')
