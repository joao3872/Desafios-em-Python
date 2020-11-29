# acima de 80Km aplica-se, R$ 7,00 de multa, por cada Km, acima do limite de velocidade.

km = int(input('Informe a velocidade, na qual você estava dirigindo o seu carro: Km '))
multa = (km - (8 * 10)) * 7

if(km > 80):
    print(f'Você foi Multado. Por ultrapassar o limite de 80Km/h. E o valor de sua Multa é de R$ {multa :.2f}')
else:
    print('Muito bem! Dirija sempre com segurança!')

