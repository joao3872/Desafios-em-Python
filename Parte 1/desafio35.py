print('<-' * 14)
print('Analisador de Triângulos')
print('->' * 14)
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
confira = ((s2 - s3) < s1 < s2 + s3) and ((s1 - s3) < s2 < s1 + s3) and ((s1 - s2) < s3 < s1 + s2)

if(confira):
    print('Os três Segmentos Formam um Triângulo !')
else:
    print('Os três Segmentos Não formam um Triângulo.')
