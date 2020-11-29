# confere se uma pessoa já fez o alistamento militar e a quanto tempo fez, ou falta para fazer.

from datetime import date
nascido = int(input('Informe o ano de seu Nascimento: '))
atual = date.today().year
idade = (atual - nascido)
atras = (idade - 18)
ano = (atual - atras)
falta = (18 - idade)

if(idade == 18):
    print(f'Você nasceu em {nascido} e tem {idade} anos em {atual} \n E deve se alistar Agora.')
elif(idade > 18):
    print(f'Você nasceu em {nascido} e tem {idade} anos em {atual} \n Já se alistou a {atras} anos atrás! \n O alistamento, foi no ano de {ano}')
else:
    print(f'Você nasceu em {nascido} e tem {idade} anos em {atual} \n Ainda falta {falta} anos para o alistamento. \n E será no ano de {ano}')

