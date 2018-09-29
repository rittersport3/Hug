import hug
import urllib.request


listaDeUrls = []
sair = 0;

# cli é usado para que o usuário interaja
# com a API a partir da linha de comando
@hug.cli
@hug.get()
def crawler():
    """Busque palavras em algum site"""
    retorno = []
    for url in listaDeUrls:
        conteudo = urllib.request.urlopen(url).read()
        conteudo = str(conteudo)
        retorno.append('Site : {0} - Número de Ocorrencias: '
                '{1}'.format(url, conteudo.count(palavra)))
    return 'Palavra pesquisada: {0} {1}'.format(palavra, str(retorno))

while sair == 0:
    url = input('Digite um site para adiciona-lo a lista (-1 para sair): ')
    if url == '-1':
        sair = -1;
    else:
        listaDeUrls.append(url)
        print('Site adicionado...')

palavra = input('Que palavra deseja pesquisar?: ')
