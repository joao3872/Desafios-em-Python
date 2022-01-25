from datetime import date
atual = date.today().year
ano = int(input('Digite o Ano de seu Nascimento: '))
idade = (atual - ano)
print('O Atleta tem {} anos'.format(idade))

if(idade <= 9):
    print('Sua Classificação é: Mirim')
elif(idade <= 14):
    print('Sua Classificação é: Infantil')
elif(idade <= 19):
    print('Sua Classificação é: Junior')
elif(idade <= 25):
    print('Sua Classificação é: Sênior')
else:
    print('Sua Classificação é: Master')
