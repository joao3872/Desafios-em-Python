# Analisando um nome.

nome = input('Informe seu nome completo: ')
nomeM = nome.upper()
nomem = nome.lower()
letras = nome.replace(' ', '')
todos = len(letras)
primeiroN = nome.split()
pNome = len(primeiroN[0])

print(f'Seu nome com letras maiúsculas: {nomeM} \nSeu nome com letras minúsculas: {nomem} \nTotal de letras do seu nome: {todos} \n Quantidade de letras de seu primeiro nome: {pNome}')
