# Converte o número informado, em uma das três opções que você escolher.

num = int(input('Digite um número inteiro: '))
print('Escolha uma base de conversão: \n [1] converter para Binário \n [2] converter para Octal \n [3] converter para Hexadecimal')
opcao = int(input('Escolha a opção: '))
binario = bin(num).replace('0b', '')
octal = oct(num).replace('0o', '')
hexa = hex(num).replace('0x', '').upper()

if(opcao == 1):
    print(f'{num} convertido em Binário é igual a: {binario}')
elif(opcao == 2):
    print(f'{num} convertido em Octal é igual a: {octal}')
elif(opcao == 3):
    print(f'{num} convertido em Hexadecimal é igual a: {hexa}')
else:
    print('Nenhuma das opções, foram escolhidas.')
