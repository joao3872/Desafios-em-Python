s1 = int(input('Informe o primeiro segmento: '))
s2 = int(input('Informe o segundo segmento: '))
s3 = int(input('Informe o terceiro segmento: '))
veja = ((s2 - s3) < s1 < s2 + s3) and ((s1 - s3) < s2 < s1 + s3) and ((s1 - s2) < s3 < s1 + s2)
e = (s1 == s2 != s3) or (s1 != s2 == s3) or (s2 != s1 == s3)

if(e and veja):
    print('Os Segmentos Formam um Triângulo ISÓSCELES !')
elif(s1 == s2 == s3 and veja):
    print('Os Segmentos Formam um Triângulo EQUILÁTERO !')
elif(s1 != s2 != s3 and veja):
    print('Os Segmentos Formam um Triângulo ESCALENO !')
else:
    print('Os Segmentos Não formam um Triângulo.')
