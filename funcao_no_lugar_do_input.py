def leiaInt(num):
    while True:
        valor = str(input(num))
        if valor.isnumeric():
            return valor
        else:
            print('\033[31m Erro. Digite outro número. \033[m')

numero = leiaInt('Digite um número: \033[36m')
print(f'\n\033[32mO número digitado foi:\033[m \033[33m{numero} \033[m')
