num = input('Digite um número de 0 á 9999: ')
valor = num.zfill(4)

print('O número {} possui:'.format(num[0:4]))
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(valor[3], valor[2], valor[1], valor[0]))
