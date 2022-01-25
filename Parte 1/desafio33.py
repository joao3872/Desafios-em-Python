print('Digite três números, para que o programa, mostre qual é o Menor e o Maior número')
print('>' * 80)
valor = float(input('Digite um número: '))
valor2 = float(input('Digite outro número: '))
valor3 = float(input('Digite mais um número: '))
v = [valor, valor2, valor3]
ver = sorted(v)
#o sorted() coloca os valores em ordem crescente.
igual = (valor == valor2 and valor3) and (valor2 == valor and valor3) and (valor3 == valor and valor2)
i = (ver[0] == 0) and (ver[1] == 0) and (ver[2] == 0)

if(igual or i):
    print('Todos os três números são iguais !')
else:
    print(' O Menor número é {} \n E o Maior número é {}'.format(ver[0], ver[2]))
