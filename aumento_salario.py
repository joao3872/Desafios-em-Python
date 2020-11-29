# salário superior a R$ 1250,00, ganha um aumento menor, e um salário menor, ganha um aumento maior.

salario = float(input('Digite o seu salário R$ '))
aumentom = (salario * (10/100)) + salario
aumentoM = (salario * (15/100)) + salario

if(salario > 1250):
    print(' Seu salário era R${salario :.2f} \n Com o aumento, seu salário passa a ser: R${aumentom :.2f}')
else:
    print(' Seu salário era R${salario :.2f} \n Com o aumento, seu salário passa a ser: R${aumentoM :.2f}')
