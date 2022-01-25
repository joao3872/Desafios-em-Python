km = float(input('Qual é a distância em Km de sua viagem? Km '))
longa = km * 0.45
curta = km * 0.50

if(km > 200):
    print('Sua viagem tem {}Km \nE por possuir mais de 200Km de distância, você pagará R$ 0,45 por Km \nO total a pagar é: R${:.2f}'.format(km, longa))
else:
    print('Sua viagem tem {}Km \nJá que não é uma distância, acima de 200Km, então você pagará R$ 0,50 por Km \nO total a pagar é: R${:.2f}'.format(km, curta))
