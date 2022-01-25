from datetime import date
nascido = int(input('Informe o ano de seu nascimento: '))
atual = date.today().year
idade = (atual - nascido)
atras = (idade - 18)
ano = (atual - atras)
falta = (18 - idade)

if(idade == 18):
    print(' Você nasceu em {} e tem {} anos em {} \n E deve se alistar Agora.'.format(nascido, idade, atual))
elif(idade > 18):
    print(' Você nasceu em {} e tem {} anos em {} \n Já se alistou a {} anos atrás! \n O alistamento, foi no ano de {}'.format(nascido, idade, atual, atras, ano))
else:
    print(' Você nasceu em {} e tem {} anos em {} \n Ainda falta {} anos para o alistamento. \n E será no ano de {}'.format(nascido, idade, atual, falta, ano))
