# this is based on beautiful soup to scrape the main newsites in
# Colombia and extract the main news

from bs4 import BeautifulSoup
import requests


class el_tiempo():
    def __init__(self):
        self.titulares = self.first_scrap()


    def first_scrap(self):
        URL = 'https://www.eltiempo.com'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        titulares = (soup.
        find_all('a', {"class" : "title page-link"}))[1:]
        lista = []
        banned_cat = [
            '/vida/', 
            '/opinion/',
            '/contenido-comercial/',
            'deportes',
            'http://',
            'https://',
            '/cultura/'
            ]
        
        def esta_en(cat):
            for i in banned_cat:
                if i in cat:
                    return True
            return False
        def extraer_cat(href): 
            marker = False
            for c,i in enumerate(href):
                if i == '/':
                    if marker:
                        return href[inicio:(c)]
                    else:
                        marker = True
                        inicio = c

        
        for i in titulares:
            c_titular = {'href':None, 'categoria':None, 'titular':None}
            if esta_en(i['href']):
            #Esta en las categorias que no interesan
                continue
            else:
                c_titular['href'] ="https://www.eltiempo.com/" + i['href']
                c_titular['categoria'] = extraer_cat(i['href'])
                c_titular['titular'] = i.contents[0]
                lista.append(c_titular)

        return lista


#class el_colombiano(): 

class el_espectador():

    def __init__(self):

        self.titulares = self.first_scrap()


    def first_scrap(self):
        banned_cat=[
            '/opinion/',
            '/cultura/',
            '/entretenimiento/',
            '/deportes/'
        ]
        def esta_en(cat):
            for i in banned_cat:
                if i in cat:
                    return True
            return False

        URL = 'https://www.elespectador.com/'

        titulares = (
            BeautifulSoup(requests.get(URL).content, 'html.parser').
            find_all('a', {'class' : 'card-link'})
        )

        lista = []

        def extraer_cat(href): 
            marker = 0
            for c,i in enumerate(href):
                if i == '/':
                    if marker == 2:
                        return href[inicio:(c)]
                    elif marker==1:
                        inicio = c+1
        
                    marker += 1

        for i in titulares:
            try:
                c_titular = {'href':None, 'categoria':None, 'titular':None}
                c_titular['href'] = 'https://www.elespectador.com' + i['href']
                c_titular['categoria'] = extraer_cat(i['href'])

                if not esta_en(i['href']):
                    if (aux := i.find('span')):
                        c_titular['titular'] = aux.contents[0]
                    elif (aux := i.find('div')):
                        if len(aux.contents) != 0:
                            c_titular['titular'] = aux.find('h1').contents[0]
                    
                    if not c_titular['titular'] is None:
                        lista.append(c_titular)
            except:
                continue
        
        
        return lista



