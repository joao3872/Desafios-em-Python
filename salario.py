salario = float(input('Informe o seu salário: R$ '))
desconto = (salario * (15/100))
aumento = (salario + desconto)

print(f'Seu salário era R$ {salario :.2f} \nAgora com 15% de aumento, você receberá R$ {aumento :.2f}')
print(f'Este é o valor dos 15% de aumento do seu salário: R$ {desconto :.2f}')
