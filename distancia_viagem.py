# Cobra um valor se a viagem tiver menos ou uma distância igual a 200Km, senão é cobrado outro valor.

distancia = float(input('Informe a distancia de sua viagem: Km '))
curta = (distancia * 0.50)
longa = (distancia * 0.45)

if(distancia > 200):
    print(f'A distância de sua viagem: {distancia}Km, é maior do que 200Km, portanto você pagará R$ 0,45 por Km. Então o total a pagar é: R$ {longa :.2f}')
else:
    print(f'A distância de sua viagem: {distancia}Km, é curta. Portanto, você pagará R$ 0,50 por Km. Então o total a pagar é: R$ {curta :.2f}')

