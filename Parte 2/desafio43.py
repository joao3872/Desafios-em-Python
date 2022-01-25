peso = float(input('Qual o seu Peso? Kg '))
altura = float(input('Qual a sua Altura? m '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))

if(imc <= 18.5):
    print('Você está abaixo do Peso Ideal.')
elif(imc <= 25):
    print('Você está com o Peso Ideal !')
elif(imc <= 30):
    print('Você está com Sobrepeso.')
elif(imc <= 40):
    print('Você está com Obesidade.')
else:
    print('Você está com Obesidade Mórbida. \nMuitos cuidados serão necessários daqui para frente.')
