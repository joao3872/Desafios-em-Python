nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
resultado = ('Sua primeira nota foi {:.1f} e a segunda foi {:.1f}. Então a sua Média é {:.1f}'.format(nota1, nota2, media))

if(nota1 > 10 or nota2 > 10):
    print(' Nota inválida ! As Notas são de 0 até 10. \n Números maiores que 10, não são considerados Notas.')
elif(media >= 7.0):
    print(' {} \n Parabéns, você foi Aprovado !'.format(resultado))
elif(media >= 5.0 and 6.9):
    print(' {} \n Você está de Recuperação. Se esforçe mais !'.format(resultado))
else:
    print(' {} \n Você foi Reprovado. Portanto, estude bastante.'.format(resultado))
