# Classificação de atletas.

from datetime import date
atual = date.today().year
ano = int(input('Digite o Ano de seu Nascimento: '))
idade = (atual - ano)
print(f'O Atleta tem {idade} anos')

if(idade <= 9):
    print('Sua Categoria é: Mirim !')
elif(idade <= 14):
    print('Sua Categoria é: Infantil !')
elif(idade <= 19):
    print('Sua Categoria é: Junior !')
elif(idade <= 25):
    print('Sua Categoria é: Sênior !')
else:
    print('Sua Categoria é: Master !')

