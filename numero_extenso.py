extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numero = int(input('Digite um número de 0 a 20: '))

while numero not in range(0, 21):
    numero = int(input('Tente novamente... Digite um número de 0 a 20: '))
print(f'Você digitou o número: {extenso[numero]}')
