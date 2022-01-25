alug = float(input('Informe a quantidade de dias, em que o carro foi alugado: '))
dist = float(input('Quantos Km você percorreu com o carro? '))
valorA = (alug * 60)
valorD = (dist * 0.15)
soma = (valorA + valorD)

print('Então o valor de seu aluguel é de R$ {:.2f}'.format(soma))
print('Caso você queira saber, o valor dos Km percorridos, é R$ {:.2f} \nE o valor dos dias alugados é de R$ {:.2f}'.format(valorD, valorA))
