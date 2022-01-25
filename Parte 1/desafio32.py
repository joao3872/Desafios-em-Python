ano = int(input('Digite um ano: '))
confira = (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)

if(confira):
    print('O ano {} é Bissexto !'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))
