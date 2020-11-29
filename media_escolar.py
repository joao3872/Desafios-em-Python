# Clássico da média de um Aluno.

nota1 = float(input('Digite a primeira Nota: '))
nota2 = float(input('Digite a segunda Nota: '))
media = (nota1 + nota2) / 2
resultado = (f'Sua primeira nota foi {nota1 :.1f} e a segunda foi {nota2 :.1f}. Então a sua média é: {media :.1f}')

if(nota1 > 10 or nota2 > 10):
    print('Nota inválida. Só é considerado Nota, números de 0 a 10.')
elif(media >= 7.0):
    print(f'{resultado} \n Parabéns você foi Aprovado !')
elif(media > 5.0 and 6.9):
    print(f'{resultado} \n Você está de recuperação. Se esforçe mais !')
else:
    print(f'{resultado} \n Você foi Reprovado. Portanto estude bastante.')

