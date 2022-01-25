salario = float(input('Digite o seu salário: '))
aumentom = (salario * (10/100)) + salario
aumentoM = (salario * (15/100)) + salario

if(salario > 1250):
    print(' O seu salário era R${:.2f} \n Agora seu salário passa a ser R${:.2f}'.format(salario, aumentom))
else:
    print(' O seu salário era R${:.2f} \n Agora seu salário passa a ser R${:.2f}'.format(salario, aumentoM))
