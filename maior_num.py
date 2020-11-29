# confere, qual é o maior número, ou, se os dois são iguais. 

num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if(num > num2):
    print('O primeiro número é Maior !')
elif(num2 > num):
    print('O segundo número é Maior !')
else:
    print('Os dois números são iguais !')
