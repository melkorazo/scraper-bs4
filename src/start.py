from process import Process

class Start(object):
    """ Web Scraper para prueba técnica 
            @autor Fabián Aravena
            @email fabian@aravena.dev
        
    """
    url = 'https://books.toscrape.com/index.html'

    def main(self):
        Process(self.url).process()
        print("FIN: Programa terminado")

if __name__ == '__main__':
    Start().main()
    
