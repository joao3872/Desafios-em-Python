def ler():
    import urllib
    import urllib.request

    site = str(input('Digite o linl do site: '))

    try:
        site1 = urllib.request.urlopen('https://www.'+site+'/')
    except urllib.request.URLError:
        print('Este Site, Não Está Acessível No Momento.')
    else:
        print('Este Site. Está Ativo !')
