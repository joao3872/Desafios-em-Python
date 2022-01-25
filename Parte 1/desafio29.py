km = int(input('Informe qual é a velocidade em Km/h, que você atingiu com seu carro: Km '))
limite = (km - (8 * 10)) * 7

if(km > 80):
    print('A velocidade atingida foi {}Km, e você quebrou o limite de 80 Km/h. \nPortanto sua multa é de R${:.2f}'.format(km, limite))
else:
    print('Muito bem sua velocidade foi {}Km \nDirija sempre com segurança !'.format(km))
