# Cálculo do IMC (Índice de Massa Corporal)

peso = float(input('Informe o seu Peso: '))
altura = float(input('Informe a sua Altura: '))
imc = (peso / (altura ** 2))
print(f'Seu IMC é: {imc :.1f}')

if(imc <= 18.5):
    print('Você está abaixo do peso ideal.')
elif(imc <= 25):
    print('Você está com o peso ideal !')
elif(imc <= 30):
    print('Você está com Sobrepeso.')
elif(imc <= 40):
    print('Vocé está com Obesidade.')
else:
    print('Você está com Obesidade mórbida. Tome muito cuidado.')
