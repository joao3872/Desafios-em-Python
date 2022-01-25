vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'TRABALHAR')

for palavra in palavras:
    print(f'Na palavra {palavra} temos as vogais: ', end = '')
    
    for letras in palavra:
        if(letras.lower() in vogais):
            print(f'{letras.lower()}', end = ' ')
    print()
