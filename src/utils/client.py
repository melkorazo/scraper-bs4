import requests

class Client:
    """ Clase para llamadas HTTP """

    def getUrl(url):
        try:
            r = requests.get(url)
            r.raise_for_status()
            return r
        except requests.exceptions.Timeout as et:
            raise et
        except Exception as e:
            raise e
            
