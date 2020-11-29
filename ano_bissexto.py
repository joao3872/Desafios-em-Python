# conferi se o Ano digitado é Bissexto ou não.

ano = int(input('Informe um ano: '))
confira = (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)
# faz uma verificação de 4 em 4 anos, verifica se a cada 100 anos é múltiplo ou não e a cada 400 anos...
if(confira):
    print(f'O ano {ano} é Bissexto !')
else:
    print(f'O ano {ano} não é Bissexto.')

