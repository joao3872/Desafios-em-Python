from math import radians, sin, cos, tan
ang = float(input('Informe um ângulo que quiser: '))
sen = sin(radians(ang)) # É necessário, converter a variável, para radians, já que o calculo original não é este...
cos = cos(radians(ang))
tan = tan(radians(ang))

print('O ângulo de {} tem o seu Seno igual a {:.2f} \nSeu Cosseno é igual a {:.2f} \nSua Tangente é igual a {:.2f}'.format(ang, sen, cos, tan))
