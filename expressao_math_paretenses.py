expressao = str(input('Digite uma expressão matemática: \033[36m'))

if(expressao.count('(') == expressao.count(')')):
    print(f'\033[32m A expressão: {expressao} É Válida !\033[m')
else:
    print(f'\033[31m A expressão: {expressao} Não é Válida.\033[m')
