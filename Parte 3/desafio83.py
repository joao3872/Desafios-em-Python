expressao = str(input('Digite uma expressão matemática: '))

if(expressao.count('(') == expressao.count(')')):
    print('Essa expressão é Válida !')
else:
    print('Essa expressão Não é Válida.')
