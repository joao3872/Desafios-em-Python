def metadeP(preco):
    metade = preco / 2
    return metade

def dobroP(preco):
    dobro = preco * 2
    return dobro

def porcento10(preco):
    porcentagem = preco + (preco * 10/100)
    return porcentagem

def desconto(preco):
    desconta = preco - (preco * 10/100)
    return desconta

def moeda(preco):
    preco = f'{preco :.2f}'
    resposta = preco.replace('.', ',')
    return resposta
