from requests.exceptions import HTTPError
from utils.client import Client
from bs4 import BeautifulSoup
from data.connection import DB
from data.models import Article, Catalogue, Category


class Process(object):
    """ Clase con procesos para realizar Web scraping """
    pathDetails = 'catalogue/'
    catalogues = []
    lists = []
    articles = {}
    isNext = False
    i18n = {'obtener_categorias': 'INFO: Obteniendo categorías',
            'obtener_articulos': 'INFO: Obteniendo artículos',
            'error_proceso': 'ERROR: Ocurrio un problema al obtener URL: ',
            'error': 'ERROR: ',
            }

    def __init__(self, url, next=False):
        self.url = url
        self.urlDomain = url.split('/')[0] + '//' + url.split('/')[2]+'/'
        self.isNext = next

    def getDetails(self, url):
        url = self.pathDetails + url if self.pathDetails not in url else url
        detail = Client.getUrl((self.urlDomain + url if 'http' not in url else url))
        bsDetail = BeautifulSoup(detail.text, 'lxml')
        response = {'title': bsDetail.article.find('div', {'class': 'product_main'}).h1.text,
                   'thumbnail': self.urlDomain + bsDetail.article.find('div', {'class': 'thumbnail'}).div.div.img['src'].replace('../', ''),
                   'price': bsDetail.article.find('p', {'class': 'price_color'}).text,
                   'stock': bsDetail.article.find('p', {'class': 'availability'}).text.strip(),
                   'category': bsDetail.find('ul', {'class': 'breadcrumb'}).find_all('li')[2].text.strip(),
                   'description': bsDetail.article.find('p', {'class': ''}).text.strip() if bsDetail.article.find('p', {'class': ''}) else '',
                   'upc': bsDetail.article.find('table', {'class': 'table table-striped'}).td.text,
                   'url': url
                   }
        return response

    def article(self, content):
        print(self.i18n.get('obtener_articulos'))
        for element in content.ol.find_all('li'):
            dataArticle = self.getDetails(element.article.h3.a['href'])
            Article.objects.update_or_create(title=dataArticle.get(
                'title'), thumbnail=dataArticle.get('thumbnail'),
                price=dataArticle.get('price'),
                stock=dataArticle.get('stock'),
                category=Category.objects.filter(name=dataArticle.get('category')).first(),
                description=dataArticle.get('description'),
                upc=dataArticle.get('upc'),
                url=dataArticle.get('url'))
        DB().get_close_connection()
        return content

    def content(self, obCatalogue, content):
        for data in content:
            Category.objects.update_or_create(name=data.text.strip(
            ), url=self.urlDomain + data['href'], catalogue=obCatalogue)
            self.lists.append(
                {'name': data.text.strip(), 'url': self.urlDomain + data['href']})
        return self.lists

    def category(self, content):
        print(self.i18n.get('obtener_categorias'))
        for data in content:
            obCatalogue = Catalogue.objects.update_or_create(
                name=data.ul.a.text.strip())
            self.content(obCatalogue[0], data.ul.li.ul.find_all('a'))

    def process(self):
        try:
            DB().get_connection()
            site = Client.getUrl(self.url)
            bsObject = BeautifulSoup(site.text, 'lxml')
            if not self.isNext:
                self.category(bsObject.find_all(
                    'div', {'class': 'side_categories'}))
            article = self.article(bsObject.find('section'))
            next = article.find('ul', {'class': 'pager'}
                                ).find('li', {'class': 'next'})
            if next is not None:
                urlNext = next.a['href']
                print(urlNext)
                Process(self.urlDomain + (self.pathDetails if self.pathDetails not in urlNext else '') + urlNext, True).process()
        except HTTPError as eh:
            print(self.i18n.get('error_proceso'), eh)
        except Exception as e:
            print(self.i18n.get('error'), e)
