# conferi qual é o maior número, o menor número e se ambos os números, são iguais.

print('Digite três números, e o programa lhe mostrará, qual é o Menor e o Maior número.')
print('>' * 30)
valor = float(input('Digite um número: '))
valor2 = float(input('Digite outro número: '))
valor3 = float(input('Digite mais um número: '))
lista = [valor, valor2, valor3]
ver = sorted(lista)
# o sorted() coloca os números em ordem crescente.
igual = (ver[0] == ver[1] and ver[2]) and (ver[1] == ver[0] and ver[2]) and (ver[2] == ver[0] and ver[1])
zero = (ver[0] == 0) and (ver[1] == 0) and (ver[2] == 0)

if(igual or zero):
    print('Todos os três números são iguais !')
else:
    print(f' O Menor número é: {ver[0]} \n E o Maior número é: {ver[2]}')

