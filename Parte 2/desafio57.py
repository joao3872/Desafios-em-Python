sexo = str(input('Informe o sexo de uma pessoa [M / F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dado inválido. Informe o sexo: ')).strip().upper()
if(sexo == 'M'):
    print(f'Sim ! {sexo} é a abreviação correta para Homens !')
else:
    print(f'Sim ! {sexo} é a abreviação correta para Mulheres !')
