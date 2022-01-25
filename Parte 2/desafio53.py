frase = input('Digite uma frase: \033[33m').strip().upper().replace(' ', '')
for c in range(0, len(frase) + 1):
    inverso = frase[::-1].upper().replace(' ', '')
print(f'\033[mO inverso de {frase} é: {inverso}')
if(frase == inverso):
    print(f'\033[32mEssa frase, é um Palíndromo ! \n\033[mA frase é a mesma coisa de trás para frente. \n E a frase possui: {c} letras.')
else:
    print(f'\033[31mEssa frase, não é um Palíndromo. \n\033[mA frase não é a mesma coisa de trás para frente. \n E a frase possui: {c} letras.')
