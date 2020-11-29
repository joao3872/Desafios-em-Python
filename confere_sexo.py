# Confere se a abreviação de Homem ou Mulher está correta, caso, seja digitado qualquer valor diferente de M ou F, a resposta será: Dado inválido. E pedirá para informar o sexo corretamente, até digitar o correto. 

sexo = str(input('Informe o sexo de uma pessoa [M / F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dado inválido. Informe o sexo: ')).strip().upper()
if(sexo == 'M'):
     print(f'Sim ! {sexo} é a abreviação correta para Homens !')
else:
     print(f'Sim ! {sexo} é a abreviação correta para Mulheres !')
