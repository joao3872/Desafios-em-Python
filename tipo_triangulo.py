# Confere se os 3 segmentos formam um Triângulo Equilátero ou Isósceles ou Escaleno.

s1 = float(input('Digite o primeiro segmento : '))
s2 = float(input('Digite o segundo segmento : '))
s3 = float(input('Digite o terceiro segmento : '))
veja = ((s2 - s3) < s1 < s2 + s3) and ((s1 - s3) < s2 < s1 + s3) and ((s1 - s2) < s3 < s1 + s2)
v = (s1 == s2 != s3) or (s1 != s2 == s3) or (s2 != s1 == s3)

if(veja and v):
    print('Os segmentos formam um Triângulo Isósceles !')
elif(s1 == s2 == s3 and veja):
    print('Os segmentos formam um Triângulo Equilátero !')
elif(s1 != s2 != s3 and veja):
    print('Os segmentos formam um Triângulo Escaleno !')
else:
    print('Os três segmentos não formam um Triângulo.')
