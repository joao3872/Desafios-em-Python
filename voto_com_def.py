def voto(nascimento):
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, seu Voto é Opcional.'
    elif idade >= 18:
        return f'Com {idade} anos, seu voto é Obrigatório.'
    else:
        return f'Com {idade} anos, Não pode Votar.'
        
nascimento = int(input('Digite o ano de seu nascimento: '))
print(voto(nascimento))
