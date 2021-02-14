def inteiro(num):
    while True:
        try:
            valor = int(input(num))
        except (TypeError, ValueError):
            print('Erro, tente de novo.')
        except (KeyboardInterrupt):
            print('Usuário não quis digitar.')
            return 0
        else:
            return valor

def real(num):
    while True:
        try:
            valor = str(input(num)).replace(',', '.').strip()
            return float(valor)
        except (TypeError, ValueError):
            print('Erro, tente de novo.')
        except (KeyboardInterrupt):
            print('Usuário não quis digitar.')
            return 0
