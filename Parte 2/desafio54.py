from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    nascimento = int(input(f'Informe o ano de nascimento da {c}º pessoa: '))
    ano = atual - nascimento
    if(ano < 18):
        menor += 1
    else:
        maior += 1
print(f'Em um Grupo, existe {menor} pessoa(s) mais nova(s). \nE no mesmo Grupo, existe {maior} pessoa(s) maior(es) de idade.')
