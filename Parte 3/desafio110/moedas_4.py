def moeda(preco):
    preco = f'{"R$":>3} {preco :.2f}'
    resposta = preco.replace('.', ',')
    return resposta

def titulo(resumo):
    print()
    print('<>' * 16)
    print(f'{"Resumo do Preço":>23}')
    print('<>' * 16)

def resumo(preco):
    metade = preco / 2
    dobro = preco * 2
    aumento = preco + (preco * 20/100)
    desconto = preco - (preco * 12/100)
    
    print(f'Preço Analisado: {moeda(preco)}')
    print(f'Metade do Preço: {moeda(metade)}')
    print(f'Dobro do Preço : {moeda(dobro)}')
    print(f'20% de Aumento : {moeda(aumento)}')
    print(f'12% de Desconto: {moeda(desconto)}')
    print('<>' * 16)
